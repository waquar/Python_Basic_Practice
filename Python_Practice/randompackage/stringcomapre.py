def stringcompare(*args, name = 'krish'):
    for items in args:
        if items == name:
            print('this item matched', items)
        else:
            pass

names = ['hari', 'ravi', 'krish', 'roy']
stringcompare(*names)
