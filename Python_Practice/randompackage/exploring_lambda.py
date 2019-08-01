def myfunc(n):
  return lambda ab : ab * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(12))
print(mytripler(12))

#lambda is a anonymous one liner function which do calculation in single line
#at first function called with 2 and returned lambda with no acceptor.
#my doubler caught that return and passed 12 at lambda .
#after that it calculated with expression and printed the value.