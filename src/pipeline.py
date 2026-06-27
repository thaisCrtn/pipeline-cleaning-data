import pandas as pd
import os


def process_data(entrance_path, exit_path):
    """
        Function that reads a raw file, performs cleaning, and saves the result.
    """

    print(f"Reading the file: {entrance_path}")

    # chech if the file exists
    if not os.path.exists(entrance_path):
        print(f"Error: The file {entrance_path} wasn't find.")
        return

    df = pd.read_csv(entrance_path)

    # Cleaning Step
    print('Starting the data cleaning...')

    # 1. Remove duplicates
    lines_before = len(df)
    df = df.drop_duplicates()
    print(f".   - Removed {lines_before - len(df)} duplicates lines")

    # 2. Treating null values
    # Customize based on the database, but the generic example is: "Not provided"
    df = df.fillna("Not provided")

    # 3. Standardize text (lowercase columns, no extra spaces at the ends)
    df.columns = df.columns.str.strip().str.lower()

    # Save Step
    print(f"Salving cleaning data in: {exit_path}")
    df.to_csv(exit_path, index=False)
    print('Pipeline executed successfully!')
