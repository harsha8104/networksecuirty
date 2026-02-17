import pandas as pd 
import numpy as np 
import os
import sys


# Pipeline configuration
PIPELINE_NAME = "network_security"
ARTIFACT_DIR = "artifact"

# Data ingestion configuration
DATA_INGESTION_COLLECTION_NAME = "NetworkData"
DATA_INGESTION_DATABASE_NAME = "NetworkSecurity"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

# File and directory names
FILE_NAME = "network_data.csv"
TRAIN_DIR_NAME = "train"
TEST_DIR_NAME = "test"

# Train/test split configuration
TEST_SIZE = 0.2
TRAIN_TEST_SPLIT_RATIO = 0.2
