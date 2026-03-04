from src.data_loader import DataLoader
from src.feature_engineering import FeatureEngineering as fen
from src.config import Config
from src.eda import EDA

def main():
    # Load data
    loader = DataLoader(Config.DATA_PATH)
    df = loader.get_data()

    # Initialize EDA
    eda = EDA(df, Config.BINS)

    # Check original skew
    eda.check_skew(Config.TARGET)

    # Feature Engineering
    fe = fen(df, Config.TARGET)
    log_col = fe.log_transform_target()

    # Check skew after transformation
    eda.check_skew(log_col)

    # Compare distributions
    eda.compare_columns(Config.TARGET, log_col)

if __name__ == "__main__":
    main()