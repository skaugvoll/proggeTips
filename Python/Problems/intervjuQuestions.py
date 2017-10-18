# Source : https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6 : Online : 16.sept. 00.49am

"""
Q1:
Create a function that takes the name of a directory
    and prints out the paths, to files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
"""

def print_directory_contents(sPath):
    import os # import the operating system module
    for sChild in os.listdir(sPath): # os.listdir(sPath) returns a array with all files at sPath
        sChildPath = os.path.join(sPath,sChild) # joint (conncatonate) the given path with the found file name to create absolute path
        if os.path.isdir(sChildPath): # if the newly created conncatination of a absolute path, is a directory
            print_directory_contents(sChildPath) # find all files within the found directory
        else: # if the found file/path is not a directory,
            print(sChildPath)  # print the found file path.

# print_directory_contents("/Users/sigveskaugvoll/Documents/programming/proggeTips/Python/Problems")


'''
What does this (function addero) output?

Answer:
[0, 2]
[3, 2, 1, 0, 2, 4]
[0, 2, 0, 2, 4]

Does not make sense?
The first function call should be fairly obvious,
the loop appends 0 and then 2 to the empty list, l.

l is a name for a variable that points to a list stored in memory.

The second call starts off by creating a new list in a new block of memory.
l then refers to this new list.
It then appends 0, 2 and 4 to this new list. So that's great.

The third function call is the mad weird one.
It uses the original list stored in the original memory block (call one / first call).
That is why it STARTS OFF with 0 and 2.

>>> See adderoWritenOut to make it into more sense!

'''
def addero(x,l=[]):
    for i in range(x):
        l.append(i+i)
    print(l)

addero(2)
addero(3,[3,2,1])
addero(3)


def adderoWritenOut():
    l_mem = []

    l = l_mem           # the first call
    for i in range(2):
        l.append(i+i)

    print(l)            # [0, 2]

    l = [3,2,1]         # the second call
    for i in range(3):
        l.append(i+i)

    print(l)            # [3, 2, 1, 0, 2, 4]

    l = l_mem           # the third call
    for i in range(3):
        l.append(i+i)

    print(l)            # 0, 2, 0, 2, 4]
