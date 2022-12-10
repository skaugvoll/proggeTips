'''
What are decorators in python?
First we need to know that functions are actually just an "advanced"-object in python
They have a memory address, and thus, since we can pass objects as arguments to other functions,
store them as variables, etc. We can do the same with/for functions.
The only difference is that we do not want to call the function when passing it as a argument.
We want to call the passed argument inside the receiving function.
So we just use the name for function
'''


def prolog():
    def passMeAround():
        print("Here I am")

    def whereAreYou(fnc):
        fnc()
    whereAreYou(passMeAround)  # prints 'Here I am'


'''
a decorator is simpy another way of writing
x = decorator(func) # and the decorator returns a function that does something, and calls the passed in func
'''


def exampleOne():
    def myDecorator(func):
        def wrapper(*args, **kvargs):
            print("Begin")
            r = func(*args, **kvargs)
            print("After")
            return r

        return wrapper

    @myDecorator
    def add(*args):
        res = sum(args)
        print(f"res: {res}")
        return res

    r = add(1, 4, 5)
    print("Returned value : {}".format(r))


if __name__ == "__main__":
    # prolog()
    exampleOne()
