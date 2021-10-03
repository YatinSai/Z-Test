import pandas as pd 
import statistics
import random
import plotly.figure_factory as ff

df = pd.read_csv("school1int.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)

plot = ff.create_distplot([data],['Plot Graph'],show_hist = True)
plot.show()

