import pandas as pd
class DataLoader:
    def __init__(self, path):
         #to read data end to add in memory
        self.df = pd.read_csv(path)
            
    def get_data(self):
        return self.df
    

        
   
    
    
    