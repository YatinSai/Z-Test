import plotly.express as px
import random

count = []
sum = []
number = 1


for n in range(1,100):
    d_1 = random.randint(1,6)
    d_2 = random.randint(1,6)  
    result = d_1 + d_2
    sum.append(result)
    number = number + 1
    count.append(number)

graph = px.bar(x = sum , y = count)

graph.show()

    
  
 