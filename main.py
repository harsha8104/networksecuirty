from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        TrainingPipelineConfig=TrainingPipelineConfig()
        DataIngestionConfig = DataIngestionConfig(TrainingPipelineConfig)
        data_ingestion = DataIngestion(DataIngestionConfig)
        logging.info("Data Ingestion Started")
        DataIngestionartifact =data_ingestion.initiate_data_ingestion()
        print(DataIngestionartifact)
        

    except Exception as e:
        raise NetworkSecurityException(e,sys)