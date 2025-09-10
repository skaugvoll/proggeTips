# Here we learn how to use generators

from creation import generator
g = generator()

# g is a generator that holds a list from 0 to 10 (not including)
# To get the next value from a generators, which is the first element is 0
# NOTE : the funtion next(generator), removes the element from the generator!
value = next(g)
print("Value is {} and should be {}".format(value, 0))

# the next value should be 1
print("Value is {} and should be {}".format(next(g), 1))

# if we want the entire list the generator holds, we can convert it
# this removes all the performance and memory benefits of a generator, becuase we construct the entire list
# Since we had a genertor from [0,9], and we have extracted 0 and 1
# the generator has [2,9] left, thus the generator_list should be [2,3,4,5,6,7,8,9]
generator_list = list(g)
print("The generator list is ", generator_list, " and should be [2,3,4,5,6,7,8,9]")
