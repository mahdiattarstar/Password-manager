from add_password_screen import Base_screen
from kivy.app import App
from kivy.uix.screenmanager import Screen
from operations.password_generator import Password_generator
from Password_manager import shared_data
import pandas as pd
#class update 
class Update_password(Screen):
    def __init__(self,key_manager,data_base_dash,encrypt_data,valid_entry,**kwargs):
        super().__init__(**kwargs)  
   
#calling all the function and class that i need 
        self.key_manager=key_manager
        self.data_base_dash=data_base_dash
        self.encrypt_data=encrypt_data
        self.valid_entry=valid_entry
        self.update_pass=Password_generator()
        self.layout=Base_screen()
#chainging the title       
        self.layout.page_title.text='Update'    
#calling the button for update opretation
        self.layout.button_comfirm.bind(on_press=lambda instance: self.update_confirm())
        self.layout.back_button.bind(on_press=lambda instance: self.back_doshboard())
        self.add_widget(self.layout)
#this function is  for kivy (whenever update password is ready to called thid function is called too)
    def on_enter(self,*args):
        try:
            self.get_valeus()
            self.all_values()
        except:
             self.manager.current='dashboard'         
#the password generator button 
    def back_doshboard(self):
        self.manager.current='dashboard'
# the function get all the entries and ...
    def get_valeus(self):

        checking=self.data_base_dash.checking_id(shared_data.selected_row)
        key=self.key_manager.retrieve_key()
        self.df=pd.DataFrame([checking])
        encrypted_data=[col for col  in self.df.columns if col!= 'Id']
        self.df[encrypted_data]=self.df[encrypted_data].applymap(lambda encrypted: 
                                                                     self.encrypt_data.decryption(encrypted,key))
       
#put all values on the entries 
    
    def all_values(self):
        self.title=self.layout.title_ent.text=self.df['Title'].iloc[0]
        self.username=self.layout.user_name.text=self.df['Username'].iloc[0]
        self.email=self.layout.email.text=self.df['Email'].iloc[0]
        self.password=self.layout.password.text=self.df['Password'].iloc[0]
        self.note=self.layout.note.text=self.df['Note'].iloc[0]
#getting new inputs
    def update_confirm(self):
        try:
            tilte=self.layout.title_ent.text
            username=self.layout.user_name.text
            email=self.layout.email.text
            password=self.layout.password.text
            note=self.layout.note.text
            if not self.valid_entry.validate_email(email):
                self.layout.message_label.text=f'Invalid Email !'
                return False
            if not self.valid_entry.validate_password(password):
                self.layout.message_label.text=f'invalid password !'
                return False
            else:
             data_dict={'Title':tilte,'Username':username,'Email':email,
                           'Password':password,'Note':note}
             self.add_new_data(data_dict)
             self.clearing_entries()
             self.manager.current='dashboard'

        except:
                self.layout.message_label.text=f'please check the email, password ... again'
    def add_new_data(self,data_dict):
        key=self.key_manager.retrieve_key()
        encrypt_data={ke:self.encrypt_data.encrypt(val,key)for ke,val in data_dict.items()}
        self.data_base_dash.Update(self.df['Id'].iloc[0],encrypt_data['Title'],encrypt_data['Username'],
                                                encrypt_data['Email'],encrypt_data['Password'],encrypt_data['Note'])
      
     #clear all the entries
    def clearing_entries(self):
        list_ent=[self.layout.title_ent,self.layout.user_name,
                  self.layout.email,self.layout.password,self.layout.note]
        for clear in list_ent:
            clear.text=''
        self.layout.message_label.text=f'___' 
            
                
                      
               
