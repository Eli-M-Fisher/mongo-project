from app.fetcher import MongoFetcher
from app.processor import TextProcessor


class DataManager:
    """
    orchestrates fetching and processing of data.
    """

    def __init__(self, weapons_file: str = "data/weapons.txt"):
        self.weapons_file = weapons_file

    def get_processed_data(self):
        # fetch
        fetcher = MongoFetcher()
        df = fetcher.fetch_all()

        df["id"] = df["id"].astype(str)

        # processor
        processor = TextProcessor(df, self.weapons_file)
        processed_df = processor.process_all()

        return processed_df.to_dict(orient="records")
