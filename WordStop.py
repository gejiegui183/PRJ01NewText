import csv
import jieba

class WordStop:

    def __init__(self):
        self.dict = "cn_stopwords.txt"
        self.dataFile = "processed.csv"
        self.resultFile = "deviced.csv"
        self.stopList = []


    def readDict(self):
        with open(self.dict, 'r', encoding='utf-8') as f:  #
            self.stopList = [word.strip('\n') for word in f.readlines()]
        self.remove()

    def remove(self):
        file = open(self.resultFile , "w" , encoding="gbk")
        writer = csv.writer(file)
        with open(self.dataFile , "r" ,newline="" , encoding="gbk") as file:
            reader = csv.reader(file)
            for row in reader:
                words = jieba.lcut(row[0])
                filteredWord = [word for word in words if words not in self.stopList]
                writer.writerow([" ".join(filteredWord)])

    def start(self):
        self.readDict()


if __name__ == '__main__':
    W = WordStop()
    W.start()