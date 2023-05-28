import csv
import os
import jieba


class PreProcess:
    def __init__(self):
        self.fileByStep1 = "FinalData.csv"
        self.processedCasch = "Casch04.csv"
        self.processedFile = "DevicedData.csv"
        self.stopWordList = "cn_stopwords.txt"
        self.readData = []

    def readFile(self):
        with open(self.stopWordList, 'r', encoding='utf-8') as f:  #
            self.stopList = [word.strip('\n') for word in f.readlines()]
        self.wordDevice()


    def wordDevice(self):
        file2 = open(self.processedCasch , "w" , encoding="utf-8")
        with open(self.fileByStep1 , "r" , encoding="utf-8") as file3:
            reader = csv.reader(file3)
            writer = csv.writer(file2)
            for row in reader:
                words = jieba.lcut(row[0])
                filteredWord = [word for word in words if words not in self.stopList]
                data = [" ".join(filteredWord)]
                writer.writerow(data)
        file2.close()


    def strip(self):
        with open(self.processedCasch, 'r', newline='', encoding="utf-8") as input_file, open(self.processedFile, 'w', newline='',
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
        self.readFile()
        self.strip()


if __name__ == '__main__':
    P = PreProcess()
    P.init()

