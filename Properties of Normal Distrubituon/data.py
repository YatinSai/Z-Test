import pandas as pd
import statistics

df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()
mean = statistics.mean(data)
std = statistics.stdev(data)

range1_max,range1_min = mean+1*std, mean-1*std
range2_max,range2_min = mean+2*std, mean-2*std
range3_max,range3_min = mean+3*std, mean-3*std
print(range1_min,range1_max)

range1_array = [i for i in data if i > range1_min and i < range1_max]  
range2_array = [j for j in data if j > range2_min and j < range2_max] 
range3_array = [k for k in data if k > range3_min and k < range3_max] 
        

print(len(range1_array),len(range2_array),len(range3_array))

range1_per = (len(range1_array)/(len(data)-1))*100
range2_per = (len(range2_array)/(len(data)-1))*100
range3_per = (len(range3_array)/(len(data)-1))*100

print(range1_per,range2_per,range3_per)