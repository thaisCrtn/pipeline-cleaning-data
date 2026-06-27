import pandas as pd
import os
from deep_translator import GoogleTranslator


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

    # ==========================================================
    # 1. GENERAL TREATMENTS - Using for any base
    # ==========================================================
    lines_before = len(df)
    df = df.drop_duplicates()
    print(f".   - Removed {lines_before - len(df)} duplicates lines")

    # Remove extra whitespace from the beginning/end of text on the lines
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()

    # Standardize text (lowercase columns, no extra spaces at the ends)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Dictionary for specific corrections (avoiding translation bugs)
    corrections = {
        'preco': 'price',
        'quantidade': 'amount',
        'nome': 'name',
        'idade': 'age'
    }

    # Standardize the names
    print('Translating columns...')
    df.columns = [
        corrections[col] if col in corrections else
        GoogleTranslator(source='auto', target='en').translate(col) for col in df.columns
    ]
    # ========================================================================
    # 2. SPECIFIC TREATMENTS - Only run if the columns exists
    # =======================================================================

    # if base for clients/RH and have age:
    if 'age' in df.columns:
        df['age'] = pd.to_numeric(df['age'], errors='coerce')
        df['age'] = df['age'].fillna(df['age'].median())
        print(".  - Columns 'age' treated with median")

    # if base for sales/e-commerce and have price and amount:
    if 'price' in df.columns and 'amount' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df['total_revenue'] = df['price'] * df['amount']
        print(".  - Columns 'total_revenue' calculate automatically.")

    # if base there are any columns of DATA:
    if 'data_sale' in df.columns:
        df['time_sale'] = pd.to_datetime(df['time_sale'], errors='coerce')
        print(".  - Columns 'time_sale' converted for to format correct. ")

    # ===============================================================
    # 3. FINAL TREATMENT OF RESIDUAL NULLS
    # ===============================================================

    # Any remaining empty space in text columns becomes "not provided."
    df = df.fillna('Not provided')

    # Save Step
    print(f"Salving cleaning data in: {exit_path}")
    df.to_csv(exit_path, index=False)
    print('Pipeline executed successfully!')
