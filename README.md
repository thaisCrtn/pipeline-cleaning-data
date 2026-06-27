# Automated Data Cleaning Pipeline

A dynamic and automated data engineering pipeline developed using Python and Pandas. This project functions as a "Swiss Army Knife" for data cleaning, capable of processing messy data sources (such as sales reports or legacy system exports), normalizing schemas, translating columns programmatically, and exporting clean, production-ready data.

---

## Intelligent Features

•⁠  Duplication & Whitespace Removal: Automatically identifies and drops duplicate rows while stripping hidden whitespaces (⁠ .strip() ⁠) from the edges of text strings.

•⁠  ⁠Schema Standardization & Column Translation: Converts headers to lowercase, replaces spaces with underscores, and integrates the ⁠ deep_translator ⁠ library to translate column names into English automatically.

•⁠  ⁠Override Dictionary:* Features a manual translation mapping system to lock down critical terms (e.g., preventing words like ⁠ preco ⁠ from being mistranslated into ⁠ why ⁠ by the translation engine).

•⁠  ⁠Dynamic Type Inference (80% Rule): Evaluates string columns and only converts them to numeric types if at least 80% of the values are valid numbers. This prevents text columns (like game titles or platforms) from accidentally being forced into numeric formats.

•⁠  Smart Null (NaN) Value Handling:
    Entire rows are dropped if essential identifier columns (such as ⁠ product ⁠ or ⁠ name ⁠) are missing.
    Generic text attributes with missing values are filled with ⁠ "Not provided" ⁠.
    Financial and critical numeric metrics keep their native ⁠ NaN ⁠ status to prevent artificial distortion of future statistical averages or sums.

---

## Technologies used 

- Python 3.13
- Pandas
- Deep Translator

---

## Next steps to improve
- Add treat outliers.
- Implement logs to record errors.
- Conect the pipeline directly the a database SQL.
- Create unit tests to validate the data.
- Create MissingDetector, ImputationStraterySelector, DataCleanerPipeline

---

## Project Structure

```text
pipeline-cleaning-data/
│
├── data/                  # Data directory (Raw and cleaned assets)
│   ├── raw_data.csv       # Messy test dataset
│   └── clean_data.csv     # Target dataset processed by the pipeline
│
├── src/                   # Modular source code
 
---