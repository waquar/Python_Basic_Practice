# list1 = []
# list2 = []

def bondnum(num):
    # for items in num:
    #     if str(items)=='0' or str(items)=='7':
    #         list1.append(items)
    #         for items in range(3):
    #             if items[0] == 0:
    #                 if items[1] == 0:
    #                     if items[2] == 7:
    #                         print("enjoy match found")
    #             else:
    #                 list1.clear()               
    #     else:
    #         list2.append(items)
    #         print(items)
    #         print(list1)
    #         print(list2)
    return (0,0,7) in zip(num, num[1:], num[2:])


a = bondnum([2,4,6,7,8,9,0,0,7,4,5,6])
print(a)
