import csv
import re
import os
import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from snownlp import SnowNLP
from zhon.hanzi import punctuation


class DataClean:

    def __init__(self):
        self.orgData = "D:\Python项目\文本挖掘\Exam\PRJ01\Work2\Data\common.csv"
        self.orgData2 = "D:\Python项目\文本挖掘\Exam\PRJ01\Work2\Data\FinalData.csv"
        self.orgDataList = []

    def readFile(self):
        with open(self.orgData , "r" , encoding="utf-8") as file1:
            reader = csv.reader(file1)
            for row in reader:
                self.dataClean(row[1])

    def dataClean(self , item):
        dicts = {i: '' for i in string.punctuation}
        dicts2 = {i: '' for i in punctuation}
        puncTable = str.maketrans(dicts)
        puncTable2 = str.maketrans(dicts2)
        newS = item.translate(puncTable)
        newS2 = newS.translate(puncTable2)
        chineseText = re.sub(r"[^\u4e00-\u9fff]+", "", newS2)
        self.orgDataList.append(chineseText)


    def emotionMark(self):
        vector = TfidfVectorizer()
        file2 = open("D:\Python项目\文本挖掘\Exam\PRJ01\Work2\Data\Cache05.csv" , "w" , encoding="utf-8")
        with open(self.orgData2, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            writer = csv.writer(file2)
            for row in reader:
                try:
                    s = SnowNLP(row[0])
                    sentimentScore = s.sentiments
                    sentences = s.sentences
                    for sentence in sentences:
                        s = SnowNLP(sentence)
                        sentimentScore = s.sentiments
                        if sentimentScore > .5:
                            writer.writerow([sentimentScore , sentence , "Positive"])
                        elif sentimentScore < .5:
                            writer.writerow([sentimentScore , sentence , "Negative"])
                        else:
                            writer.writerow([sentimentScore, sentence, "Natural"])
                except:
                    pass
            file2.close()

        with open('D:\Python项目\文本挖掘\Exam\PRJ01\Work2\Data\Cache05.csv', 'r', newline='',
                  encoding="utf-8") as input_file, open('D:\Python项目\文本挖掘\Exam\PRJ01\Work2\Data\EmotionMark.csv', 'w',
                                                        newline='',
                                                        encoding="utf-8") as output_file:
            # 创建 CSV 读取器和写入器
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            # 遍历 CSV 文件的每一行
            for row in reader:
                # 检查行是否为空行
                if any(field.strip() for field in row):
                    # 如果当前行不是空行，则将其写入新的 CSV 文件
                    writer.writerow(row)


    def init(self):
        # self.readFile()
        # self.cutRepeat()
        self.emotionMark()


if __name__ == '__main__':
    D = DataClean()
    D.init()