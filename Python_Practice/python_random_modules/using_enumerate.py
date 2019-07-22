list1 = ['apple' , 'grapes', 'banana', 'muskmelon' , 'watermelon']
list2 = ('apple' , 'grapes', 'banana', 'muskmelon' , 'watermelon')
list3 = {'waquar': 'code learner', 'shadab': 'pro coder', 'vicky': 'awesome writer', 'shariq': 'rapgod'}
# i = 1
# for items in list1:
#     if i%2 is not  0:
#         print(items)
#     i+= 1

for index, item in enumerate(list3):
    if index%2 == 1:
        print(item)

#enumerate returns index and item both of given list,tuple,dictionary
