import csv
from sklearn.feature_extraction.text import TfidfVectorizer


class Extract:

    def __init__(self):
        self.dataFile = "tag.csv"

    def extractMatrix(self):
        vector = TfidfVectorizer()
        with open(self.dataFile , "r" , newline= "" , encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    corpus = []
                    corpus.append(row[1])
                    X = vector.fit_transform(corpus)
                    featureName = vector.get_feature_names_out()
                    for docIdx, doc in enumerate(X.toarray()):
                        for featureIdx, featureValue in enumerate(doc):
                            print(f"{featureName[featureIdx]}: {featureValue}")
                except:
                    pass



if __name__ == '__main__':
    E = Extract()
    E.extractMatrix()
