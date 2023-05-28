import csv

emoList = []
with open("tag.csv", "r" , newline="" , encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] > '0.5':
            emoList.append("Positive")
        elif row[0] < '0.5':
            emoList.append("Negative")
        else:
            emoList.append("Normal")

with open("newTag.csv" , "w" , encoding="utf-8") as newFile:
    writer = csv.writer(newFile)
    for r in emoList:
        writer.writerow([r])