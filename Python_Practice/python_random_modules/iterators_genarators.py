my_list = ['a', 'b', 'c', 'd']
gen_obj = (x for x in my_list)
for val in gen_obj:
    print(val)