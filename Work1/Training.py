import csv

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

class Training:
    def __init__(self):
        self.trainSamples = []
        self.trainLables = []
        self.dataSource1 = "tag.csv"
        self.dataSource2 = "NewTag2.csv"
        self.predictFile = "tag5.csv"
        self.predictData = []
        self.testData1 = []

    def training(self):
        with open(self.dataSource1 , "r" , encoding="utf-8") as file1:
            reader = csv.reader(file1)
            for row in reader:
                self.trainSamples.append(row[1])

        with open(self.dataSource2 , "r" , encoding="utf-8") as file2:
            reader2 = csv.reader(file2)
            for row2 in reader2:
                self.trainLables.append(row2[0])

        # 使用CountVectorizer将文本转换为词频向量
        vectorizer = CountVectorizer()
        trainData = vectorizer.fit_transform(self.trainSamples)


        # 创建并训练支持向量机分类器
        classifier = SVC()
        classifier.fit(trainData, self.trainLables)

        # 准备测试样本
        with open("TestDataProcess3.csv", "r" , encoding="utf-8") as file3:
            reader3 = csv.reader(file3)
            for row in reader3:
                self.testData1.append(row[0])


        testSamples = self.testData1
        testData = vectorizer.transform(testSamples)

        # 使用分类器进行预测
        predictions = classifier.predict(testData)

        # 输出预测结果
        for sample, prediction in zip(testSamples, predictions):
            self.predictData.append(prediction)
            print(f"Sample: {sample}\nPrediction: {prediction}\n")

    def evaluation(self):
        with open(self.predictFile , "r" , encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                self.testData1.append(row[0])

        with open(self.dataSource2 , "r" , encoding="utf-8") as file2:
            reader2 = csv.reader(file2)
            index = len(self.testData1)
            i = 0
            for row2 in reader2:
                while i < index:
                    self.predictData.append(row2[0])
                    i += 1

        test_labels = self.testData1
        predictions = self.predictData

        # 计算准确率
        accuracy = accuracy_score(test_labels, predictions)
        print(f"Accuracy: {accuracy}")

        # 计算精确率
        precision = precision_score(test_labels, predictions, average='weighted')
        print(f"Precision: {precision}")

        # 计算召回率
        recall = recall_score(test_labels, predictions, average='weighted')
        print(f"Recall: {recall}")

        # 计算F1值
        f1 = f1_score(test_labels, predictions, average='weighted')
        print(f"F1 Score: {f1}")

        # 计算混淆矩阵
        confusion_mat = confusion_matrix(test_labels, predictions)
        print("Confusion Matrix:")
        print(confusion_mat)

        # 生成分类报告
        class_report = classification_report(test_labels, predictions)
        print("Classification Report:")
        print(class_report)



if __name__ == '__main__':
    T = Training()
    T.training()
    # T.evaluation()

