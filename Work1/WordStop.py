import csv
import jieba

class WordStop:

    def __init__(self):
        self.dict = "cn_stopwords.txt"
        self.dataFile = "tag.csv"
        self.resultFile = "deviced.csv"

        self.stopList = []
        self.resultList = []

    def readDict(self):
        with open(self.dict, 'r', encoding='utf-8') as f:  #
            self.stopList = [word.strip('\n') for word in f.readlines()]
        self.remove()

    def remove(self):
        colIndex = 0
        newFile = open(self.resultFile , "w")
        with open(self.dataFile , "r") as file:
            reader = csv.reader(file)
            writer = csv.writer(newFile)
            for row in reader:
                words = jieba.lcut(row[1])
                filteredWord = [word for word in words if words not in self.stopList]
                data = [row[0] , " ".join(filteredWord)]
                writer.writerow(data)





    # def start(self):
    #     self.readDict()


if __name__ == '__main__':
    W = WordStop()
    W.remove()