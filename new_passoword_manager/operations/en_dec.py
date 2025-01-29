from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import base64
from hashlib import sha256
class Encription:
    def encrypt(self,data,key):
#creating a chiper and how mode_cbc is a kind of encryption
        chiper= AES.new(key,AES.MODE_CBC)
#it encryptes the data and it is become a bytes here
        ct_bytes=chiper.encrypt(pad(data.encode(),AES.block_size))
# iv is a first value that will be combined with ct(iv works with chiper and ct with encrypted data)
        iv=base64.b64encode(chiper.iv).decode('utf-8')
        ct=base64.b64encode(ct_bytes).decode('utf-8')
        result=f'{iv}:{ct}'
        return result
    
    def decryption(self,encrypted_data,key):
#checking if iv and ct is not separated
        if ":" not in encrypted_data:
           raise ValueError("Invalid encrypted data format. Expected 'iv:ct' format")
#it splits and puts it into the two variables  
        iv_b64,ct_b64=encrypted_data.split(':')
#both of have to become bytes agaen with base4    
        iv=base64.b64decode(iv_b64)
        ct=base64.b64decode(ct_b64)
#choosing the model of decrypt 
        chiper=AES.new(key,AES.MODE_CBC,iv)
#  decryption  and return it
        decrypted_data=unpad(chiper.decrypt(ct),AES.block_size)
        return decrypted_data.decode('utf-8')