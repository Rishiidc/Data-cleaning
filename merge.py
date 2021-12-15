import csv
from os import write

dataset1 = []
dataset2 = []

with open("dataset_1.csv","r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        dataset1.append(i)

headers1 = dataset1[0]
planet_data1 = dataset1[1:]

with open("dataset_2.csv","r") as q:
    csvreader = csv.reader(q)
    for i in csvreader:
        dataset2.append(i)

headers2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = headers1+headers2
planet_data = []

for index,d in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
    
with open("mergeddata.csv","a+") as q:
    csvwriter = csv.writer(q)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
    