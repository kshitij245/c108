import pandas as pd
import statistics

df =pd.read_csv("StudentsPerformance.csv")
dataset = [df]
dataset.pop(0)

mean =statistics.mean(dataset)
median=statistics.median(dataset)
mode=statistics.mode(dataset)
