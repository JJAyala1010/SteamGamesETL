import polars as pl
from .config import RAW_DATA_DIR, PROCESSED_DATA_DIR

def transform():
    df = pl.scan_csv(RAW_DATA_DIR / "loan_approval_dataset/loan_approval_records.csv")
    df.sink_parquet(PROCESSED_DATA_DIR / 'loan_approval_records.parquet')

    print("Transformed dataset saved to processed folder")
