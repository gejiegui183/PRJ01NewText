import csv

tag = []

with open("tag3.csv", "r" , encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] > '0.5':
            tag.append("Positive")
        elif row[0] < '0.5':
            tag.append("Negative")
        else:
            tag.append("Normal")

with open("tag4.csv", "w" , encoding="utf-8") as f2:
    writer = csv.writer(f2)
    for row2 in tag:
        writer.writerow([row2])


with open('tag4.csv', 'r', newline='', encoding="utf-8") as input_file, open('tag5.csv', 'w', newline='',
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

