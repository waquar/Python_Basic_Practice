def nameprinter(fname, lname):
    return  fname +' '+ lname

def sumtotal(a,b,c):
    return a+b+c+13

print(__name__)
if __name__ == '__main__':
    name = nameprinter('waquar', 'alam')
    print(name)
    sumnum = sumtotal(54,5,78)
    print(sumnum)