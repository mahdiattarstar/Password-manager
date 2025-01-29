import re
class Valid_entry:
#creating regex that check the email and match it 
    def validate_email(self,email):
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern,email) 
#creating regex that check the password and match it 
    def validate_password(self,password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&+=~`^\-<>])[A-Za-z\d@$!%*?&+=~`^\-<>]{8,}$'
        return re.match(pattern,password)