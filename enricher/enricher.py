from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime

class enricher:
    def __init__(self):
        self.weapons = list()
        self.dates = list()
    def sentiment(self, doc):
        score = SentimentIntensityAnalyzer().polarity_scores(doc["processed_text"])
        num = score['compound']
        if num < -0.5:
            sen = 'negative'
        elif num < 0.5:
            sen = 'neutral'
        else:
            sen = 'positive'
        doc["sentiment"] = sen

    def check_weapon(self, doc, path):
        words = doc["processed_text"].split()
        with open(path, 'r') as f:
            weapons = f.read()
        weapon_list = weapons.split('\n')
        for w in words:
            if w in weapon_list:
                found = w
                self.weapons.append(found)

    def find_earliest_time(self, doc):
        self.dates.append(datetime.strptime(doc['datetime'], "%Y-%m-%d"))
        self.latest_date = max(self.dates).strftime("%Y-%m-%d")
