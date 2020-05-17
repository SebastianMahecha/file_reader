import tempfile, cv2, pytesseract, re, unidecode
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

class ImageUtils:

    def process_image_for_ocr(self, file_path):
        temp_filename = self.set_image_dpi(file_path)
        im_new = self.remove_noise_and_smooth(temp_filename)
        im = Image.fromarray(im_new)
        im.save(file_path)
        return im_new

    def set_image_dpi(self,file_path):
        im = Image.open(file_path)
        length_x, width_y = im.size
        factor = max(1, int(1800 / length_x))
        size = factor * length_x, factor * width_y
        im_resized = im.resize(size, Image.ANTIALIAS)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        temp_filename = temp_file.name
        im_resized.save(temp_filename, dpi=(600, 600))
        return temp_filename

    def image_smoothening(self,img):
        ret1, th1 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
        ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        blur = cv2.GaussianBlur(th2, (1, 1), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return th3

    def remove_noise_and_smooth(self,file_name):
        img = cv2.imread(file_name, 0)
        filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41,
                                        3)
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        img = self.image_smoothening(img)
        or_image = cv2.bitwise_or(img, closing)
        return or_image
    
    def get_text_from_document(self, img):
        
        text=pytesseract.image_to_string( img,config='-l spa --psm 6')
            
        text = re.sub('[a-z]', '', text)
        
        text = unidecode.unidecode(text)
        fiscal_number = ""            
        sex = ""
        first_name = ""
        last_name = ""
        try:
            if re.search(r'COLOMBIA', text):
                
                lines = text.split("\n")
                
                end_line = lines[-1]
                end_line_elements = end_line.split("-")
                fiscal_number = end_line_elements[4].lstrip("0")
                sex = end_line_elements[3]
                del lines[-1]
                
                text = '\n'.join(lines)

                text = re.sub(r'\b\w{,2}\b', '', text)
                text = re.sub(r"[^a-zA-Z.\d\s]", ' ', text)
                text = re.sub(r'[0-9]', '', text)
                text = re.sub('^[a-zA-Z0-9\\-\\s]+$', ' ', text)
                text = re.sub('[\.]','', text)
                text = text.strip()
                lines = text.split("\n")
                
                i = 0
                final_line = -1
                new_lines = []
                for line in lines:
                    
                    if "REPUBLICA" in line or "COLOMBIA" in line or "PERSONAL" in line or "CEDULA" in line  or "IDENTIFICACION" in line or "CIUDADANIA" in line  or "NNER" in line  or "NUME" in line or "NUMERO" in line:
                        new_lines = []
                    elif line.strip() == "" or "APELLIDOS" in line:
                        pass
                    else:
                        new_lines.append(line.strip().replace("  "," "))                    
                
                text = '\n'.join(new_lines)
                
                last_name = new_lines[0]
                if len(new_lines[2].replace(" ","")) > len(new_lines[1].replace(" ","")):
                    first_name = new_lines[2]
                else:
                    first_name = new_lines[1]
        except:
            print("error")
        return fiscal_number, first_name, last_name, sex
        