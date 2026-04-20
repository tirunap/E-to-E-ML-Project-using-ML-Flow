import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config):
        self.config = config

    def perform_train_test_split(self):
        try:
            data = pd.read_csv(self.config.data_path)

            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)

            train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info(f"Data transformation completed. Train and test data saved in {self.config.root_dir}")
            logger.info(f"Train data shape: {train_set.shape}")
            logger.info(f"Test data shape: {test_set.shape}")

        except Exception as e:
            raise e 