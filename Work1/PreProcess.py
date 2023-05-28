import re
import string
from zhon.hanzi import punctuation
import csv
from snownlp import SnowNLP
import pandas as pd

class PreProcess:
    def __init__(self):
        self.txtPath = "common.csv"
        self.newFile = "newProcessed.csv"
        self.newFile2 = "processed2.csv"
        self.tagFile = "tag.csv"
        self.devicedFile = "deviced.csv"
        self.wordList = []
        self.tag = []
        self.newTag = []


    def readFile(self):
        with open(self.newFile , "r" , newline="" , encoding="gbk") as file:
            reader = csv.reader(file)
            for row in reader:
                self.txtCleaning(row[1])


    def txtCleaning(self , item):
        dicts = {i: '' for i in string.punctuation}
        dicts2 = {i:'' for i in punctuation}
        puncTable = str.maketrans(dicts)
        puncTable2 = str.maketrans(dicts2)
        newS = item.translate(puncTable)
        newS2 = newS.translate(puncTable2)
        chineseText = re.sub(r"[^\u4e00-\u9fff]+", "", newS2)
        self.wordList.append(chineseText)


    def cacheWriteIn(self):
        with open(self.newFile2 , "w" , newline="" , encoding="gbk") as file2:
            witer = csv.writer(file2)
            for i in self.wordList:
                witer.writerow([i])

    def analysis(self):
        with open(self.newFile , "r" , newline="" , encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    s = SnowNLP(row[0])
                    sentimentScore = s.sentiments
                    sentences = s.sentences
                    for sentence in sentences:
                        s = SnowNLP(sentence)
                        sentimentScore = s.sentiments
                        list = [sentimentScore , sentence]
                except:
                    pass
                self.newTag.append(list)


    def saveTag(self):
        file = open(self.tagFile , "w" , encoding="utf-8")
        writer = csv.writer(file, delimiter=",")
        for i in self.newTag:
            writer.writerow([i[0], i[1]])


    def starter(self):
        # pass
        # self.readFile()
        # self.cacheWriteIn()
        self.analysis()
        self.saveTag()
        # self.test()




if __name__ == '__main__':
    process = PreProcess()
    process.starter()

# C:\Users\86186\AppData\Local\Temp\jieba.cache
# - 'C:\\Users\\86186/nltk_data'
#  - 'C:\\Users\\86186\\AppData\\Roaming\\nltk_data
# C:\Users\86186\AppData\Local\Temp\jieba.cache