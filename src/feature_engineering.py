import numpy as np
 
class FeatureEngineering:
    def __init__(self, df, target):
        self.df = df
        self.target = target
            
    def log_transform_target(self):
        new_column = f"{self.target}_log"
        self.df[new_column] = np.log1p(self.df[self.target])
        return new_column
   
        