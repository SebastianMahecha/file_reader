import unidecode

class CommonsUtils():
    def clean_text(self, text):
        
        text = text.lower()
        text = text.replace(" ", "")
        text = unidecode.unidecode(text)
        return text
