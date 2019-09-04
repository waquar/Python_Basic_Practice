
# Iterable - __iter__() or __getitem__()
# Iterator - __next__()
# Iteration -

class iterAndGen():
    # def geneartorexample(self):
    #     a = 'a string first'
    #     b = 'a string second'
    #     return b
    #     return a
    def geneartorexample(self):
        a = 'a string first'
        b = 'a string second'
        yield a
        yield  b

i = iterAndGen()
c = i.geneartorexample()
print(c.__next__())
print(c.__next__())