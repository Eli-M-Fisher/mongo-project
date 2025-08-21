from app.fetcher import MongoFetcher

def main():
    fetcher = MongoFetcher()
    df = fetcher.fetch_all()
    print(df.head()) 

if __name__ == "__main__":
    main()
