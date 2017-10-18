'''
List comprehensions are just another way to write and declare lists

List comprehensions is almost accacly like mathematics define lists
l = {2^x: x in {0 ... 9}}


So in Python, the syntax is
[what we want to do FOR variable IN ITERABLE ]

Example
[ 2 ** x for x in range(4)] # now we say that we want a list with all
numbers 2 ^ x, where x is 0 to 4(not including) --> [2**0, 2**1, 2**2, 2**3] --> [1,2,4,8]
'''


def lcEx1():
    '''
    Creates a list with binary numbers 2^0, 2^1, 2^2, 2^3

    '''
    lc = [2 ** x for x in range (4)]
    # lc should now be equal to [2,4,8,16]
    print("LC: {} == {} are: {}".format(lc,[1,2,4,8], lc == [1,2,4,8]))

def lcEx2():
    '''
    Function that uses condition in list comprehensions

    Creates a list with binary numbers, only if the binary position
    is of even number. i.e 2^x, wher x is an even number, i.e x = 4 --> 2^4 --> 4
    '''
    lc = [2 ** x for x in range(100) if x % 2 == 0]
    print(lc)

def lcEx3():
    '''
    Creates a list with lists using list comprehensions

    '''
    lc = [ True for x in range(2) for y in range(5) ]
    lcX = [ x for x in range(2) for y in range(5) ]
    lcY = [ y for x in range(2) for y in range(5) ]
    # the first  True for x in range(1), decides how many  times, y-True's should be added
    # the second for y in range(5), decides how many Trues should be added for each x
    # So if x in range (1), we get  a sequence of only 5 Trues
    # if x in range (2), we get 2 seqeunces with 5 Trues --> 10 Trues

    # so to figure out how many elements in list x in range(2) and y in range(5)
    # we get 2 * 5 --> we want 2 sequences, with 5 elementes each = 10 elements in total

    # lcX should print 2 sequences (that gives us that x is 0 and 1, with y elements)
    # thus we should get 0'y times and 1'y times. --> 00001111
    # if we upped x's range to 3 we would get 000011112222
    # if we decreased y's range to 4 and x's range is 2 w would get 000111 <-- notice that we have 3 elements in 2 sequences

    # What will the result of lcY be ?
    # Y's value is 0,1,2,3,4 and we want to add those elements in 2 runs/sequences --> 0 1 2 3 4 0 1 2 3 4 is the result

    print("lc: {}\nlcX: {}\nlcY: {}".format(lc,lcX,lcY))




if __name__ == "__main__":
    lcEx1()
    # lcEx2()
    # lcEx3()
