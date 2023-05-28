import csv
from snownlp import SnowNLP


class EmotionTag:

    def __init__(self):
        self.dataPath = "TestDataProcess3.csv"
        self.tagFile = "tag2.csv"
        self.newTag = []

    def analysis(self):
        with open(self.dataPath, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    s = SnowNLP(row[0])
                    sentimentScore = s.sentiments
                    sentences = s.sentences
                    for sentence in sentences:
                        s = SnowNLP(sentence)
                        sentimentScore = s.sentiments
                        list = [sentimentScore, sentence]
                except:
                    pass
                self.newTag.append(list)


    def saveTag(self):
        file = open(self.tagFile, "w", encoding="utf-8")
        writer = csv.writer(file, delimiter=",")
        for i in self.newTag:
            writer.writerow([i[0]])

if __name__ == '__main__':
    E = EmotionTag()
    E.analysis()
    E.saveTag()