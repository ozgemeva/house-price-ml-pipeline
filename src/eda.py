import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

class Eda:
    def __init__(self,df: pd.DataFrame,bins):
        self.df = df
        self.bins = bins
         
    def dataset_overview(self):
        print("\n===== DATASET OVERVIEW =====")
    
        print(f"Shape: {self.df.shape}")
        print("\nHead:")
        print(self.df.head())

        print("\nDescribe:")
        print(self.df.describe())
        
    def number_of_missing_data(self):
        #to check how many missing data in column
        print("\n===== MISSING DATA ANALYSIS =====")
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
       
         # print 
        print("\nLOW (<5%)")
        for col, p in summary["low_missing"]:
            print(f"{col}: {p:.2f}%")

        print("\nMEDIUM (5-20%)")
        for col, p in summary["medium_missing"]:
            print(f"{col}: {p:.2f}%")

        print("\nHIGH (>20%)")
        for col, p in summary["high_missing"]:
         print(f"{col}: {p:.2f}%")
        
        return summary
        
    def is_duplicated_row(self):
        print("\n===== DUPLICATE CHECK =====")
        duplicate_count = self.df.duplicated().sum()
        total_rows = self.df.shape[0]
        duplicate_percent = (duplicate_count / total_rows) * 100
        print(f"Total duplicate rows: {duplicate_count}")
        print(f"Duplicate percentage: {duplicate_percent:.2f}%")
        
        if duplicate_count > 0:           
        
           print("\nSample duplicate rows:")
           print(self.df[self.df.duplicated()].head())
           
        else:
            print ("Dataset is clean.")
       
        return duplicate_count      
    
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
        
        if skew_value>1:
           print(f"\nInterpretation: Strong Right Skew: {skew_value:.2f}")
        elif skew_value<-1:
             print(f"\nInterpretation: Strong Left Skew: {skew_value:.2f}")
        else:
           print(f"\nInterpretation: Approximately Symmetric: {skew_value:.2f}")
        
        return {
        "skew": skew_value,
        "mean": mean_value,
        "median": median_value
         }
        
    """     
    def histogram(self,column_name,ax):
         # Histogram
        plt.figure()# create blank graph
        self.df[column_name].hist(bins=self.bins)#create 50 intervals
       
        ""
        1.bin 34.900-49.300
        2.bin 49.300 – 63.700
        50.bin -755.000
        ""
        plt.title(f"{column_name} Distribution")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.grid(False)
        plt.show()
        """ 
        
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



        
        
      
        
 
        
        
   
    
        