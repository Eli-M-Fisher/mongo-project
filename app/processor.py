import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class TextProcessor:
    """
    process texts: rarest word, sentiment analysis, weapons detection.
    """

    def __init__(self, df: pd.DataFrame, weapons_file: str = "data/weapons.txt"):
        self.df = df.copy()

        # sentiment analyzer
        nltk.data.path.append("/usr/local/share/nltk_data")
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

        # load weapons list
        with open(weapons_file, "r") as f:
            self.weapons_list = [w.strip().lower() for w in f.readlines() if w.strip()]

    def add_rarest_word(self):
        """
        find the rarest word in each text (by length, as a simple heuristic).
        """
        rarest_words = []
        for text in self.df["original_text"]:
            words = text.split()
            if not words:
                rarest_words.append("")
                continue
            rarest = min(words, key=lambda w: words.count(w))
            rarest_words.append(rarest)
        self.df["rarest_word"] = rarest_words

    def add_sentiment(self):
        """
        Add sentiment classification: positive / neutral / negative
        """
        sentiments = []
        for text in self.df["original_text"]:
            score = self.sentiment_analyzer.polarity_scores(text)["compound"]
            if score >= 0.5:
                sentiments.append("positive")
            elif score <= -0.5:
                sentiments.append("negative")
            else:
                sentiments.append("neutral")
        self.df["sentiment"] = sentiments

    def add_weapons_detected(self):
        """
        Check if any weapon from blacklist appears in text
        """
        detected = []
        for text in self.df["original_text"].str.lower():
            found = ""
            for weapon in self.weapons_list:
                if weapon in text:
                    found = weapon
                    break
            detected.append(found)
        self.df["weapons_detected"] = detected

    def process_all(self) -> pd.DataFrame:
        """
        Run all processing steps and return enriched DataFrame
        """
        self.add_rarest_word()
        self.add_sentiment()
        self.add_weapons_detected()
        return self.df