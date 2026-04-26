from src.environment_setup import check_environment
from src.load_preview_dataset import load_and_preview_dataset
from src.data_analysis import analyze_data

if __name__ == "__main__":
    check_environment()
    load_and_preview_dataset()
    analyze_data()