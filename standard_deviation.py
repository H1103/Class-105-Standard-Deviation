import math

# list of elements to calculate mean
import csv
with open('data.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

#getting the mean
# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean



# squaring and getting the values
squared_list= []
for number in data:
    print(data," data")
    print(number)
    a = (int(number)) - (mean(data))
    a= a**2
    squared_list.append(a)

#getting sum
sum =0
for i in squared_list:
    sum =sum + i

#dividing the sum by the total values
result = sum/(len(data)-1)

# getting the deviation by taking square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)
# print("derived using predefined function ",statistics.stdev(data))