from google.cloud import bigquery
from google.api_core.exceptions import NotFound
from config import GCP_PROJECT_ID, PROCESSED_DATA_DIR

dataset_name = "loan_approvals"
table_name = "loan_approval_records"

# Initialize client
client = bigquery.Client(project=GCP_PROJECT_ID)


try:
    client.get_dataset(dataset_name)
except NotFound:
    print(f"Creating dataset {dataset_name}")
    dataset = bigquery.Dataset(f"{GCP_PROJECT_ID}.{dataset_name}")
    dataset.location = "US"
    client.create_dataset(dataset, timeout=30)
else:
    print(f"Dataset {dataset_name} already exists")

table_id = f"{GCP_PROJECT_ID}.{dataset_name}.{table_name}"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)
parquet_path = PROCESSED_DATA_DIR / f"{table_name}.parquet"
with parquet_path.open("rb") as file:
    load_job = client.load_table_from_file(
        file,
        destination=table_id,
        job_config=job_config
    )

load_job.result()

print(f"Successfully loaded data into {table_id}")
