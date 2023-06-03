import csv
import pickle

import numpy as np
import pandas as pd


class Predict:
    def __init__(self):
        self.data = "TestDataProcess3.csv"
        self.model = "model.pkl"
        self.dataCache = []

    def dataLoding(self):
        with open(self.data , "r" , encoding="utf-8") as file1:
            reader = csv.reader(file1)
            for row in reader:
                self.dataCache.append(row[0])
        self.modelLoding()

    def modelLoding(self):
        with open("modelSVC.pkl", "rb") as file2:
            model = pickle.load(file2)
        # for item in self.dataCache:
        #     X = np.array([[item]])
        #     # print(type(item))
        #     predictions = model.predict()
        data = pd.read_csv('EmotionMark.csv', sep=',', header=None)[0][:4167]
        # print(data)
        # print(type(item))
        predictions = model.predict([data])
        print(predictions)

if __name__ == '__main__':
    P = Predict()
    P.dataLoding()
