import plotly.figure_factory as ff
import random
import pandas as pd

 
df = pd.read_csv("project.csv")
data = df["Avg Rating"].tolist()

fig = ff.create_distplot([data], ['AvgRatingPlot'], show_hist = True)

fig.show()