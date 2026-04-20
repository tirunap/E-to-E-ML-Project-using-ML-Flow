import os
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

from mlProject.utils.common import read_yaml, create_directories, save_json
from mlProject.entity.config_entity import TrainingPipelineConfig
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: TrainingPipelineConfig):
        self.config = config


    def eval_metrics(self, actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        r2 = r2_score(actual, predicted)
        mae = mean_absolute_error(actual, predicted)
        return rmse, r2, mae
    
    def evaluate_model(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(self.config.mlflow_uri).scheme

        with mlflow.start_run():
            predicted = model.predict(test_x)

            rmse, r2, mae = self.eval_metrics(test_y, predicted)

            score = {"rmse": rmse, "r2": r2, "mae": mae}
            save_json(path=self.config.metric_file_path, data=score)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            mlflow.sklearn.log_model(model, "model")


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                #   Register the model
                #   There are other ways to use the Model Registry, which depends on the use case,
                #   please refer to the doc for more information:
                #   https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestRegressor")
            else:
                mlflow.sklearn.log_model(model, "model")