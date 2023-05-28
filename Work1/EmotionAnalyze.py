import pickle
from sklearn.naive_bayes import MultinomialNB

# 假设您已经训练好了一个朴素贝叶斯模型
model = MultinomialNB()

# 假设您有一些训练好的特征和标签数据
features = [[0,1], [1, 1]]
labels = [0, 1]

# 使用训练数据拟合模型
model.fit(features, labels)

# 打包并保存模型到文件
with open('naive_bayes_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# 加载模型
with open('naive_bayes_model.pkl', 'rb') as file:
    model = pickle.load(file)

# 使用模型进行预测
prediction = model.predict([[2, 2]])
print(prediction)