import os
import sys
from dotenv import load_dotenv
import certifi
import pandas as pd
import pymongo

# Load .env variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in python script name [{self.file_name}] line number [{self.line_no}] error message [{self.error_message}]"


class NetworkDataExtract:

    def __init__(self):
        if MONGO_DB_URL is None:
            raise Exception("MONGO_DB_URL not found in .env file")

    def csv_to_json_converter(self, file_path: str):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict(orient="records")
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database: str, collection: str):
        try:
            mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = mongo_client[database]
            coll = db[collection]

            result = coll.insert_many(records)

            mongo_client.close()

            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    FILE_PATH = r"Network_Data\phishingdataset.csv"
    DATABASE = "NetworkSecurity"
    COLLECTION = "NetworkData"

    try:
        network_obj = NetworkDataExtract()

        records = network_obj.csv_to_json_converter(FILE_PATH)
        print(f"First 5 records:\n{records[:5]}")

        no_of_records = network_obj.insert_data_mongodb(
            records=records,
            database=DATABASE,
            collection=COLLECTION
        )

        print(f"Number of records inserted: {no_of_records}")

    except Exception as e:
        print(e)
