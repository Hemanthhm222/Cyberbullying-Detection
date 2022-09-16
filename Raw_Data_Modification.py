from Logging_files import logger
import pandas as pd

class data_arrange():
    
    def __init__(self,data):
        self.data = data
        self.log_writter = logger.Logger()
    
    def dropping_waste_class(self,df):
        try:
            data = df
            data.drop(data[data['sentiment']=='other_cyberbullying'].index,inplace=True)
            return data
            
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e
    
    def rename_columns(self):
        try:
            data = self.data
            data = data.rename(columns={'tweet_text':'text','cyberbullying_type':'sentiment'})
            return data
        
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e
    
    def data_encoding(self,df):
        try:
            data=df
            data['sentiment'].replace({'religion':1,'age':2,'gender':3,'ethnicity':4,'not_cyberbullying':5},inplace=True)
            return data
        
        except Exception as e:
            file_object = open("Logging_files/Training_logs.txt","a+")
            self.log_writter.log(file_object,f"An Errror occurred :: {e}")
            file_object.close()
            raise e
    