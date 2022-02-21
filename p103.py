import pandas as pd
import plotly.express as px

df=pd.read_csv("family .csv")
fig=px.scatter(df,x="subjectName",y="timeGiven",size="timegivingdate")
fig.show()