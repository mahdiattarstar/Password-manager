from Crypto.Random import get_random_bytes
import win32cred
import base64
import keyring
# screating a key for encryption and decryption
class KEY:
    def __init__(self):
        self.name_key='password'
        self.username='Attar'
    
#storing the key with sting      
    def store_key(self,key):
#it must be become a str for sorting 
        key_base64=base64.b64encode(key).decode('utf-8')
#writing with its informations
        credWrite=({
            'TargetName':self.name_key,
            'Type':win32cred.CRED_TYPE_GENERIC,
            'Persist':win32cred.CRED_PERSIST_LOCAL_MACHINE,
            'CredentialBlob':key_base64,
            'UserName':self.username
        })
        win32cred.CredWrite(credWrite)
#creating the key with a randon 32 bytes
    def genate_key(self):
        return get_random_bytes(32)
#reading the key and chenaged to the bytes for encryotion and decryption
    def retrieve_key(self):
            credential =win32cred.CredRead(self.name_key,win32cred.CRED_TYPE_GENERIC)
            key_base64=credential['CredentialBlob']
            key=base64.b64decode(key_base64)
            return key
#checking the key if it is already created or not (login and signup)
    def check_key(self):
         service_name=self.name_key
         user_name=self.username
         password=keyring.get_password(service_name,user_name)
         return password
         