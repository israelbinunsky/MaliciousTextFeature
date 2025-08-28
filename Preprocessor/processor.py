import re
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')



class Processor:
    def row_cleaner(self):
        text=self.text
        text = re.sub(r"@[A-Za-z0-9_]+", "", self.text)
        text = re.sub(r"http\S+|www\S+", "", text)
        text = " ".join(text.split())
        text = text.replace("#", "").replace("_", " ")
        self.text = text
        return self

    def remove_stopwords(self, stopwords: list):
        words = self.text.split()
        words = [w for w in words if w not in stopwords]
        self.text = " ".join(words)
        return self

    def lowercase(self):
        self.text = self.text.lower()
        return self


    def lemmatize(self):
        lemmatizer = WordNetLemmatizer()
        words = self.text.split()
        words = [lemmatizer.lemmatize(w) for w in words]
        self.text = " ".join(words)
        return self

    def new_param(self, doc):

        self.text = doc["text"]
        processed_text =self.row_cleaner().lowercase().remove_stopwords(["the", "and", "is"]).lemmatize().text
        # print(processed_text)
        doc["processed_text"] = processed_text
        print(doc)
        return doc