
"""
Task: take in a number, check if it is a palindrom, or if the sum of itself multiplied with 2 is a palindrom
Check if, for 100 multiplications

Palindrom = a number that is the same backwards. 121, 11, 55,

example : 28 + 82 = 110 + 011 = 121 --> palindrome
example : 196 is not a palindrom, or any of its multiplications. should then return -1

So return the palindrome, or -1 if not number or able to "create" a palindrom.
"""


def transform(number, depth=0, multiplications=0):
    maxDepth = 100
    multiplications += multiplications
    if depth == maxDepth:
        print("Multiplications: ", str(multiplications))
        return -1

    if checkIsPalindrom(str(number)):
        print("Multiplications: ", str(multiplications))
        return number

    reverse = int(str(number)[::-1]) # reverse the number
    sum = str(number + reverse) # add the org number with it self reversed

    if not (checkIsPalindrom(sum)): # if not a palindrome, try a new addition
        return transform(int(sum), depth +1, multiplications + 1)

    else:
        print("Multiplications: ", str(multiplications))
        return sum


def checkIsPalindrom(number):
    for i in range(1,len(number)):
        if number[i-1] != number[-i]:
            return False

    return True





def main():
    print(transform(28))



# check that it's this functions .py that is trying to execute the main function.
if __name__ == "__main__":
    main()
