def testreturns(num):
    for items in int(num):
        yield items*3

for value in testreturns(2):
    print(value)