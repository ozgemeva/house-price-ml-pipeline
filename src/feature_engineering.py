import numpy as np
 
class FeatureEngineering:
    def __init__(self, df, target):
        self.df = df
        self.target = target

    def log_transform_target(self):
        new_column = f"{self.target}_log"

        if new_column not in self.df.columns:
            self.df[new_column] = np.log1p(self.df[self.target])

        return self.df
    
   
        