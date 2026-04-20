import os
from mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib
import pandas as pd
from mlProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop(columns=[self.config.target_column])
        test_x = test_data.drop(columns=[self.config.target_column])
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        score = lr.score(test_x, test_y)
        logger.info(f"Model training completed. Test R² score: {score}")

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))