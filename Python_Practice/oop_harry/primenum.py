# num = 20
# for i in range(2,num):
#     print('waq')
#     if num%i==0:
#         break
# else:
#     print(num)
#
a = 2
b = 66

for i in range(a,b+1):
    if i> 1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print("this is prime:-", i)
# a = 20
# b = 20
# c = 30
# for i in range(3):
#     print(a)
#     if a!=c:
#         break
# else:
#     print("waquar")