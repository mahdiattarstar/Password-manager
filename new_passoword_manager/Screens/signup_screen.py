from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
import logging

class Sign_up(Screen):
        def __init__(self,key_manager,data_base,hash_password,encrypt_data,valid_entry,**kwargs):
            super().__init__(**kwargs)
            self.key_manager=key_manager
            self.data_base=data_base
            self.hash_password=hash_password
            self.encrypt_data=encrypt_data
            self.valid_entry=valid_entry
      
#main layout
            layout=BoxLayout(orientation='horizontal',padding=50,spacing=50)
#column1 box layout
            column_1=BoxLayout(orientation='vertical',padding=2,size_hint_x=0.3,spacing=100)
       
#title
            column_1.add_widget(Label(text='Password manager',font_size=20))
#for the messaging
            self.message=Label(text='_____',font_size=15)

            column_1.add_widget(self.message)

#icon  
            icon=Image(source='C:\\Users\\user\\Desktop\\new_passoword_manager\\icons\\key.png',size_hint=(None,None))
            column_1.add_widget(icon)
#creating column 2 for entries and button
            column_2=BoxLayout(orientation='vertical',padding=20,spacing=50)
#sign_up label
            column_2.add_widget(Label(text='Login',font_size=40,size_hint_x=0.6))
#entry user name 
            self.entry_user_name=TextInput(hint_text='User name',size_hint=(None,None),width=300,height=50)
            column_2.add_widget(self.entry_user_name)
#entry email
            self.entry_email=TextInput(hint_text='Email',size_hint=(None,None),width=300,height=50)
            column_2.add_widget(self.entry_email)
#entry password
            self.entry_pass=TextInput(hint_text='Password',size_hint=(None,None),password=True,width=300,height=50)
            column_2.add_widget(self.entry_pass)
#buttom confirm
            self.button_con=Button(text='confirm',size_hint=(None,None),width=300,height=50)
            self.button_con.bind(on_press= lambda instance :self.getting_entry())
            column_2.add_widget(self.button_con)

            layout.add_widget(column_1)
            layout.add_widget(column_2)
# you have add the main_layout to the self that mention to the class
            self.add_widget(layout)
#function for confirming the user 
        def getting_entry(self):
          try:

#getting all the entries(username,email,password)
            user_name_input=str(self.entry_user_name.text)
            email_input=str(self.entry_email.text)
            password_input=str(self.entry_pass.text)
            self.user_login(user_name_input,email_input,password_input)
          except :
             self.message.text=f'sth went wrong (valuses, internet) ! '

        def user_login(self,username_in,email_in,password_in):
          try:
#calling the key for decrypting 
            key=self.key_manager.retrieve_key()
#this function checks the username and if it true ,it turns id and email and password 
            Id,email,password=self.data_base.check_user(username_in)
#this function decrypte the email with the key
            email_decrypted=self.encrypt_data.decryption(email,key)
#checking the password and email 
            if self.hash_password.check_password(password_in,password) and self.emails_compare(email_in,email_decrypted):
                 self.message.text=f'you can use passwordmanager now'
                 self.manager.current='dashboard'
              
            else:
                self.message.text=f'there is no user with this  !'

          except :
             self.message.text=f'sth went wrong (valuses, internet) ! '
                    
#this function compares input user with the sorted email and if it is true it turns a true(bool)    
        def emails_compare(self,input_user:str,email:str)->bool:
           return input_user==email