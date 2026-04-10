from src.data_loader import DataLoader
from src.feature_engineering import FeatureEngineering 
from src.config import Config
from src.eda import Eda
from src.data_cleaner import DataCleaner

def main():
    DEBUG = Config.DEBUG
    
# ---------------- LOAD ----------------
    loader = DataLoader(Config.DATA_PATH)
    df = loader.get_data()
    original_df = df.copy()

   
# ---------------- EDA (BEFORE CLEANING) ----------------
    eda = Eda(df, Config.BINS)
    general_info = eda.run_general()  # number_of_missing_data(),is_duplicated_row
    dataType_info = eda.get_columns_by_type()
    
    missing_summary = general_info["missing"] #summary list output
    duplicate_info = general_info["duplicates"] #duplicate_count output
    
 # ---------------- CLEANING ----------------
    constant_cols = eda.constant_data()
    cleaner = DataCleaner(df)
    clean_result=cleaner.missing_data_fixed(missing_summary,dataType_info)
    
    cleaner.duplicated_rows(duplicate_info["count"])
    cleaner.drop_constant_columns(constant_cols)

    df = cleaner.df
    
    # ---------------- CLEANING OUTPUT ----------------
    print("\n===== CLEANING SUMMARY =====") 
    for col, method in clean_result["filled"].items():
        print(f"{col} → {method}")
    
    for col, method in clean_result["dropped"].items():
        print(f"{col} → {method}")
        
        
 # ---------------- EDA (AFTER CLEANING) ----------------
    eda = Eda(df, Config.BINS)


 # ---------------- FEATURE ENGINEERING ----------------
    fe = FeatureEngineering(df, Config.TARGET)
    df,log_col = fe.log_transform_target()
    

# ---------------- VISUAL CHECK ----------------
    eda.compare_columns(Config.TARGET, log_col)

    
    if DEBUG:
        print("\n===== DATA SHAPE =====")
        print("Before:", original_df.shape)
        print("After:", df.shape)

        print("\n===== SKEW COMPARISON =====")

        eda_before = Eda(original_df, Config.BINS)
        eda_after = Eda(df, Config.BINS)

        skew_before = {r["column"]: r["skew"] for r in eda_before.run_numerical(Config.TARGET)["skew_results"]}
        skew_after = {r["column"]: r["skew"] for r in eda_after.run_numerical(Config.TARGET)["skew_results"]}

        for col in skew_before:
            if col in skew_after:
                if abs(skew_before[col]) > 1 or abs(skew_after[col]) > 1:
                    print(f"{col} → before: {skew_before[col]:.2f}, after: {skew_after[col]:.2f}")
    
if __name__ == "__main__":
    main()