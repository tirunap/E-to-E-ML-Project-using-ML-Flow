import os
from types import SimpleNamespace

class ConfigurationManager:
    def __init__(self):
        # Example: define default configs here
        self.data_ingestion_config = SimpleNamespace(
            root_dir=os.path.join("artifacts", "data_ingestion"),
            source_URL="https://github.com/tirunap/ML-DL-Models/raw/refs/heads/main/WineQT%20(1).zip",
            local_data_file=os.path.join("artifacts", "data_ingestion", "WineQT%20(1).zip"),
            unzip_dir=os.path.join("artifacts", "data_ingestion", "data")
        )

    def get_data_ingestion_config(self):
        return self.data_ingestion_config
