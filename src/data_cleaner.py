import pandas as pd
from src.eda import Eda

class DataCleaner:
    
    def __init__(self,df: pd.DataFrame):
        self.df = df  
        
    #Droped high percent missing data
    def missing_data_fixed(self,summary):
        for col, percent in summary["high_missing"]:
            self.df.drop(columns=[col], inplace=True)
              
    #Droped all duplicate datas
    def duplicated_rows(self,duplicateDataCount):
     
       
       if duplicateDataCount>0:
           print(f"Removing {duplicateDataCount} duplicate rows")
           self.df = self.df.drop_duplicates().reset_index(drop=True) # index line fixed after dropping
       else:
           print("No duplicates found. Skipping...")
            
    #Droped all constant datas
    def drop_constant_columns(self,consData):
        if len(consData) > 0 :
         print(f"Dropping constant columns: {consData}")
         self.df = self.df.drop(columns=consData)        
        
       
        
        
        