import csv
import pandas as pd 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import random
import statistics 

df= pd.read_csv("School2.csv")
data=df["Math_score"].to_list()

fig=ff.create_distplot([data], ["Math Score"], show_hist=False)
fig.show()

#population mean and std deviation
mean=statistics.mean(data)
std_deviation = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
std_deviation=statistics.stdev(mean_list)

first_std_deviation_start, first_std_deviation_end=mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end=mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end=mean-(3*std_deviation), mean+(3*std_deviation)

print(mean, std_deviation)

#finding the mean of the first data (students who got tab with learning material)

df=pd.read_csv("School_1_Sample.csv")
data=df["Math_score"].tolist()

mean_of_sample1=statistics.mean(data)
print(mean_of_sample1)

fig=ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="Mean of sample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation 2 End"))

fig.show()

#finding the mean of the second data (students who got extra classes)

df=pd.read_csv("School_2_Sample.csv")
data=df["Math_score"].tolist()

mean_of_sample2=statistics.mean(data)
print(mean_of_sample2)

fig=ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="Mean of sample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation 2 End"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation 3 End"))

fig.show()

#finding the mean of the third data (students who got worksheets)

df=pd.read_csv("School_3_Sample.csv")
data=df["Math_score"].tolist()

mean_of_sample3=statistics.mean(data)
print(mean_of_sample3)

fig=ff.create_distplot([mean_list], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="Mean of sample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation 2 End"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="Standard Deviation 3 End"))

fig.show()

z_score1=(mean-mean_of_sample1)/std_deviation
z_score2=(mean-mean_of_sample2)/std_deviation
z_score3=(mean-mean_of_sample3)/std_deviation

print(z_score1, z_score2, z_score3)