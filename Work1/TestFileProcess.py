import csv
import string
import re
import pandas as pd

from zhon.hanzi import punctuation


class TestFileProcess:
    def __init__(self):
        self.data = "common6.csv"
        self.text = []
        self.cleanData = []

    def readFile(self):
        with open(self.data , "r" , encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                self.text.append(row[1])

    def dataClean(self):
        file = open("TestDataProcess1.csv" , "w" , encoding="utf-8")
        writer = csv.writer(file)
        for item in self.text:
            dicts = {i: '' for i in string.punctuation}
            dicts2 = {i: '' for i in punctuation}
            puncTable = str.maketrans(dicts)
            puncTable2 = str.maketrans(dicts2)
            newS = item.translate(puncTable)
            newS2 = newS.translate(puncTable2)
            chineseText = re.sub(r"[^\u4e00-\u9fff]+", "", newS2)
            writer.writerow([chineseText])


    def deleteSpace(self):
        with open('tag2.csv', 'r', newline='', encoding="utf-8") as input_file, open('tag3.csv', 'w', newline='',
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

    def strip(self):
        data = pd.read_csv("TestDataProcess2.csv", encoding="utf-8")
        data = data.drop_duplicates()
        data.to_csv("TestDataProcess3.csv", index=False)


    def start(self):
        # self.readFile()
        # self.dataClean()
        self.deleteSpace()

if __name__ == '__main__':
    T = TestFileProcess()
    T.start()