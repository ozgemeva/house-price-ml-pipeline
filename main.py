from src.data_loader import DataLoader
from src.feature_engineering import FeatureEngineering 
from src.config import Config
from src.eda import Eda
from src.data_cleaner import DataCleaner

def main():
    RUN_FULL_EDA = Config.RUN_FULL_EDA
    
# ---------------- LOAD ----------------
    loader = DataLoader(Config.DATA_PATH)
    df = loader.get_data()
    original_df = df.copy()

   
# ---------------- EDA (BEFORE CLEANING) ----------------
    eda = Eda(df, Config.BINS)
    general_info = eda.run_general()  
    
    missing_summary = general_info["missing"]
    duplicate_count = general_info["duplicates"]
    constant_cols = eda.constant_data()
    
 # ---------------- CLEANING ----------------
    cleaner = DataCleaner(df)

    cleaner.missing_data_fixed(missing_summary)
    cleaner.duplicated_rows(duplicate_count)
    cleaner.drop_constant_columns(constant_cols)

    df = cleaner.df

 # ---------------- EDA (AFTER CLEANING) ----------------
    eda = Eda(df, Config.BINS)
    eda.run_numerical(Config.TARGET)

 # ---------------- FEATURE ENGINEERING ----------------
    fe = FeatureEngineering(df, Config.TARGET)
    df,log_col = fe.log_transform_target()
    

# ---------------- VISUAL CHECK ----------------
    eda.compare_columns(Config.TARGET, log_col)

# ---------------- DEBUG ----------------
    print("\n===== DEBUG =====")
    print("Before:", original_df.shape)
    print("After:", df.shape)
    print("Dropped columns:", set(original_df.columns) - set(df.columns))
    
if __name__ == "__main__":
    main()