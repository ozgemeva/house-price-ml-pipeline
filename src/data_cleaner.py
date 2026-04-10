import pandas as pd
from src.eda import Eda

class DataCleaner:
    
    def __init__(self,df: pd.DataFrame):
        self.df = df  
        
    #Droped high percent missing data
    def missing_data_fixed(self,summary,dataType):
        dropped = {}
        filled ={}
        numerical_cols = dataType["numerical"]
        categorical_cols = dataType["categorical"]
        special_fill = {"PoolQC","MiscFeature","Alley","Fence","MasVnrType","FireplaceQu"}
        
        for col, percent in summary["high_missing"]:
            
            # 1. Numerical → drop
            if col  in  numerical_cols:
                self.df = self.df.drop(columns=[col],inplace=True)
                dropped[col] = "high missing numerical"
            
            # 2. Special categorical → fill
            elif col in special_fill:
                self.df[col] = self.df[col].fillna("None")
                filled[col] = "filled with 'None'"
                
            # 3. Other categorical → drop
            elif col in categorical_cols:
                self.df = self.df.drop(columns=[col],inplace=True)
                dropped[col] = "high missing categorical"
            
        return {
        "dropped": dropped,
        "filled": filled
                }   
              
    #Droped all duplicate datas
    def duplicated_rows(self,duplicateDataCount):
       removed = 0
       
       if duplicateDataCount>0:
           beforeDuplicateNum = len(self.df)
           self.df = self.df.drop_duplicates().reset_index(drop=True) # index line fixed after dropping
           afterDuplicateNum = len(self.df)
           removed = beforeDuplicateNum-afterDuplicateNum
           
       return{
            "duplicate_romoved" : removed
        }
          
    #Droped all constant datas
    def drop_constant_columns(self,consData):
        if len(consData) > 0 :
         print(f"Dropping constant columns: {consData}")
         self.df = self.df.drop(columns=consData)        
        
       
        
        
        