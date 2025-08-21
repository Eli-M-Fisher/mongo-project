import os
from pymongo import MongoClient
import pandas as pd


class MongoFetcher:
    """
    responsible for connecting to MongoDB and fetching raw text data.
    """

    def __init__(self):
        connection_string = os.getenv("MONGO_URI")

        if not connection_string:
            raise ValueError("Missing MONGO_URI environment variable")

        self.client = MongoClient(connection_string)
        self.db = self.client["IranMalDB"]   # DB name מהמטלה
        self.collection = self.db["tweets"]  # שם האוסף (נשאר אותו דבר)

    def fetch_all(self) -> pd.DataFrame:
        """
        fetch all records from the MongoDB collection and return as DataFrame
        """
        data = list(self.collection.find({}))
        if not data:
            return pd.DataFrame()

        df = pd.DataFrame(data)

        df = df.rename(columns={
            "_id": "id",
            "Text": "original_text"
        })

        return df[["id", "original_text"]]
