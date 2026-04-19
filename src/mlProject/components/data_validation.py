import os 
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd 


class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)

            all_schema_columns = list(self.config.all_schema.keys())

            for col in all_columns:
                if col not in all_schema_columns:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Column: {col} is not in the schema")
                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"All columns are present in the schema")   
                    
            return validation_status
        
        except Exception as e:
            raise e