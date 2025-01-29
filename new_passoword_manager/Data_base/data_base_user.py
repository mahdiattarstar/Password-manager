import sys
from sqlalchemy import create_engine,MetaData,Table,Column,VARCHAR,INT
from sqlalchemy.sql import text
#creating a class for database (connecting to the online  data base)
class Data_base:
    def __init__(self):
        sys.stdout.reconfigure(encoding='utf-8') 
        #self.db_name=db_name
#all the information for connection
             
#connecting to the database and creating (connection pool)
       
        self.engine=create_engine(
            f'mysql+pymysql://mahdi:MahdiAttarzade2002@localhost/password_manager', 
             pool_size=5,
             max_overflow=10,
             echo=True
        ) 
    
#creating first table for login and sign with matadata(connection pool)
    def create_table_user(self):
        metaData=MetaData()
        user_table=Table('Users',metaData,
                         Column('Id',INT,primary_key=True,autoincrement=True),
                         Column('Username',VARCHAR(255)),
                         Column('Email',VARCHAR(255)),
                         Column('Password',VARCHAR(255)))
        metaData.create_all(self.engine)
            
#checking the input user name that if it exists in the table , it returns all the values
    def check_user(self,input_username:str):
        with self.engine.connect()as connection:
            query=text('''SELECT Id,Email,Password FROM Users WHERE Username=:Username''')
            result=connection.execute(query,{'Username':input_username}).fetchone()
            return result  if result else False      
#inserting username email passweord into the table 
    def insert_table(self,Username,Email,Password):
    
        with self.engine.connect()as connection:

            query=text('''INSERT INTO Users(Username,Email,Password)
                                    VALUES(:Username,:Email,:Password)
                                    ''')
            connection.execute(query,{'Username':Username,'Email':Email,'Password':Password})
            connection.commit()