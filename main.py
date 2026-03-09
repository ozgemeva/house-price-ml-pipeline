from src.data_loader import DataLoader
from src.feature_engineering import FeatureEngineering 
from src.config import Config
from src.eda import EDA
from src.data_cleaner import DATACLEANER

def main():
    # Full dataset exploration (optional)
    RUN_FULL_EDA = Config.RUN_FULL_EDA
    
    # Load data
    loader = DataLoader(Config.DATA_PATH)
    df = loader.get_data()

    # Initialize EDA
    eda = EDA(df, Config.BINS)
    
    if RUN_FULL_EDA:
         print("\n===== DATASET OVERVIEW =====")
         eda.dataset_overview()
   
    # Check original skew 
    eda.target_overview(Config.TARGET)
      
    # Feature Engineering
    fe = FeatureEngineering(df, Config.TARGET)
    log_col = fe.log_transform_target()

    # Compare distributions
    eda.compare_columns(Config.TARGET, log_col)
    
    # Initialize Clean Data
    dc = DATACLEANER(df)
    dc.data_clean()
    
if __name__ == "__main__":
    main()