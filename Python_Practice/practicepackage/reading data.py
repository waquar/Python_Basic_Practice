a = ['This line should be in last.']

with open('read.txt', 'a') as w:
    w.write(str(a))


a = open('read.txt', 'r')
print(a.readlines())
a.close()