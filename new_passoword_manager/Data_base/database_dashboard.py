from sqlalchemy import MetaData,Table,Column,VARCHAR,INT,text
from data_base_user import Data_base

class Database_doshboard(Data_base):
    def __init__(self):
        super().__init__()

#creating a table for doshboard
    def create_table_dashboard(self):
        meta_data=MetaData()
        doshboard_table=Table('Dashboard',meta_data,
                            Column('Id',INT,primary_key=True,autoincrement=True),
                            Column('Title',VARCHAR(255)),
                            Column('Username',VARCHAR(255)),
                            Column('Email',VARCHAR(255)),
                            Column('Password',VARCHAR(255)),
                            Column('Note',VARCHAR(255)))
        meta_data.create_all(self.engine)
#inserting into the table
    def insert_dashboard(self,title,username,email,password,note):
        with self.engine.connect()as connection:
            query=text('''INSERT INTO Dashboard(Title,Username,Email,Password,Note)
                          VALUES(:Title,:Username,:Email,:Password,:Note) ''')
            
            connection.execute(query,{'Title':title,'Username':username,
                                      'Email':email,'Password':password,'Note':note})
            connection.commit()

#getting all the values for dashboard table
    def read_all_values(self):
        with self.engine.connect()as connection:
            query=text('''SELECT * FROM Dashboard''')
            result=connection.execute(query).fetchall()
            connection.commit()
            return result
# checking the id and it exists , it gives its row  
    def checking_id(self,id:int):
        with self.engine.connect()as connection:
            query=text('''SELECT Id,Title,Username,Email,Password,Note FROM Dashboard WHERE Id=:Id''' )
            result=connection.execute(query,{'Id':id}).fetchone()
            connection.commit()
            return result
#delete the row ,considering its id
    def delete_row(self,id:int):
        with self.engine.connect()as connection:
            query=text('''DELETE FROM Dashboard WHERE Id=:Id''')
            connection.execute(query,{'Id':id})
            connection.commit()
#updating the row ,considering its id  


    def Update(self, id: int,title:str,username:str,email:str,passw:str,note:str):
        with self.engine.connect() as connection:
            query = text('''UPDATE Dashboard SET Title = :Title, Username=:Username ,Email=:Email, Password=:Password, Note=:Note    WHERE Id = :Id''')
            connection.execute(query, {'Id': id, 'Title':title,'Username':username,'Email':email,'Password':passw,'Note':note })
            connection.commit()




