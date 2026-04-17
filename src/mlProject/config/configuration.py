import os
print(os.getcwd())

class ConfigurationManager:
    def __init__(self):
        # Example: define default configs here
        self.data_ingestion_config = {
            "download_url": "https://https://github.com/tirunap/ML-DL-Models/raw/refs/heads/main/WineQT%20(1).zip",
            "local_data_file": os.path.join("artifacts", "WineQT%20(1).zip"),
            "unzip_dir": os.path.join("artifacts", "data")
        }

    def get_data_ingestion_config(self):
        return self.data_ingestion_config
