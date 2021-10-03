import pandas as pd 
import statistics
import random
import plotly.figure_factory as ff

df = pd.read_csv("school3int.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(data)

dist = ff.create_distplot([data],['Graph'], show_hist= True)

dist.show()