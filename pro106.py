import numpy as np
import plotly_express as px
import csv

def plotFigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="days_present",y="marks_in_percentage")
        fig.show()

def dataSource(data_path):
    marks_in_percentage=[]
    days_present=[]
    with open(data_path) as f:
        dg=csv.DictReader(f)
        for d in dg:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x":marks_in_percentage,"y":days_present}