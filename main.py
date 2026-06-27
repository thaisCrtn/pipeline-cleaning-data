from src.pipeline import process_data

if __name__ == "__main__":
    # Path th files
    RAW_FILE = 'data/raw_data.csv'
    CLEAN_FILE = 'data/clean_data.csv'

    # Run robo
    process_data(RAW_FILE, CLEAN_FILE)
