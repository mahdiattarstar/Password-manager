from bcrypt import hashpw,gensalt,checkpw
#creating class for password
class Bcrypt_hash:
#hash password with bcrypt algorithm and returned
    def hash_passworsd(self,password):
        hash=hashpw(password.encode(),gensalt())
        return hash
# checking the input password with sorted password and if it is ok, it returns a true if not false
    def check_password(self,input_password,sorted_password)->bool:
        sorted_password=sorted_password.encode()

        return checkpw(input_password.encode(),sorted_password)
    
    

        