import pandas as pd 
import statistics
import random
import plotly.figure_factory as ff

df = pd.read_csv("bi.csv")
data = df["Math_score"].tolist()


def sample_100_average():
    samples_100 = []
    for i in range(0,100):
        rand = random.randint(0,len(data)-1)
        value = data[rand]
        samples_100.append(value)
    average = statistics.mean(samples_100)
    return average



all_average = []
for e in range(0,100):
    mean = sample_100_average()
    all_average.append(mean)
average = statistics.mean(all_average)
sd = statistics.stdev(all_average)
print(sd)
print(average)

dist = ff.create_distplot([data],['Graph'], show_hist= True)

dist.show()

    




