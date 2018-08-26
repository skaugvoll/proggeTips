# A generator is basically just an iterator

# There are many ways to create a generator,
# one can create a custom generator
# one can use comprehensions to create generator
# one can use a function
# etc

# Lets start with the simplest one : generator function
def generator():
    '''
    This function creates a generator OBJECT / iterator
    The difference between this function and a function that returns a list
    Is that this function yields (returns one and one element) instead of the whole list at performance
    This means that we have to call a object method, called next, to get the next value from our generator
    in stead of just indexing it as with a list
    '''
    for e in range(10):
        yield e

func_gen = generator()
print("FUNCTION generator: ", type(func_gen))


# this one is also very simple : comprehension
comp_gen = (x for x in range(10))
print("COMPREHENSION generator: ", type(comp_gen))


# Creating a custom generator we can follow the usual pattern
# Using the generator pattern (an iterable)
# our custom generator is just going to return all integers from 0 to n
class CustomGenerator:
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    def __next__(self):
        return self.next() # returns the next value less then n

    def next(self):
        # check if out of range
        if self.num < self.n:
            # get the current number, and our count so we know what the next value is
            cur, self.num = self.num, self.num+1
            # return the integer to the "user"
            return cur
        # if we have reached the end, do not try and return another value
        else:
            raise StopIteration()

cust_gen = CustomGenerator(10)
print("CUSTOM generator: ", type(cust_gen))
