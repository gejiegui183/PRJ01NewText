import csv
import pickle
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class Analyze:

    def __init__(self):
        self.data = "EmotionMark.csv"
        self.data2 = "DevicedData.csv"
        self.txtList = []
        self.markList = []
        self.testData1 = []
        self.modelBayes = None
        self.modelSVC = None


    def classify(self):
        with open(self.data , "r" , encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                self.markList.append(row[2])
                self.txtList.append(row[1])
        file.close()
        vectorizer = CountVectorizer()
        txt = vectorizer.fit_transform(self.txtList)
        self.xTrain, self.xTest, self.yTrain, self.yTest = train_test_split(txt, self.markList, test_size=.2,random_state=42)
        # self.trainingBayes()
        self.trainingSVC()

    # 朴素贝叶斯
    def trainingBayes(self):
        self.classifier = MultinomialNB()
        self.classifier.fit(self.xTrain , self.yTrain)
        self.modelBayes = self.classifier

        with open("modelBayes.pkl" , "wb") as file:
            pickle.dump(self.modelBayes , file)
        file.close()

        yPredBayes = self.classifier.predict(self.xTest)
        self.evaluation(yPredBayes)

    # 支持向量机
    def trainingSVC(self):
        self.svmModel = SVC(kernel="linear")
        print(self.xTrain , ";" ,  self.yTrain)
        self.svmModel.fit(self.xTrain , self.yTrain)

        # with open("modelSVC.pkl", "wb") as file:
        #     pickle.dump(self.svmModel, file)
        # file.close()

        yPredSVC = self.svmModel.predict(self.xTest)
        # self.evaluation(yPredSVC)

    def evaluation(self , yPred):
        # 模型评估
        accuracy = metrics.accuracy_score(self.yTest, yPred)
        precision = metrics.precision_score(self.yTest, yPred, average='weighted')
        recall = metrics.recall_score(self.yTest, yPred, average='weighted')
        f1_score = metrics.f1_score(self.yTest, yPred, average='weighted')

        print('Accuracy:', accuracy)
        print('Precision:', precision)
        print('Recall:', recall)
        print('F1 Score:', f1_score)


if __name__ == '__main__':
    A = Analyze()
    A.classify()
