import plotly.figure_factory as ff
import random
import pandas as pd

 
df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

fig = ff.create_distplot([data], ['HeightPlot'], show_hist = True)

fig.show()
