from src.data_loader import DataLoader
from src.feature_engineering import FeatureEngineering as fen
from src.config import Config
from src.eda  import EDA

def main():
    loader = DataLoader(Config.DATA_PATH)
    df = loader.get_data() 
  
# EDA
    eda = EDA(df, Config.TARGET,Config.BINS)
    eda.target_analysis()
    eda.check_skew()
    eda.histogram(Config.TARGET) 
     
# Feature Engineering
    fe = fen(df, Config.TARGET)
    df = fe.log_transform_target() 
    
# Analisis after Transform
    eda = EDA(df, f"{Config.TARGET}_log",Config.BINS)
    eda.check_skew()
    eda.histogram(f"{Config.TARGET}_log")
    
if __name__ == "__main__":
    main()
    
   