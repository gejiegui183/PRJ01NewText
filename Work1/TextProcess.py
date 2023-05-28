import csv

# 打开原始的 CSV 文件和新的 CSV 文件
with open('newTag.csv', 'r', newline='' , encoding="utf-8") as input_file, open('NewTag2.csv', 'w', newline='' , encoding="utf-8") as output_file:
    # 创建 CSV 读取器和写入器
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # 遍历 CSV 文件的每一行
    for row in reader:
        # 检查行是否为空行
        if any(field.strip() for field in row):
            # 如果当前行不是空行，则将其写入新的 CSV 文件
            writer.writerow(row)