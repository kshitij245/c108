import csv
from statistics import median
from typing import Counter

from numpy import append 
with open("height-weight.csv",newline="")as f:
    reader=csv.reader(f)
    file_Data=list(reader)
file_Data.pop(0)
new_data=[]
for i in range(len(file_Data)):
    num=file_Data[i][1]
    new_data.append(float(num))
data=Counter(new_data)
mode_data_range_for={
    "50-60":0,
     "60-70":0,
 "70-80":0,
}
for height,occurence
n=len(new_data)
new_data.sort()
total=0
for o in new_data:
    total+=o
if n%2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]
print(median)
    
