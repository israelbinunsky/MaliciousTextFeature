from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

class Enricher:

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
        weapons_found = list()
        words = doc["processed_text"].split()
        with open(path, 'r') as f:
            weapons = f.read()
        weapon_list = weapons.split('\n')
        for w in words:
            if w in weapon_list:
                weapons_found.append(w)
        doc["weapons_detected"] = weapons_found

    def find_time(self, doc):
        found = re.findall(r"\d{4}-\d{2}-\d{2}", doc["processed_text"])
        latest = max(found)
        doc["relevant_timestamp"] = latest

    def make_enriche(self, doc):
        self.sentiment(doc)
        self.check_weapon(doc, 'weapon_list.txt')
        self.find_time(doc)


