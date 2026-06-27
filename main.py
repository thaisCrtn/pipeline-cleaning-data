from src.pipeline import process_data

if __name__ == "__main__":
    print('STARTING THE AUTOMATION ROBOT...\n')

    print("-- PROCESSING CLIENTS --")
    process_data('data/raw_data.csv', 'data/clean_data.csv')

    print('\n-----------------------------------------------')

    print("-- PROCESSING SALES")
    process_data('data/data_sales.csv', 'data/clean_sales.csv')

    # Path th files
    # RAW_FILE = 'data/raw_data.csv'
    # CLEAN_FILE = 'data/clean_data.csv'

    # Run robo
   # process_data(RAW_FILE, CLEAN_FILE)
