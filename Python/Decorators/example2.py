from time import time_ns


def timer(func):
    def wrapper(*args, **kvargs):
        start = time_ns()
        res = func(*args, **kvargs)
        execution_ms = (time_ns() - start) / 1000
        print(f"Execution took {execution_ms}ms")
        return res

    return wrapper


'''
create two identical fibon-functions,
one with and one without timer decorator
to Show the different behaviour when having recursive functions
'''


def recursiveFibo(n: int):
    if n == 0:  # base case
        return 0
    elif n == 1:  # base case
        return 1
    else:
        return recursiveFibo(n-1) + recursiveFibo(n-2)


@timer
def recursiveFiboWithTimerDecorator(n: int):
    if n == 0:  # base case
        return 0
    elif n == 1:  # base case
        return 1
    else:
        return recursiveFibo(n-1) + recursiveFibo(n-2)


@timer
def timeRecursive():
    return recursiveFibo(5)


if __name__ == "__main__":
    print(f"-"*10)
    print('result: ', recursiveFibo(5))
    print(f"-"*10)
    print('result: ', recursiveFiboWithTimerDecorator(5))
    print(f"-"*10)
    print("result: ", timeRecursive())
    print(f"-"*10)
