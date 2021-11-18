import hashlib
import hmac
def checkSum(obj=[]):
    key = "19BDC82255CED" # need to discuss about the key
    message = []
    for i in range(len(obj)):
        if obj[i] != None:
            message.append(obj[i].strip()) 
    
    signature = hmac.new(
        key.encode(), 
        msg = "||".join(message).encode(), 
        digestmod = hashlib.sha256).hexdigest()

    return signature

print(checkSum(['365285', '2021-11-18 12:53:35','5000']))
