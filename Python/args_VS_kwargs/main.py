'''
*args and **kwargs are both optional, and not required as arguments, even though the function head declares them

*args = arguments = unspesified number of arguments. Think of as list or tuple
**kwargs = keyword arguments = unspesified number of key-value pair. Think of this as a dictionary

the *args and **kwargs, are not passed in as list or dictionary,
but as normal arguments. Thus the difference is
*args; arg1, arg2, arg3, ... argN
**kwargs; key1=value1, key2=value2, ... keyN = valueN
'''


def someFunction(required, *args, **kwargs):
    print("Required argument: {}\n".format(required))


    # we can omit the *'s infront of the argument / parameters inside the function because they are now declared in the head as list/tuple and dictionary
    if args:
        print("*args: {}".format(args))
        # now we can access the *args as with normal list/tuples
        print("Accessing *args 2 is {}\n".format(args[1])) # remember [1] is the second element

    if kwargs:
        print("**kwargs: {}".format(kwargs))
        # we can also access the **kwargs as a normal dictionary
        print("Accessing **kwarg: {} is {}\n".format("programming", kwargs['programming']))

'''
Python alows to send functions as arguments,
This means that one can send functions as elements in the  *args or\and **kwargs
'''

def func1():
    print("func1")

def func2():
    print("func2")

def func3():
    print("func3")


def someFunctionCallingOtherFunctionsTroughArgs(*args):
    print("Now calling functions from args")
    for function in args:
        function()

def someFunctionCallingOtherFunctionsTroughKwargs(**kwargs):
    print("Now calling functions from kwargs")
    for key, function in kwargs.items():
        function()

    
if __name__ == "__main__":
    # Simple function demonstrating that *args and **args are optional
    someFunction("Sigve")

    # Example of both *args and **kwargs
    someFunction("Sigve", "has", "hobbies", "such as", music="Playes guitar", programming="prefer python")

    # Example of only *args AND passing functions!
    someFunctionCallingOtherFunctionsTroughArgs(func1, func2)

    # Example of only **kwargs AND passing functions, and even lambda expression!
    someFunctionCallingOtherFunctionsTroughKwargs(f1=func1, f2=func2, f3=func3, f4=lambda: print("func4"))