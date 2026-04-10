import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

class Eda:
    def __init__(self,df: pd.DataFrame,bins):
        self.df = df
        self.bins = bins
      
  # ---------------- CORE ----------------   
    def dataset_overview(self):
        print("\n===== DATASET OVERVIEW =====")
    
        print(f"Shape: {self.df.shape}")
        print("\nHead:")
        print(self.df.head())

        print("\nDescribe:")
        print(self.df.describe())
        
    def number_of_missing_data(self):
        #to check how many missing data in column
        missing_percent = self.df.isnull().mean() * 100
        missing_percent = missing_percent[missing_percent > 0].sort_values(ascending=False)
       
        summary = {
            "low_missing" : [],
            "medium_missing" : [],
            "high_missing" : []
            }

        for col,percent in missing_percent.items():
    
            if percent < 5:
                summary["low_missing"].append((col, percent))
            elif percent < 20:
                summary["medium_missing"].append((col, percent))
            else:
                summary["high_missing"].append((col, percent))                 
        
        return summary
    
    def analyze_high_missing(self,summary):
        result ={}
        for col, percent in summary["high_missing"]:
         result[col] = {
            "value_counts": self.df[col].value_counts(dropna=False),
            "nan_count": self.df[col].isna().sum(),
            "missing_percent": percent
        }
         return result

            
        
    def is_duplicated_row(self):
          duplicate_count = self.df.duplicated().sum()
          total_rows = self.df.shape[0]
          duplicate_percent = (duplicate_count / total_rows) * 100

          return {
            "count": duplicate_count,
            "percent": duplicate_percent
          }   

    def get_columns_by_type(self):
        #data_type = self.df.select_dtypes(include=dtype).columns.tolist()     
        #tolist() = pandas obj conver to python list.
       cols = {
        "categorical": self.df.select_dtypes(include=["object", "category"]).columns.tolist(),
        "numerical": self.df.select_dtypes(include=["number"]).columns.tolist(),
        "boolean": self.df.select_dtypes(include="bool").columns.tolist(),
        "datetime": self.df.select_dtypes(include=["datetime64[ns]"]).columns.tolist(),
        }   
       return cols
    
    def target_analysis(self,column_name):
        print(f"\n===== TARGET ANALYSIS: {column_name} =====")
        desc = self.df[column_name].describe()
        print(desc)
        
        skew_info = self.check_skew(column_name)
        print(f"\nMean: {skew_info['mean']}")
        print(f"Median: {skew_info['median']}")
    
    def check_skew(self, column_name): 
        data = self.df[column_name].dropna()
        
        skew_value=data.skew()
        mean_value=data.mean()
        median_value=data.median()
        interpretation = "symmetric"
        
        if skew_value>1:
           interpretation = "strong_right"
    
        elif skew_value<-1:
           interpretation = "strong_left"
                
        return {
        "column": column_name,
        "skew": skew_value,
        "mean": mean_value,
        "median": median_value,
        "interpretation": interpretation
        }
        
    def histogram(self, column_name, ax):
         data = self.df[column_name].dropna()
         skew = data.skew()
         ax.hist(data, bins=self.bins)
         ax.set_title(f"{column_name} Distribution, (skew={skew:.2f})")
         ax.set_xlabel(column_name)
         ax.set_ylabel("Frequency")
         ax.axvline(data.mean(), linestyle="dashed", linewidth=1)
         ax.axvline(data.median(), linestyle="dotted", linewidth=1)
         ax.grid(False)
    
    def compare_columns(self, col1, col2, save_path=None):
        
        fig, axes = plt.subplots(1, 2, figsize=(12,5))

        self.histogram(col1, axes[0])
        self.histogram(col2, axes[1])

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
            print(f"Saved to {save_path}")
        else:
             plt.show()
             
    #To include all same value of each data
    def constant_data(self):   
        constant_columns = [col for col in self.df.columns
        if self.df[col].nunique(dropna=False) == 1] # include NaN 
        #constant columns
        return constant_columns
    
    def detect_outliers_all(self):
        results = {}
        cols = self.get_columns_by_type()["numerical"]
        total_rows = len(self.df)
        
        #IQR value = q3-q1 --> %75 - %25 = %50 
        for col in cols:
            Q1= self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR =  Q3 - Q1 
            upper_outlierBorder = Q3 + 1.5 * IQR
            lower_outlierBorder = Q1 - 1.5 * IQR
           
            #col < lower   or   col > upper
            outliers = self.df [ (self.df[col] < lower_outlierBorder) | (self.df[col] > upper_outlierBorder) ]
            
            count = len(outliers)
            percent = (count / total_rows) * 100
        
        results[col] = {
            "count": count,
            "percent": percent,
            "lower_bound": lower_outlierBorder,
            "upper_bound": upper_outlierBorder
             }
                
   # ---------------- GROUP ----------------
    def run_general(self):
        #self.dataset_overview()
        missing = self.number_of_missing_data()
        dup = self.is_duplicated_row()

        return {
        "missing": missing,
        "duplicates": dup
        }
    
    def run_numerical(self, target=None): #Target= Opsiyonel
        results = []
        cols = self.get_columns_by_type()["numerical"]
        
        for col in cols:
            skew_info = self.check_skew(col)
            results.append(skew_info)
        
        target_summary = None

        if target:
           target_summary = self.df[target].describe()
        
        return{
            "skew_results": results,
            "target_summary": target_summary
        } 
           

    def run_categorical(self):
            print("\n===== CATEGORICAL EDA =====")
            cols = self.get_columns_by_type()["categorical"]
            print("Categorical cols:", cols)

            constants = self.constant_data()
            print("Constant cols:", constants)
        
        
   
    
        