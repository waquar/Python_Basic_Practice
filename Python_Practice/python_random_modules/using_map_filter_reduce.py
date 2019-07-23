#--------------------------------------------------Map_______________
# list1 = ['12','14', '16','18','20','22', '24']
# # taking integers as strings
#
# a = list(map(int, list1))
# print(a[0] + 20)
#--------------------------------------------------##-------------------
#using map we typecasted all the strings to list
# always use list before map because it returns list for taking it in variable

def square(a):
    return a*a
def cube(a):
    return  a*a*a

func = [square, cube]                                                  #func is a list of functions
for i in range(10):
    val = list(map(lambda  x:x(i) , func))
    print(val)


#----------------------------------------FILTER-----------------------------

list1 = [12,47,80,9,8,9,32,65,378,65,43,2,2]

def isgreaterthen_10(num):
    return  num>10

greater_10 = list(filter(isgreaterthen_10, list1))
print(greater_10)
 # also for filter  we have to use list if we want to take the value in variable

 #----------------------------------------Reduce------------------------------------
