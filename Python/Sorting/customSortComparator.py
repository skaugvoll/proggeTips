'''
This is only for Python 2.x NOT python 3.x
In python 3, the cmp keyword is no longer supported by sorted-function.
'''


'''
An example of what we want to do today
Lets say we have a list with three elements, where each element is a list with two elements.
This gives us the data format: [ [1,1], [8,9] [1,2]  ].

Now if we want to sort this in a ascending way (low to high):
if [1,1] and [8,9] is compared parameter a [1,1] has 1 as the first element, and parameter b, has 8 as first elemetn so 1 - 8 = -7, which gives us that the first element [1,1] ~ parameter a, is to be sorted before parameter b [8,9] in the list.

if [1,1] and [1,2] is compared both has 1 as the first element, so 1 - 1 = 0, then we can sort on the second element, which gives us 1 - 2 = -1. -1 means that the first element [1,1] ~ parameter a, is to be sorted before parameter b in the list.

Note: remeber that lists has index 0 for the first element. so to get 1, from a = [1,2] we have to write a[0], and to get 2, we have to write a[1]
'''


# this is just to show and describe what is going on in a sort function. what the sort function actually do.
def customComparatorFunction(a, b):
  if a[0] - b[0] < 0: # positiv number is a first,
    return -1  # -1 means sort a first

  elif a[0] - b[0] > 0: # positiv number is b first
    return 1 # 1 means sort b first

  else: # 0 they have the same value, sort on the second element in the element-list
    return a[1] - b[1] # sort based on the second value in the element-list


# A better way of writing the comparator, does accatly the same! (but with less code)
def betterCustomComparatorFunction(a, b):
  if a[0] - b[0] == 0: # if they are the same (0), we can sort on another attribute
    return a[1] - b[1] # sort based on the second value in the "element-list" (element list is not the entire list, but the inner list in the nested list.)

  return a[0] - b[0]  # negativ number is 'a' first, positiv number is 'b' first



# this function takes in a 2-d array (nested list), and a optional boolean reverseSort, default False
def sortMyArray(arraylist, reverseSort=False):
  # the cmp and reverse is optional for sorted function
  sortedList = sorted(arraylist, cmp=betterCustomComparatorFunction, reverse=reverseSort)

  print(sortedList) # print the sorted list.




# 2D array we want to sort
l = [[7,9],[1,2], [3,3], [1,1], [3,3]]

# sort using only the customComparatorFunction
print("Sorting in a ascending way, default")
sortMyArray(l) # do not need to pass in an argument for the revereSort, because we have set a default in the method

print("\n"*2) # print space between the two sorted lists

# sort in a reverse / decending way, using the customComparatorFunction
print("Sorting in a decending way, specified in the method call")
sortMyArray(l, True) # passes in the 2D list, and wants to reverse sort it.
