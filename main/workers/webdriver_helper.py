import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebdriverHelper():
    
    def __init__(self, driver_path): 
        chrome_options = Options()
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
        
    
    def open_page(self, url):
        self.driver.get(url)
    
    def close_page(self):
        self.driver.close()

    def find_element_by_id(self, element_id):
        return self.driver.find_element_by_id(element_id)
    
    def find_elements_by_class(self, class_name):
        return self.driver.find_elements_by_class_name(class_name)        
    
    def find_element_by_tag_attribute(self, tag, attribute, value):        
        return self.driver.find_element_by_xpath('//'+tag+'[@'+attribute+'="'+str(value)+'"]')
    
    def find_element_by_path(self, value):        
        return self.driver.find_element_by_xpath(value)
    
    def find_elements_by_path(self, value):        
        return self.driver.find_elements_by_xpath(value)
    
    def find_elements_by_tag_attribute(self, tag, attribute, value):         
        return self.driver.find_elements_by_xpath('//'+tag+'[@'+attribute+'="'+str(value)+'"]')

    def show_by_id(self, element_id):        
        self.driver.execute_script("arguments[0].style.display = 'block';", self.find_element_by_id(element_id))
    
    def click_by_id(self, element_id):
        self.find_element_by_id(element_id).click()
    
    def click_by_tag_attribute(self, tag, attribute, value):
        self.find_element_by_tag_attribute(tag, attribute, value).click()

    def set_value_by_id(self, element_id, value):
        self.find_element_by_id(element_id).send_keys(value)
    
    def back(self):
        return self.driver.back()
    def wait(self, seconds = None):
        if seconds:
            time.sleep(seconds)
        else:
            time.sleep(5)
        


