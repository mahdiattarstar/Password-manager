from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from Password_manager.validate_en import Valid_entry
from Password_manager.hash import Bcrypt_hash
from Password_manager.encription import Encription
from Password_manager.key_manager import KEY
from Password_manager.data_base import Data_base
class Sign_up(App):
    def build(self):
        self.valid_entry=Valid_entry()
        self.hash_password=Bcrypt_hash()
        self.encrypt_data=Encription()
        self.key=KEY()
        self.data_base=Data_base()
#main layout
        layout=BoxLayout(orientation='horizontal',padding=50,spacing=50)
#column1 box layout
        column_1=BoxLayout(orientation='vertical',padding=2,size_hint_x=0.3,spacing=100)
       
#title
        column_1.add_widget(Label(text='Password manager',font_size=20))
#a lebel for messegging
        self.message=Label(text='_____',font_size=15)

        column_1.add_widget(self.message)

#icon  
        icon=Image(source='C:\\Users\\user\\Desktop\\new_passoword_manager\\icons\\key.png',size_hint=(None,None))
        column_1.add_widget(icon)
#creating column 2 for entries and button
        column_2=BoxLayout(orientation='vertical',padding=20,spacing=50)
#sign_up label
        column_2.add_widget(Label(text='SignUP',font_size=40,size_hint_x=0.6))
#entry user name 
        self.entry_user_name=TextInput(hint_text='User name',size_hint=(None,None),width=300,height=50)
        column_2.add_widget(self.entry_user_name)
#entry email
        self.entry_email=TextInput(hint_text='Email',size_hint=(None,None),width=300,height=50)
        column_2.add_widget(self.entry_email)
#entry password
        self.entry_pass=TextInput(hint_text='Password',size_hint=(None,None),width=300,height=50)
        column_2.add_widget(self.entry_pass)
#buttom confirm
        self.button_con=Button(text='confirm',size_hint=(None,None),width=300,height=50)
        self.button_con.bind(on_press=lambda instance : self.add_new_user())
        column_2.add_widget(self.button_con)

        layout.add_widget(column_1)
        layout.add_widget(column_2)

        return layout
    
#we have just one user in this app,this function gets all the entries and finally they will be sorted in a table(mysql)
    def add_new_user(self):
      #  try:
            user_name=self.entry_user_name.text
            email=self.entry_email.text
            password=self.entry_pass.text
#check the email and password if its not right
            if not self.valid_entry.validate_email(email):
                self.message.text=f'Wrong Email!'
                return False
            
            if not self.valid_entry.validate_password(password):
                self.message.text=f'not safety password !'
                return False
            else:
               key=self.key.retrieve_key()
               user_name=self.encrypt_data.encrypt(user_name,key)
               email=self.encrypt_data.encrypt(email,key)
               password=self.hash_password.hash_passworsd(password)
               self.data_base.insert_tabel(user_name,email,password)

                
               self.message.text=f'You could sign up successfully'
                
#you should not use ()for this becouse the python thinks ,you call a function
                
      #  except:
        #    pass
        
        
            
        



        

