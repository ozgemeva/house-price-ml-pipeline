import matplotlib.pyplot as plt 
import numpy as np

class EDA:
    def __init__(self,df,target,bins):
        self.df = df
        self.target = target
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
        
    def check_data_info(self):
        #to check missing data 
        print("\nData Info:")
        self.df.info()
        
    def check_describe(self):
        #to get statistic value from all cloumn , check Non-null count,numeric and categorical column
        statisticColumn = self.df.describe(include=[np.number])
        print("\nNumerical Summary:")
        print(statisticColumn)
    
    def number_of_missing_data(self):
        #to check how many missing data in column
        numMissingData = self.df.isnull().sum()
        print("\nNumber of Missing Data:")
        print(numMissingData.sort_values(ascending=False))
        
    def target_analysis(self):
        #SalePrice is target value
        print("\nSalePrice Summary:")
        print(self.df[self.target].describe()) 
    
    def check_skew(self, column_name):
        
        skew_value=self.df[column_name].skew()
        
        if skew_value>1:
           print("Strong Right Skew:", skew_value)
        elif skew_value<-1:
             print("Strong Left Skew:", skew_value)
        else:
           print("Approximately Symmetric:", skew_value)
            
        print(f"{column_name} skew: {skew_value}")
        
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
         ax.hist(self.df[column_name], bins=self.bins)
         ax.set_title(f"{column_name} Distribution")
         ax.set_xlabel(column_name)
         ax.set_ylabel("Frequency")
         ax.grid(False)
    
    def compare_columns(self, col1, col2):
        fig, axes = plt.subplots(1, 2, figsize=(12,5))

        self.histogram(col1, axes[0])
        self.histogram(col2, axes[1])

        plt.tight_layout()
        plt.show()
                
        
        
   
    
        