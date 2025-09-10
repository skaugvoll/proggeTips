
# this function just checks to see if given number is of a given factor
def checkIfFactorOf(numberToCheck, factor, quoteToReturn=""):
    # if not a factor
    if not (numberToCheck % factor == 0):
        return False

    # if number is a factor
    return True


# this function does the actual logic, and solves for the current number
def solve(number):
    str = "" # string builder, we use this variable to build up our fizzbuzz string.
    if checkIfFactorOf(number, 3):
        str += "Fizz"
    if checkIfFactorOf(number, 5):
        str += "Buzz"

    # if we found a number that was a factor of one or both, our string is not empty
    if str:
        return str

    # if our string was empty, then the number was not a factor, and we print the number
    else:
        return number


def fizzBuzz(number, maxNumber):
    if (number == maxNumber):
        x = solve(number)
        print(x)
        return str(x)

    else:
        print(solve(number))
        return fizzBuzz(number+1, maxNumber)


def main():
    fizzBuzz(1, 100)

if __name__ == "__main__":
    main()