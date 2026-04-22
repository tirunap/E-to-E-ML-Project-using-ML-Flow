import joblib
import pandas as pd
import numpy as np
from pathlib import Path 


class PredictionPipeline:
    def __init__(self, model_path: Path):
        self.model_path = model_path

    def predict(self, input_data: pd.DataFrame) -> np.ndarray:
        model = joblib.load(self.model_path)
        predictions = model.predict(input_data)
        return predictions