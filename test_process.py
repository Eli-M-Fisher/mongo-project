from app.fetcher import MongoFetcher
from app.processor import TextProcessor

def main():
    # שליפה
    fetcher = MongoFetcher()
    df = fetcher.fetch_all()

    # עיבוד
    processor = TextProcessor(df, "data/weapons.txt")
    result = processor.process_all()

    print(result.head())

if __name__ == "__main__":
    main()
