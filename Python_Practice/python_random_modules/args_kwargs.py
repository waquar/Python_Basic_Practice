# def function_name_print(a,b,c,d):
#     print(a,b,c,d)

def funargs(normal , *args):
    #print(args[0])
    print(normal)
    print('using args below:---------')
    for items in args:
        print(items)

def funkwargs( *args, **kwargs):
    print("\nusings kwargs below:--------")
    for key, value  in kwargs.items():
        print(f"{key} is a  {value}")

#function_name_print(12,13,14,15,16)

normal = 'waquar'
namelist = ['har','rav','krish','roy']
namedictionary = {'waquar': 'code learner', 'shadab': 'pro coder', 'vicky': 'awesome writer', 'shariq': 'rapgod'}


funargs(*namelist)
funkwargs(*namelist, **namedictionary)

