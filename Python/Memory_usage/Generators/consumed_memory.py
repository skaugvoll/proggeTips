import psutil as psu

# this shows how much memory we have used
memory_used = psu.virtual_memory()[3]
print(memory_used)


# Decide how many elements in list to create
num_elements = 1000000


# Lets create a list and see how much memory it consumes
memory_used_b = psu.virtual_memory()[3]
list = [x for x in range(num_elements)]
memory_used_a = psu.virtual_memory()[3]
print("memory used with list for \n{} Elements is\n{}".format(num_elements, memory_used_a - memory_used_b))


# lets create a generator function instead of a list
def generator(num_elements):
    for i in range(num_elements):
        yield i

# Lets see how much memory the generator object usees!
memory_used_b = psu.virtual_memory()[3]
gen = generator(num_elements)
memory_used_a = psu.virtual_memory()[3]
print("memory used with generator for \n{} Elements is\n{}".format(num_elements, memory_used_a - memory_used_b))

# Freeky to see that the generator object does not use any memory, this is because it knows what to do next
# in stead of creating a list with a million elements, it creates one element at a time, and knows what element is the next to create
# this gives huge performance benefits
