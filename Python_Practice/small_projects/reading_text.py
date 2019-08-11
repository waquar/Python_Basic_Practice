# list1 = []
# file = open('iris.txt', 'r')
# for items in file:
#     list1.append(items)
# for items in list1:
#     print(items)


import  pickle
import  requests

list1 = []
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = requests.get(url)
result = response.text
data = result.splitlines()

file = open('webdata.txt', 'w')
for items in file:
    pickle.dump(file, 'wb')
    file.close()










