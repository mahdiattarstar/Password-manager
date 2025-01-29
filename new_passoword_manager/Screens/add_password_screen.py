from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from operations.password_generator import Password_generator
class Base_screen(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) 

        self.add_password=Password_generator()  
#main layout
        self.orientation='horizontal'
        self.padding=20
        self.spacing=20
      
#column1 box layout
        column_1=FloatLayout(size_hint_x=0.3)
#creating a button for back to the dashboard
        self.back_button=Button(text='Back',size_hint=(None,None),pos_hint={'x':0.10,'y':0.95},width=100,height=30) 
        column_1.add_widget(self.back_button)
#creating a label for massaging 
        self.message_label=Label(text='____',font_size=15,size_hint=(None,None),pos_hint={'x':0.3,'y':0.08})
        column_1.add_widget(self.message_label)
#button for generating password
        self.genarate_pass=Button(text='ganerate password',size_hint=(None,None),
                             pos_hint={'x':0.30,'y':0.35},width=150,height=30)
        column_1.add_widget(self.genarate_pass)

#label for ...
        
#creating the next column for all the entries and ...
        column_2=BoxLayout(orientation='vertical',padding=10,size_hint_x=0.7,spacing=40)
        self.page_title=Label(text='_____',font_size=25,size_hint_x=0.45)
        column_2.add_widget(self.page_title)
        
#entry for title
        self.title_ent=TextInput(hint_text='Title...',size_hint=(None,None),width=230,height=50)
        column_2.add_widget(self.title_ent)
#entry for username
        self.user_name=TextInput(hint_text='Username...',size_hint=(None,None),width=230,height=50)
        column_2.add_widget(self.user_name)
#entry for email
        self.email=TextInput(hint_text='Email...',size_hint=(None,None),width=230,height=50)
        column_2.add_widget(self.email)
#entry for paassword
        self.password=TextInput(hint_text='Password...',size_hint=(None,None),password=True,width=230,height=50)
        column_2.add_widget(self.password)
#entry for note 
        self.note=TextInput(hint_text='Note...',size_hint=(None,None),width=230,height=50)
        column_2.add_widget(self.note)
#button for adding the new datas
        self.button_comfirm=Button(text='Confirm',size_hint=(None,None),width=230,height=50)
        column_2.add_widget(self.button_comfirm)

       
        self.genarate_pass.bind(on_press=lambda instance: self.password_generator())
      
        self.add_widget(column_1)
        self.add_widget(column_2)

    def password_generator(self):
        generated_pass=self.add_password.password()
        self.password.text=generated_pass
  
class Add_password(Screen) :
    def __init__(self,key_manager,data_base_dash,encrypt_data,valid_entry ,**kwargs):
        super().__init__(**kwargs)  
        self.key_manager=key_manager
        self.encrypt_data=encrypt_data
        self.valid_entry=valid_entry
        self.data_base_dash=data_base_dash
           
#calling the class that inherits all the ....
        self.layout=Base_screen()
#changing the page title
        self.layout.page_title.text='Add'
#the confirm button binds to the function
        self.layout.button_comfirm.bind(on_press=lambda instance:self.checking_entry())

        self.layout.back_button.bind(on_press=lambda instance: self.back_doshboard())
        self.add_widget(self.layout)
      
#the password generator button 
      

    def back_doshboard(self):
        self.manager.current='dashboard'
    
    def checking_entry(self):
#getting all the text
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
                
                self.add_new_password(data_dict)
        
#we did all of the before (no need to explain it)                  
        except:
            self.layout.message_label.text=f'please check the email, password ... again'
    def add_new_password(self,data_dict):
            key=self.key_manager.retrieve_key()
            encrypt_data={ke:self.encrypt_data.encrypt(val,key)for ke,val in data_dict.items()}

            self.data_base_dash.insert_dashboard(encrypt_data['Title'],encrypt_data['Username'],
                                                encrypt_data['Email'],encrypt_data['Password'],encrypt_data['Note'])
            self.clearing_entries()
            self.manager.current='dashboard'
#clear all the entries
    def clearing_entries(self):
        list_ent=[self.layout.title_ent,self.layout.user_name,
                  self.layout.email,self.layout.password,self.layout.note]
        for clear in list_ent:
            clear.text=''
        self.layout.message_label.text=f'___'