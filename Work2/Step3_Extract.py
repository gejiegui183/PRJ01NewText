import csv
from sklearn.feature_extraction.text import TfidfVectorizer , CountVectorizer
from snownlp import SnowNLP


class Extract:

    def __init__(self):
        self.data = "DevicedData.csv"

    def fratureTag(self):
        vector = TfidfVectorizer()
        with open(self.data, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    corpus = row
                    X = vector.fit_transform(corpus)
                    featureName = vector.get_feature_names_out()
                    for docIdx, doc in enumerate(X.toarray()):
                        for featureIdx, featureValue in enumerate(doc):
                            print(f"{featureName[featureIdx]}: {featureValue}")
                except:
                    pass

    def matrixCreate(self):
        count_vectorizer = CountVectorizer()

        # 创建TfidfVectorizer对象
        tfidf_vectorizer = TfidfVectorizer()
        # 文本数据
        with open(self.data, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    X_count = count_vectorizer.fit_transform(row)
                    X_tfidf = tfidf_vectorizer.fit_transform(row)
                    print(count_vectorizer.get_feature_names_out())
                    print(X_count.toarray())
                    print(X_tfidf.toarray())
                    print()
                except:
                    pass

if __name__ == '__main__':
    E = Extract()
    # E.fratureTag()
