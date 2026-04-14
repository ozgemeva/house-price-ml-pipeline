from src.data_loader import DataLoader
from src.feature_engineering import FeatureEngineering 
from src.config import Config
from src.eda import Eda
from src.data_cleaner import DataCleaner


def print_cleaning_summary(clean_result):
    print("\n===== CLEANING SUMMARY =====")

    filled = clean_result.get("filled", {}) or {}
    dropped = clean_result.get("dropped", {}) or {}
    summary = clean_result.get("summary", {}) or {}
  
    for col, method in filled.items():
        print(f"{col} → {method}")

    for col, method in dropped.items():
        print(f"{col} → {method}")
    
    print("\n===== HIGH MISSING =====")
    for col, percent in summary.get("high_missing", []):
        print(f"Feature name: {col}: percent: %{percent:.2f}")
    
    print("\n===== MEDIUM MISSING =====")
    for col, percent in summary.get("medium_missing", []):
        print(f"Feature name: {col}: percent: %{percent:.2f}")
    
    print("\n===== LOW MISSING =====")
    for col, percent in summary.get("low_missing", []):
        print(f"Feature name: {col}: percent: %{percent:.2f}")
    
    print("\nTotal filled:", len(filled))
    print("Total dropped:", len(dropped))

def debug_pipeline(original_df, df, eda_before, eda_after, log_col):
    print("\n===== DATA SHAPE =====")
    print("Before:", original_df.shape)
    print("After:", df.shape)

    print("\n===== TARGET CHECK =====")
    print("Before skew:", original_df[Config.TARGET].skew())
    print("After skew:", df[log_col].skew())

    print("\n===== SKEW COMPARISON =====")

    skew_before = {
        r["column"]: r["skew"]
        for r in eda_before.run_numerical(Config.TARGET)["skew_results"]
    }

    skew_after = {
        r["column"]: r["skew"]
        for r in eda_after.run_numerical(Config.TARGET)["skew_results"]
    }

    for col in skew_before:
        if col == Config.TARGET:
            print(f"{col} → before: {skew_before[col]:.2f}, after: {df[log_col].skew():.2f}")
        elif col in skew_after:
            print(f"{col} → before: {skew_before[col]:.2f}, after: {skew_after[col]:.2f}")
            
    


def main(DEBUG=Config.DEBUG):

    # LOAD
    loader = DataLoader(Config.DATA_PATH)
    df = loader.get_data()

    original_df = df.copy()

    # EDA BEFORE
    eda_before = Eda(original_df, Config.BINS)

    # CLEANING INPUT
    eda_current = Eda(df, Config.BINS)
    
    data_Overview = eda_current.dataset_overview()
    dataType_info = eda_current.get_columns_by_type()
    missing_summary = eda_current.number_of_missing_data()
    duplicate_info = eda_current.is_duplicated_row()
    constant_cols = eda_current.constant_data()
    

    # CLEANING
    cleaner = DataCleaner(df)
    df, clean_result = cleaner.clean(missing_summary,dataType_info,duplicate_info["count"],constant_cols)
    clean_result["summary"] = missing_summary
    #clean_result["overview"] = data_Overview
    print_cleaning_summary(clean_result)
    

    # FEATURE ENGINEERING
    fe = FeatureEngineering(df, Config.TARGET)
    df, log_col = fe.log_transform_target()

    # EDA AFTER
    eda_after = Eda(df, Config.BINS)

    # DEBUG
    if DEBUG:
        debug_pipeline(original_df, df, eda_before, eda_after, log_col)


if __name__ == "__main__":
    main()