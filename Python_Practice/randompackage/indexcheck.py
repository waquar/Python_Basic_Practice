def indexcheck(num):
  for items in num[num.index(5) : num.index(8)+1]:
    return items
a = indexcheck([2,4,6,7,8,9,0,5,6,7,8,9,7,0,0,7,4,5,6])
print(a)