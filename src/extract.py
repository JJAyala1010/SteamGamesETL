import kaggle
from .config import RAW_DATA_DIR, KAGGLE_DATASET


def extract_dataset():
    dataset = KAGGLE_DATASET

    # Save files relative to the project root
    output_dir = RAW_DATA_DIR


    kaggle.api.authenticate()

    kaggle.api.dataset_download_files(
        dataset,
        path=str(output_dir),
        unzip=True
    )

    print(f"Dataset downloaded to {output_dir}")


