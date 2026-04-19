from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger
import os

STAGE_NAME = "Data Validation Stage"    

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
            logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
        
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f"{'>>'*20} Starting {STAGE_NAME} {'<<'*20}")
        object = DataValidationTrainingPipeline()
        object.main()   
        logger.info(f"{'>>'*20} Completed {STAGE_NAME} {'<<'*20}")
    except Exception as e:
        logger.exception(e)
        raise e