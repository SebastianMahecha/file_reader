import json, random
import hashlib as hl
import base64 as b64

class CommonUtils:
    
    def create_token(self):
        
        na = int(random.randint(10**13, 10**23)*random.random()*random.random()*random.random())
        nb = int(random.randint(10**13, 10**23)*random.random()*random.random()*random.random())
        nc = na*nb*727
        nb = nc / (na*727)
        pub = hl.sha512()
        pub.update(str(nb).encode('utf8'))
        token = pub.hexdigest()
        token = b64.b64encode(token.encode('utf8')).decode('utf8')
        
        return token