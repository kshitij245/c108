import csv 
import pandas as pd
import plotly.figure_factory as ff

df =pd.read_csv("height-weight.csv")
fig =ff.create_distplot([df["Weight(Pounds)"].tolist()],["height"],show_hist=False)
fig.show()