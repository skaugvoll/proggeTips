'''
When creating a function, we can specify parameters.

There are a few different ways of doing so, one is to specify every argument we expect, one is to specify all the keywords we suspect,
one is when we dont know how many arguments we want, so we tell it to be dynamic, and one is when we dont know how many keywords we want, so we tell it to be dynamic.

DYNAMIC ARGUMETNS / KEYWORDS.
*args when we dont know how many arguments we are going to pass to a function.
**kwargs is used when we dont know how many keyword arguments we will pass to a function, or it can be used to pass the values of a dictionary as keyword arguments.
'''


'''
Normal way: specify excatly the ones we want
'''
def exactArguments(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

exactArguments("one","two", "three")


'''
Dynamic way:
'''
def dynamicArguments(*args):
    print(args)
    print("Number of arguments given = " + str(len(args)))

dynamicArguments("one","two", "three")
