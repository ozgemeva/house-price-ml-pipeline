from src.data_loader import DataLoader
from src.feature_engineering import FeatureEngineering 
from src.config import Config
from src.eda import Eda
from src.data_cleaner import DataCleaner

def main():
    # Full dataset exploration (optional)
    RUN_FULL_EDA = Config.RUN_FULL_EDA
    
    # Load data
    loader = DataLoader(Config.DATA_PATH)
    df = loader.get_data()

    # Initialize EDA
    eda = Eda(df, Config.BINS)
    
    if RUN_FULL_EDA:
         eda.dataset_overview()
      
    # Feature Engineering
    fe = FeatureEngineering(df, Config.TARGET)
    log_col = fe.log_transform_target()

    # Compare distributions
    eda.compare_columns(Config.TARGET,log_col)
   
    # Initialize Clean Data
    dc = DataCleaner(df)
    dc.data_clean()
    
if __name__ == "__main__":
    main()