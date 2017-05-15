
'''
In this script I will explaine how to write a recursive funtion.
there is 4 steps in doing it.
1.
    Write a if / elif / else, because in a recursive function, there will always be at least two cases.
    on case that stops the recursion / looping. This is called the base case,
    and one case where the function calls itself.

2.
    Figure out the base case, and write it.

3.
    Write the recursive function.
    it is important to use return in a recursive function, because this is what makes the function backwind from the base case.

4.
    Assume and hope the recursive funtion works.


why return, you ask?
    In a recursive call we have to write return, because of "The Stack". What is the Stack you ask? The stack is what
    language remebers about you recursive call.

    in a recursive call, the function calls itself, all the way down to the base case.
    when the function reaches the base case, we have to unwind / backup the stack.
    To back up, we have to return the value of the base case, to the call (the recursive call).
    thats why we write return, so that we can unwind, return the value to the call, all the way up, until we have solved all the
    recusive calls and have our answer, we then have to retun to the call, that started / called the recursive funciton.

    I'll explaine with a call to recursive(5).

    n = 5:    the function checks if 5 == 1, nope, so then we return 5 + recursive(5-1), here we have a recursive call, so
    n = 4:    the function checks if 4 == 1, nope, so then we return 4 + recursive(4-1),
    n = 3:    the function checks if 3 == 1, nope so then we return 3 + recursive(3-1)
    n = 2:    the function checks if 2 == 1, nope so then we return 2 + recursive(2-1)
    n = 1:    the function checks if 1 == 1, YES! so then we return 1

    since we now have built our stack of recursive calls, we backwind from the base case to the top.
    n = 1: returns 1
    n = 2: returns 2 + 1 (the return value from recursive(2-1) = 3
    n = 3: returns 3 + 3 (the return value from recursive(3-1) = 6
    n = 4: returns 4 + 6 (the return value from recursive(4-1) = 10
    n = 5: returns 5 + 10(the return value from recursive(5-1) = 15

    so the function returns the value 15.
'''
def recursive(n):
    #base case, this is what will stop the recursive, and make it unwind / backup.
    if n == 1: #this is the base case.
        return 1
    else:
        #i want to add together all the number from n down to zero. aka if n = 5, the funciton should return 5  + 4 + 3 +2 +1 +0 = 15
        # i would like to add n + n-1
        return n + recursive(n-1)

print(recursive(100))


def recursiveFibo(n):
    if n == 0: # base case
        return 0
    elif n == 1: # base case
        return 1
    else:
        return recursiveFibo(n-1) + recursiveFibo(n-2) # return (n - 1) + (n - 2), until base cases is reached.

print(recursiveFibo(20))
