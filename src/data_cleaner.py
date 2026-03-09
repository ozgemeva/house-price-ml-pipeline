class DATACLEANER:
    
    def __init__(self,df):
        self.df = df
         
    def number_of_missing_data(self):
        #to check how many missing data in column
        print("\n===== MISSING DATA ANALYSIS =====")
        missing_percent = self.df.isnull().mean() * 100
        missing_percent = missing_percent[missing_percent > 0].sort_values(ascending=False)

        low_missing = []
        medium_missing = []
        high_missing = []

        for col,percent in missing_percent.items():
    
            if percent == 0:
                continue
            elif percent < 5:
               low_missing.append((col, percent))
            elif 5 < percent < 20 :
                medium_missing.append((col, percent))
            elif 20 < percent < 40:
                high_missing.append((col, percent))
                         
        print("\nLOW MISSING (<5%) → Fill with mode/median")
        print("-----------------------------------------")
        for col, percent in low_missing:
         print(f"{col}: {percent:.2f}%")

        print("\nMEDIUM MISSING (5–40%) → Consider imputation")
        print("---------------------------------------------")
        for col, percent in medium_missing:
         print(f"{col}: {percent:.2f}%")

        print("\nHIGH MISSING (>40%) → Consider dropping column")
        print("-----------------------------------------------")
        for col, percent in high_missing:
         print(f"{col}: {percent:.2f}%")
                
    def duplicated_rows(self):

        print("\n===== DUPLICATE CHECK =====")
        duplicated_count = self.df.duplicated().sum()
        print(f"\nDuplicate rows: {duplicated_count}")

        if duplicated_count == 0:
         print("Dataset is clean.")
            
    def data_clean(self):
        self.number_of_missing_data()
        self.duplicated_rows()