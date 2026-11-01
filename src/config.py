import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]

load_dotenv(PROJECT_ROOT / ".env")



GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
KAGGLE_API_TOKEN = os.getenv("KAGGLE_API_TOKEN")
KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_DATASET = "ashoknayar/loan-approval-records-10000"

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"