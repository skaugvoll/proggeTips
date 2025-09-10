
def isDivisableByTwo(number):
    return number % 2 == 0 # if the number is DIVISIBLE by two, without a fraction (rest), then its an even number


'''
An even number is an integer which is DIVISIBLE of two. If it is divided by two the result is not a fraction, but 0.
'''
def printAllEvenNumbersBetween(lowerLimit, upperLimit): # take inn two numbers that we want to print all even numbers between.
    for number in range(lowerLimit, upperLimit+1): # number is incremented between lower- and upperlimit. upperLimit + 1, because range takes from(including) to(excluding). So if ll = 1, and ul = 3, number would get 0,1,2 without +1
        if isDivisableByTwo(number): # check if number can be divided by two, without getting a fraction / rest number.
            print(str(number) + " is a EVEN number") # print the number, followed by a statement.

# printAllEvenNumbersBetween(0,100) # call the function, so that it executes and prints all the even numbers between 0 and 100.

'''
An odd number is an integer which is not DIVISIBLE of two. If it is divided by two the result is a fraction.
'''
def printAllOddNumbersBetween(lowerLimit, upperLimit):
    for number in range(lowerLimit, upperLimit):
        if not isDivisableByTwo(number): # if the number is not DIVISIBLE by two, result is a fraction/ not null, then its an odd number by definition.
            print(str(number) + " is a ODD number")

# printAllOddNumbersBetween(0,100)

'''
A number is a factor of another number if the number we want to find factors for, is divided by the num without getting a fraction.
'''
def printAllFactorsOfANumber(number):
    for num in range(1, number+1):
        if number % num == 0: # if the number we want to find all factors for, are DIVISIBLE by the num, without a fraction, then the num is a factor of the number we want to find all factors of.
            print(str(num) + " is a factor of " + str(number)) # print the num that is a factor of the number we want to find factors of, and just that its a factor of the number we want to find factors of.


printAllFactorsOfANumber(30)
