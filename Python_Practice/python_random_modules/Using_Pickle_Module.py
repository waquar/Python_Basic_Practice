import pickle

# pickle used for storing data as a file and can be reused later
#---------------------------------------------------------------------------
# making a pickle file

list1 = ['apple' , 'grapes', 'banana', 'muskmelon' , 'watermelon']
file = 'fruits.pkl'
file_fruit = open(file, 'wb')
pickle.dump(list1, file_fruit)            #used for storing the pickle file
file_fruit.close()

#---------------------------------------------------------------------------
# reading a pickle file

list2 = ['apple' , 'grapes', 'banana', 'muskmelon' , 'watermelon', 'kivi']
file = 'fruits.pkl'
file_fruit = open(file, 'rb')
myfruits = pickle.load(file_fruit)                      #used for loading the pickle file
print(myfruits)
print(type(myfruits))

