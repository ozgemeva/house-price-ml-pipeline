import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

class EDA:
    def __init__(self,df: pd.DataFrame,bins):
        self.df = df
        self.bins = bins
         
    def sanity_check(self):
        #to use shape function to learn "how many number of row and number of column (santiy check)"
        dfShape = self.df.shape
        print('\nShape:')
        print(dfShape)      
        
    def check_head(self):
        #to check data format and column name and available target data
        dfHead = self.df.head()
        print('\nHead:')
        print(dfHead)
        
    def check_describe(self):
        #to get statistic value from all cloumn , check Non-null count,numeric and categorical column
        statisticColumn = self.df.describe(include=[np.number])
        print("\nNumerical Summary:")
        print(statisticColumn)
        
    def target_analysis(self,column_name):
        #SalePrice is target value
        print(f"\n{column_name} Summary:")
        print(self.df[column_name].describe()) 
    
    def check_skew(self, column_name): 
        skew_value=self.df[column_name].skew()
        mean_value=self.df[column_name].mean()
        median_value=self.df[column_name].median()
        
        print(f"Mean: {mean_value:.0f}")
        print(f"Median: {median_value:.0f}")
          
        if skew_value>1:
           print(f"\nInterpretation: Strong Right Skew: {skew_value:.2f}")
        elif skew_value<-1:
             print(f"\nInterpretation: Strong Left Skew: {skew_value:.2f}")
        else:
           print(f"\nInterpretation: Approximately Symmetric: {skew_value:.2f}")
        return skew_value
        
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
         skew = self.df[column_name].skew()
         ax.hist(self.df[column_name], bins=self.bins)
         ax.set_title(f"{column_name} Distribution, (skew={skew:.2f})")
         ax.set_xlabel(column_name)
         ax.set_ylabel("Frequency")
         ax.grid(False)
    
    def compare_columns(self, col1, col2):
        fig, axes = plt.subplots(1, 2, figsize=(12,5))

        self.histogram(col1, axes[0])
        self.histogram(col2, axes[1])

        plt.tight_layout()
        plt.savefig("hist.png")
        plt.close()
    
    def dataset_overview(self):
        self.sanity_check()
        self.check_head()
        self.check_describe()
        
    def target_overview(self,column_name): 
        print("\n===== TARGET ANALYSIS =====")
        #self.target_analysis(self.df[column_name])
        self.check_skew(column_name)
    

        
        
      
        
 
        
        
   
    
        