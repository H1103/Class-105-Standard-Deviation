import csv
import plotly.express as px
import pandas as pd 

with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# To remove header from the CSV file
file_data.pop(0)

total_marks = 0
total_entry = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entry
print(f"The mean is {mean : 2f}")
    
df = pd.read_csv("class1.csv")
fig = px.scatter(df, x = "Student Number", y = "Marks")

#We are displaying the line of average in our graph
fig.update_layout(shapes = [dict(type = 'line', y0 = mean, y1 = mean, x0 = 0, x1 = total_entry)])
fig.update_yaxes(rangemode = "tozero")
fig.show()

