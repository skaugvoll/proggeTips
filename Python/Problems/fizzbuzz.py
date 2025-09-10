


def checkIfFactorOf(numberToCheck, factor):
    if not (numberToCheck % factor == 0):
        return False
    return True


def fizzBuzz(maxNumber):
    numberOfThree = 0
    numberOfFive = 0
    numberOfTBoth = 0

    # start on one, because something divided by 0 is 0. maxNumber +1 because range is; up to, not included.
    for number in range(1, maxNumber + 1):
        string = ""
        if checkIfFactorOf(number, 3):
            numberOfThree += 1
            string += "Fizz"
        if checkIfFactorOf(number, 5):
            numberOfFive += 1
            string += "Buzz"
        if checkIfFactorOf(number, 3) and checkIfFactorOf(number, 5):
            numberOfTBoth += 1

        # if we found a number that was a factor of one or both, our string is not empty
        if string:
            print(string)
        # if our string was empty, then the number was not a factor, and we print the number
        else:
            print(number)

    # when done with the "solving", show some statistics
    print("\n" * 2)  # just to get some space between solving and statistics

    print("Number (#) of factors, between 1 and ", maxNumber)
    print("# of % 3: ", numberOfThree)
    print("# of % 5: ", numberOfFive)
    print("# of % 3 & 5: ", numberOfTBoth)


def main():
    fizzBuzz(10)


if __name__ == "__main__":
    main()


