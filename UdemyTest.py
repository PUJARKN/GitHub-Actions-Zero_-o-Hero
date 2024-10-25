def myfunc(*args):
    return sum(args)* 0.5

print(myfunc(21,35,35,5,45,23,2,3,4))


def myfunc(*args):
    return [num for num in args if num % 2 == 0]
#myfunc(23,24,3412,122,2,1,9)


