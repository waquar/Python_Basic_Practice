def factorial_iteration(num):

    fac = 1
    for i in range(num):
        fac = fac * (i + 1)
    return  fac

def factorial_recursion(num):
    if num == 1:
        return 1
    else:
            rec = num * factorial_recursion(num -1)
            return  rec


def fibonacci_num(num):
    if num == 1:
        return 0
    if num == 2:
        return  1
    else:
        return  fibonacci_num(num-1) + fibonacci_num(num-2)

print("enter number")
num = int(input())
print(factorial_iteration(num))
c = factorial_recursion(num)
print(c)

print(fibonacci_num(num))


