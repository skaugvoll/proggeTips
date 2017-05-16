"""
Lambda tutorial
Some of the explainations is written by me, other explainations I have found online and cannot give a better explaination my self. so I borrowed it and possibly refraced it.
Refrences :
    urls = [
    'https://docs.python.org/2/library/functions.html#zip',
    'http://book.pythontips.com/en/latest/lambdas.html',
    'http://www.python-course.eu/lambda.php',
    'https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/'
    ]

* What is lambda you ask?
Lambda is a tool for building functions, or more precisely, for building function objects. That means that Python has two tools for building functions: def and lambda.

* When do we NEED to use lambda?
Actually, we don’t absolutely need lambda; we could get along without it. But there are certain situations where it makes writing code a bit easier,
and the written code a bit cleaner. What kind of situations?
Situations in which
(a) the function is fairly simple, and
(b) it is going to be used only once.

* When do we WANT to use lambda?
1. We want to use lambda to write cool code, and make others think we are pro, while we realy arent.
2. Lambda can do alot of cool stuff, and use cool function such as map, filter, etc.
3. Did I meantion the cool functions lambda allowes us to use? (see 2)
4. When you need a function, but you only need it once.

* What to remember?
1. The return statement is, in a sense, implicit in a lambda. Since a lambda specification must contain only a single expression,
and that expression must return a value,
an anonymous function created by lambda implicitly returns the value returned by the expression.

** How to write a lambda expression **
the first thing we need is the _lambda_ keyword. This word defines / states that we want to write a lambda expression.
The next thing we need is to pass arguments into the lambda expression / functions, and then to end the lambda 'header', we use the ':' colon sign.
Then we have defined the lambda expression 'header'.
>>> lambda arg1, arg2:

The next thing is to define the function body, what does the expression / function do?
write the lambda expression 'body / function' # remember that the expression has to return something. but we doent have to write explisit the 'return' keyword.

Now your all done.
"""

def simplicity():
    # the simplest example of a working lambda expression is to add to arguments:
    print("#### Lambda expression to add two numbers ####")
    print("add = lambda x,y: x + y \n print(add(2,10))")
    add = lambda x,y: x + y
    print("lambda result: ", add(2,10))
    # >>> Output: 12


"""
Well I could have ended the tutorial here, because now you know 'everything' needed to get started with lambda expressions.
Including writing your own. I meantioned cool functions earlier, so now I'm going to show you some of them and how they work.
"""

###### COOL FUNCTIONS  ###
numbers = [1,2,3,4,5,6]
num = [9,8,7,6,5,4]


def lambdaMap():
    '''
    __map__ function.
    map() is a function with two arguments and returns a iterator object, that we can make into a list by encapsulating the map function with a list function.
    list(map(func, seq)) Now the results will be stored as a list and not an iterator object.

    Use this function to iterate through each object and then we can modify the object.

    m = map(func, seq)
    The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies the function func to all the elements of the sequence seq.
    Map returns a new iterator object with the elements changed by func. If we want this to became a list, we can as said above, encapsulate / souround the map function with a list function.

    map() can be applied to more than one list. The lists have to have the same length (if they doent, map will fill the shorter list with none objects).
    map() will apply its lambda function to the elements of the argument lists, i.e. it first applies to the elements with the 0th index,
    then to the elements with the 1st index until the n-th index is reached

    DOCS : Apply function to every item of iterable and return a list of the results.
    If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.
    If one iterable is shorter than another it is assumed to be extended with None items.
    '''
    print("#### Lambda expression to iterate trough list(s) and manipulate the elements ####")
    print("**One list, incrementing the value with one")
    print("lambda expression: incrementNumbers = map(lambda x: x + 1, numbers)")

    print("numbers list: ", numbers)
    # result iterator object name = for each (map-function) x in numbers, do : x + 1 and return to the incrementNumbers iterator object.
    incrementNumbers = map(lambda x: x + 1, numbers)
    print("numbers list incremented with one: ", list(incrementNumbers)) # list() is to make the iterator object retunred from map into a list.
    print("\n")
    print("**Two lists, adding indexes together")
    print('If correctly, the new list will have the sum 10 in each index')
    print('What we are doing is, we are taking index i from each lists and then adding them together')
    print("numbers: ", numbers, "\nnum: ", num)
    print("lambda expression: add = map(lambda x,y: x + y, numbers, num)")
    #     for each (map-function) x and y (objects and index in list x=numbers, y=num), do: x + y then: return the result to the add iterator object.
    add = map(lambda x,y: x + y, numbers, num)
    print("Lambda result: ", list(add)) # using the list function to make the iterator object from map, into  a list.


