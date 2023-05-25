import csv

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

class Extract:

    def __init__(self):
        self.dataFile = "output.csv"

    def Test(self):
        with open(self.dataFile , "r" , newline= "" , encoding="gbk") as f:
            reader = csv.reader(f)
            for row in reader:
                # print(row[0])
                corpus = row[0]

                # 使用CountVectorizer实例化词袋模型
                vectorizer = CountVectorizer()

                # 使用TfidfVectorizer实例化TF-IDF模型
                # vectorizer = TfidfVectorizer()

                # 对文本进行特征提取
                features = vectorizer.fit_transform(corpus)

                # 特征矩阵
                print(features.toarray())

                # 特征词汇
                print(vectorizer.get_feature_names_out())



if __name__ == '__main__':
    E = Extract()
    E.Test()
