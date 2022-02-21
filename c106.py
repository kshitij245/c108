import numpy as np
import plotly.express as px
import csv

def getDataSource(data_path):
    sizeOfTv=[]
    averageTimeSpent=[]

    with open("size.csv") as csv_file:
        df=csv.DictReader(csv_file)
        for i in df:
           sizeOfTv.append(float(row["Size of TV"]))
           averageTimeSpent.append(float(row("Size of TV")))
 
