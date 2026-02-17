from datetime import datetime
import os 
from networksecurity.constant import training_pipline

print(training_pipline.PIPELINE_NAME)
print(training_pipline.ARTIFACT_DIR )

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipline_name = training_pipline.PIPELINE_NAME
        self.artifact_dir = os.path.join(training_pipline.ARTIFACT_DIR,timestamp)
        self.artifact_dir = os.path.join(training_pipline.ARTIFACT_DIR,timestamp)
        self.timestamp: str = timestamp


class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipline.DATA_INGESTION_DIR_NAME
        
        )
        self.feature_store_file_path:str=os.path.join(
            self.data_ingestion_dir,
            training_pipline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipline.FILE_NAME
        )
        self.train_file_path:str=os.path.join(
            self.data_ingestion_dir,
            training_pipline.DATA_INGESTION_INGESTED_DIR,
            training_pipline.TRAIN_DIR_NAME,
            training_pipline.FILE_NAME
        )
        self.test_file_path:str=os.path.join(
            self.data_ingestion_dir,
            training_pipline.DATA_INGESTION_INGESTED_DIR,
            training_pipline.TEST_DIR_NAME,
            training_pipline.FILE_NAME
        )
        self.test_size:float=training_pipline.TEST_SIZE
        self.train_test_split_ratio:float=training_pipline.TRAIN_TEST_SPLIT_RATIO
        self.collection_name:str=training_pipline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str=training_pipline.DATA_INGESTION_DATABASE_NAME
        
