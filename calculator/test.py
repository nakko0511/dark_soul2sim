import csv
with open("dark_souls2/wepon_set.csv", encoding='utf-8') as csvfile:
    data = csvfile.read()
    print(data)
    print("-------------")
    print(type(data))