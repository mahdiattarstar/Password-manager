from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
class Login(App):
    def build(self):
#main layout
        layout=BoxLayout(orientation='horizontal',padding=50,spacing=50)
#column1 box layout
        column_1=BoxLayout(orientation='vertical',padding=2,size_hint_x=0.3,spacing=400)
       
#title
        column_1.add_widget(Label(text='Password manager',font_size=20))

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
        self.entry_pass=TextInput(hint_text='Password',size_hint=(None,None),width=300,height=50)
        column_2.add_widget(self.entry_pass)
#buttom confirm
        self.button_con=Button(text='confirm',size_hint=(None,None),width=300,height=50)
        column_2.add_widget(self.button_con)

        layout.add_widget(column_1)
        layout.add_widget(column_2)


        

        return layout
    
        

