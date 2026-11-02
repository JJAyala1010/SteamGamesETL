from src import config, extract, transform, load

if __name__ == "__main__":
    extract.extract_dataset()
    transform.transform()
    load.load()
    