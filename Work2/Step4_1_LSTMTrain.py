import csv
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding, SpatialDropout1D
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report


class LSTMModel:

    def __init__(self):
        self.data = "EmotionMark.csv"
        self.data2 = "DevicedData.csv"
        self.dataList = []

    def readFile(self):
        self.df = pd.read_csv(self.data2 , encoding="utf-8")
        for index, row in self.df.iterrows():
            self.dataList.append(list(row))
        self.preProcess()

    def preProcess(self):
        self.maxNBWords = 10000
        self.maxSeqLen = 250
        self.embDim = 100
        tokenizer = Tokenizer(num_words=self.maxNBWords , filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' , lower=True)
        tokenizer.fit_on_texts(self.dataList)
        wordIndex = tokenizer.word_index
        self.x = tokenizer.texts_to_sequences(self.dataList)
        self.x = pad_sequences(self.x , maxlen=self.maxSeqLen)
        self.y = pd.get_dummies(self.df).values
        self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(self.x, self.y, test_size=0.7, random_state=60)

    def defination(self):
        self.model = Sequential()
        self.model.add(Embedding(self.maxNBWords , self.embDim , input_length=self.x.shape[1]))
        self.model.add(SpatialDropout1D(0.2))
        self.model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
        self.model.add(Dense(10 , activation="softmax"))
        self.model.compile(loss='categorical_crossentropy' , optimizer='adam', metrics=['accuracy'])
        print(self.model.summary())

    def training(self):
        try:
            history = self.model.fit(self.Xtrain, self.Ytrain, epochs=5, batch_size=128)
            plt.title('Loss')
            plt.plot(history.history['loss'], label='train')
            plt.plot(history.history['val_loss'], label='test')
            plt.legend()
            plt.show()
            # 在使用训练集训练的过程中，其在验证集和训练集上的准确率的变化曲线
            plt.title('Accuracy')
            # plt.plot(history.history['acc'], label='train')
            plt.plot(history.history['accuracy'], label='train')
            # plt.plot(history.history['val_acc'], label='test')
            plt.plot(history.history['val_accuracy'], label='test')
            plt.legend()
            plt.show()
        except:
            pass
        self.evaluation()

    def evaluation(self):
        self.Ypred = self.model.predict(self.Xtest)
        self.Ypred = self.Ypred.argmax(axis=1)
        self.Ytest = self.Ytest.argmax(axis=1)
        print('accuracy %s' % accuracy_score(self.Ypred, self.Ytest))
        self.target_names = self.df.values
        # print(classification_report(self.Ytest, self.Ypred, target_names=self.target_names))
        # (3)根据预测标签值和实际标签值构建其混淆矩阵，模型的混淆矩阵中的对角线表示标签预测正确的数量。
        conf_mat = confusion_matrix(self.Ytest, self.Ypred)
        fig, ax = plt.subplots(figsize=(10, 8))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        plt.rcParams['axes.unicode_minus'] = False
        sns.heatmap(conf_mat, annot=True, fmt='d', xticklabels=self.df.type.values,
                    yticklabels=self.df.type.values)
        plt.ylabel('实际结果', fontsize=18)
        plt.xlabel('预测结果', fontsize=18)
        plt.show()


    def start(self):
        self.readFile()
        self.defination()
        self.training()




if __name__ == '__main__':
    L = LSTMModel()
    L.start()