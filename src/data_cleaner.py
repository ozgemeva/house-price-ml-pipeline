import pandas as pd
from src.eda import Eda

class DataCleaner:
    
    def __init__(self,df: pd.DataFrame):
        self.df = df  
        
        #Droped high percent missing data
    def missing_data_fixed(self):
        summary = Eda.number_of_missing_data()

        for col, percent in summary["high"]:
          self.df.drop(columns=[col], inplace=True)
            
    def duplicated_rows(self):
       duplicateDataCount = Eda.is_duplicated_row()
       
       if duplicateDataCount>0:
           print(f"Removing {duplicateDataCount} duplicate rows")
           self.df = self.df.drop_duplicates()
       else:
           print("No duplicates found. Skipping...")
       
         
    def find_dtype_columns(self):
        #data_type = self.df.select_dtypes(include=dtype).columns        
        cols = {
            "categorical_cols": self.df.select_dtypes(include="object").columns,
            "numerical_cols" : self.df.select_dtypes(include=["number"]).columns,
            "boolean_cols" : self.df.select_dtypes(include="bool").columns,
            "datetime_cols" : self.df.select_dtypes(include="datetime64").columns,
        }
        return cols
    
    def check_data_info(self):
        #to check data type
        cols = self.find_dtype_columns()

        cols = { k:v for k , v in cols.items() if len (v) >0 }    
        print("\n===== COLUMN GROUPS =====")
       
        for name, columns in cols.items():
           print(f"\n{name}: {list(columns)}")

        return cols             
                

    
    def seperated_columns(self):
        cols = self.find_dtype_colum()
        categorical_cols = cols["categorical_cols"]
        numerical_cols = cols["numerical_cols"]
        return numerical_cols,categorical_cols
    
    #To include all same value of each data
    def constant_data(self):
    
        constant_columns = [col for col in self.df.columns
        if self.df[col].nunique(dropna=False) == 1]

        #constant columns
        return constant_columns
        
    def drop_data(self):
        cons = self.constant_data()
        if len(cons) > 0 :
         print("Dropping constant columns:" )
         self.df = self.df.drop(columns=cons)        

    def data_clean(self):
        """self.number_of_missing_data()
        self.duplicated_rows()
        self.check_data_info()
        self.find_dtype_columns()
        self.seperated_columns()
        self.constant_data()"""
     
        
       
        
        
        