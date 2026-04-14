import pandas as pd
from src.eda import Eda

class DataCleaner:

    
    def __init__(self,df: pd.DataFrame):
        self.df = df  
        
    #Droped high percent missing data
    def handle_high_missing(self,summary,dataType):
        dropped = {}
        filled ={}
        numerical_cols = dataType["numerical"]
        categorical_cols = dataType["categorical"]
        special_fill = {"PoolQC","MiscFeature","Alley","Fence","MasVnrType","FireplaceQu"}
        
        for col, percent in summary["high_missing"]:
            
            # 1. Numerical → drop
            if col  in  numerical_cols:
                self.df = self.df.drop(columns=[col])
                dropped[col] = "high missing numerical"
            
            # 2. Special categorical → fill
            elif col in special_fill:
                self.df[col] = self.df[col].fillna("None")
                filled[col] = "filled with 'None'"
                
            # 3. Other categorical → drop
            elif col in categorical_cols:
                self.df = self.df.drop(columns=[col])
                dropped[col] = "high missing categorical"
            
        return  { "dropped": dropped, "filled": filled }   
    
    def handle_medium_missing(self,summary,dataType):
        dropped = {}
        filled ={}
        
        numerical_cols = dataType["numerical"]  
        for col,percent in summary ["medium_missing"]:
            if col in numerical_cols:
                self.df[col] = self.df[col].fillna(self.df[col].median())
                filled[col] = "filled with 'Median'"
                print("Now filling:", col)
                print("median:  ",self.df[col].median())
                
       
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
    def drop_constant_columns(self, consData):
        if len(consData) > 0:

        # SalePrice koruma
         consData = [col for col in consData if col != "SalePrice"]

        print(f"Dropping constant columns: {consData}")
        self.df = self.df.drop(columns=consData)

        return {}     
        
    def clean(self,summary,dataType,duplicateDataCount,consData):
         df = self.df.copy()
         df = self.handle_high_missing(summary,dataType)
         df = self.handle_medium_missing(summary,dataType)
         df = self.duplicated_rows(duplicateDataCount)
         df = self.drop_constant_columns(consData)
         
        
         
         clean_result = {"filled": {},"dropped": {} }
         
         filled_info = self.handle_high_missing(summary, dataType)
         clean_result["filled"] = filled_info
         
         filled_info = self.handle_medium_missing(summary, dataType)
         clean_result["filled for medium missing"] = filled_info
         
         df = self.duplicated_rows(duplicateDataCount)
         dropped_info = self.drop_constant_columns(consData)
         clean_result["dropped"] = dropped_info
        
         return self.df,clean_result
       
        
        
        