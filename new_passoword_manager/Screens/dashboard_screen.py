from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color,Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pandas as pd
import pyperclip


from Password_manager import shared_data
#creating doshboard screen 
class Doshboard(Screen):
    def __init__(self,key_manager,data_base_dash,encrypt_data,valid_entry,**kwargs):
        super().__init__(**kwargs)
#calling the classes fro getting or giving values for operations
        self.key_manager=key_manager
        self.encrypt_data=encrypt_data
        self.valid_entry=valid_entry
        self.data_base_dash=data_base_dash
        self.data_base_dash.create_table_dashboard()
        self.main_layout=BoxLayout(orientation='vertical')
#creating scroll bar  for the table           
        self.scroll=ScrollView(size_hint=(1,None),size=(700,300))
#creationg a layout for table with 5 columns and match it
        self.table_layout=GridLayout(cols=1,size_hint_y=None,spacing=2,  padding=[0, 20, 0, 0])
        self.table_layout.bind(minimum_height=self.table_layout.setter('height'))
        self.header = GridLayout(cols=6, size_hint_y=None, height=30) 
        self.table_header()
        self.scroll.add_widget(self.table_layout)
        self.main_layout.add_widget(self.scroll)
#searh entry and...     
        self.search_entry=TextInput(hint_text='Searching...',size_hint=(None,None),width=150,height=40)
        self.main_layout.add_widget(self.search_entry)
        show_button=Button(text='Show',size_hint=(None,None),width=150,height=40,color=(0,0,0,1))
        self.main_layout.add_widget(show_button)
        show_button.bind(on_press=lambda instance: self.showing())
        password_copy=Button(text='Copy Password',size_hint=(None,None),width=150,height=40,color=(0,0,0,1))
        password_copy.bind(on_press=lambda instance: self.copy_password())
        self.main_layout.add_widget(password_copy)
#add button
        add_button=Button(text='Add',size_hint=(0.8,None),width=200,height=40,color=(0,0,0,1))
        add_button.bind(on_press=lambda instance : self.Add_page())
        update_button=Button(text='Update',size_hint=(0.8,None),width=200,height=40,color=(0,0,0,1))
        update_button.bind(on_press=lambda instance: self.update_screen())
        delete_button=Button(text='Delete',size_hint=(0.8,None),width=200,height=40,color=(0,0,0,1))
        delete_button.bind(on_press=lambda instance: self.delete())
        self.main_layout.add_widget(add_button)
        self.main_layout.add_widget(update_button)
        self.main_layout.add_widget(delete_button)
              
        self.add_widget(self.main_layout)
    def on_center(self,*args):
       self.showing()
#updating the background color
    def update_bo_re(self,instance,values):
        self.bottom_re.pos=self.bottom_layot.pos
        self.bottom_re.size=self.bottom_layot.size
#the header of table
    def table_header(self):
    
        headers=['Id','Title','Username','Email','Password','Note']  
        for title in headers:
            header_t=Label(text=title,size_hint_y=None,height=40)
            self.header.add_widget(header_t)
        self.table_layout.add_widget(self.header)
            
        
#to visit add page
    def Add_page(self):
        self.manager.current='add_password'
    
    def update_screen(self):
        self.manager.current='update_password'
         
    def showing(self):
        try:
              self.table_layout.clear_widgets()
              self.header.clear_widgets()
              self.table_header()
              search_ent=self.search_entry.text
              decrypted_data=self.read_data_base()
              decrypted_data['Title']=decrypted_data['Title'].apply(lambda title : title if search_ent.lower()
                                                                    in title.lower() else None )
              filterd_data=decrypted_data.dropna(subset=['Title'])
             
           #   import pdb
              for item in filterd_data.values: 
                #pdb.set_trace()
                row=Click_row(item,self.on_row_select,self.table_layout)
                self.table_layout.add_widget(row)

              self.search_entry.text=''      
        except:
              self.table_layout.add_widget((Label(text=('you have not added so far!'),size_hint=(None,None),height=40)))
             
    def read_data_base(self):

        key=self.key_manager.retrieve_key()
        all_values=self.data_base_dash.read_all_values()    
        df=pd.DataFrame(all_values)
        
        encrypted_data=[ col for col in df.columns if col !='Id' ]
        df[encrypted_data]=df[encrypted_data].applymap(lambda encrypted_data: self.encrypt_data.decryption(encrypted_data,key))
        df['Password']=df['Password'].apply(lambda x : '*'* len(x)if isinstance(x,str)else x)
        return df      
    def on_row_select(self, selected_row):
        
         self.selected=selected_row.row_data[0]
         shared_data.selected_row=self.selected

    def check_dashboard(self):
        key=self.key_manager.retrieve_key()
#checking the id
        checked=self.data_base_dash.checking_id(self.selected)
#creating a dataframe
        df=pd.DataFrame([checked])
#checking all the columns(id can not be decrypted, so ...)
        encrypted_data=[col for col  in df.columns if col!= 'Id']
#encrypte others values
        df[encrypted_data]=df[encrypted_data].applymap(lambda encrypted: self.encrypt_data.decryption(encrypted,key))
        return df
#copy password that is commited a button   
    def copy_password(self):
        try:
            all_items=self.check_dashboard()
            password=all_items['Password'].iloc[0]
            pyperclip.copy(password)
        except :
            self.table_layout.add_widget((Label(text=('nothing has chosen!'),size_hint=(None,None),height=40)))
                 
    def delete(self):
        try:
          self.data_base_dash.delete_row(self.selected)
          self.showing()
        except:
            self.table_layout.add_widget((Label(text=('nothing has chosen!'),size_hint=(None,None),height=40)))
#a class for each click on the table                       
class Click_row(ButtonBehavior,GridLayout):
     def __init__(self,row_data,on_select,parent_layout, **kwargs):
          super().__init__(**kwargs)
          self.row_data=row_data
          self.parent_layout=parent_layout
          self.on_select=on_select
          self.cols=len(row_data)
          self.is_selected=False
          self.size_hint_y = None
          self.height = 40
 #we should put all the values from here (in this class)                                                                                       
          for item in self.row_data:
            label = Label(text=str(item), halign='center', valign='middle')
            label.bind(size=label.setter('text_size')) 
            self.add_widget(label)
 # Toggle selection state and call the callback function
     def on_press(self): 
        for child in self.parent_layout.children:
            if isinstance(child,Click_row):
                child.is_selected = False
                for widget in child.children:
                    widget.color = (1, 1, 1,1)            
        self.is_selected=True
        for widget in self.children:
            widget.color = (1, 0, 0, 1)
#it callbacks the function 
        self.on_select(self)