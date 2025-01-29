import secrets
import string
class Password_generator:
    def __init__(self):
        self.lenght=8
        self.lowercase=string.ascii_lowercase
        self.uppercase=string.ascii_uppercase
        self.digit=string.digits
        self.symbol='@$!%*?&+=~`^-<>'
        self.character_pool=self.lowercase+self.uppercase+self.digit+self.symbol
#producing password for dashboard   
    def password(self):
        password=''.join(secrets.choice(self.character_pool) for _ in range(self.lenght))
#to check if there is no upppercase in the password
        if  not any(c.isupper()for c in password):
            password=self.replace(password,secrets.choice(self.uppercase))
#to check if there is no number in the password
        if not any(c.isdigit()for c in password):
             password=self.replace(password,secrets.choice(self.digit))
#to check if there is no symbol in the password
        if not any( c in self.symbol  for c in password):
            password=self.replace(password,secrets.choice(self.symbol))
#to check if there is no lowercase in the password
        if not any(c in self.lowercase for c in password):
              password=self.replace(password,secrets.choice(self.lowercase))
        return password
  
    def replace(self,password,new_char):
#it produce an accident index in the password
        index=secrets.randbelow(len(password))
#and return password (consideraing the index , one of the word will be removed and new char replace it )
        return password[:index]+new_char+password[index+1:]