import numpy as np
 
class FeatureEngineering:
    def __init__(self, df, target):
        self.df = df
        self.target = target
            
    def log_transform_target(self):
        log_column_name = f"{self.target}_log"
        self.df[log_column_name] = np.log1p(self.df[self.target])
        return log_column_name
   
        