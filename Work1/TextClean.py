import pandas as pd
data = pd.read_csv("processed.csv" , encoding="gbk")
data = data.drop_duplicates()
data.to_csv("newProcessed.csv" , index=False)