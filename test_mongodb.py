from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

username = "harsha_db"
password = "Harsha@8104"   # your real password

encoded_password = quote_plus(password)

uri = f"mongodb+srv://{username}:{encoded_password}@cluster0.vfgvxx3.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
