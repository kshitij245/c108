import pandas as pd
import csv
import plotly.graph_objects as go

df =pd.read_csv("level.csv")
print(df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(x=df.groupby("level")["attempt"].mean(),
y=["level 1","level2","level 3","level 4" ],
orientation="v"))
fig.show()