def lambdaFilter():
    '''
    The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which the function function returns True.
    The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False. This function will be applied to every element of the list l.
    Only if f returns True will the element of the list be included in the result iterator object.

    '''
    # create a Person class to make test person objects.
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def getAge(self):
            return self.age

        def __repr__(self):
            return self.name

    # Create a few Person objects we can play around with.
    p1 = Person("Sigve", 22)
    p2 = Person("Ellen", 21)
    p3 = Person("Siri", 18)
    persons = [p1,p2,p3] # collect the person objects into a list.


    print("#### Lambda expression to filter out list elements ####")
    print("**filter function")
    print("This function goes through the list and evaluate element for element of the list, using the given function.")
    print("We want to filter through a list with people, and only have the ones of legal drinking age left.")
    print("The persons are (Sigve, 22), (Ellen,21), (Siri, 18). This means that we want to have Sigve and Ellen in the iterator object.")
    print("lambda expression: legal = filter(lambda x: x.getAge() >= 21, persons)")

    # return only the Persons that is of legal US drinking age. (>21)
    legal = filter(lambda x: x.getAge() >= 21, persons)
    print("lambda result: ", list(legal))



def lambdaReduce():
    '''
    NOTE: the function reduce ONLY WORKS on Python version < 3.x, to make the function reduce work in this example, we have to use functools.reduce (only if we realy!! need reduce-function)
    reduce(func, seq)
    I think reduce is a misleading function name. It does reduce the list, but now how you think. It does not go through the list, checks if the element is to be removed or not.
    reduce goes through the list (seq) and makes it smaller, but it does so by first;
    1. taking the first two elements of the list (seq), then executes a function (func) on the two elements, which makes the two elements into ONE element.
    2. Then reduce takes the next element in the list (seq) and passes into the function (func) with the new value from the last reduce-iteration. Executes the function and combines tho tow elements into one element
    3. This repeats through the entire list (seq).
    4. When reduce has gone through the entire list, it returns only ONE element, wich is all the elements modified by function (func) into this one element.

    Example of use would be to go through a list of numbers and then subtracting each number one by one.
    it would work like this, if the list is [5,4,3,2,1]
    func(5,4) --> 5 - 4 = 1
    func(1, 3) --> 1 - 3 = -2
    func(-2, 2) --> -2 - 2 = -4
    func(-4,1) --> -4 - 1 = -5
    The list [5,4,3,2,1] is reduced to the element -5.
    '''
    import functools # only needed for python 3.x and this example

    print("#### Lambda expression to reduce / combine list elements into one element ####")
    print("**Reduce function")
    print("This function goes through the list and combines two and two elements of the list, using the given function, until there is only one element left in the list.")
    print("The list we want to take each element and subtract it from the next element: [5,4,3,2,1]. So we want to take 5-4-3-2-1 which should give us -5")
    print("lambda expression: invert = reduce(lambda x,y: x - y, numb)")
    numb = [5,4,3,2,1]
    invert = functools.reduce(lambda x,y: x - y, numb) # functools. is needed because reduce was removed from python 3.x
    print('The reduced result: ', invert)





def main():
    print('Hello and welcome to this tutorial about lambda expressions.')
    print('The first thing we need to know is the syntax: "lambda argument_list: expression" lambda is a keyword and is mandatory.')
    print("\n"*2)
    simplicity()
    print("\n"*2)
    lambdaMap()
    print("\n"*2)
    lambdaFilter()
    print("\n"*2)
    lambdaReduce()

main()
