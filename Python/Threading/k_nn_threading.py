''' kNN threaded (multiprocess) example

We use multiprocess to handle with CPU-bound problems, so we can escape the GIL
for I/O bound problems, we use thread or multithread module

multiple process are not going to give a benefit, if small data, or not cpu bound tasks.
This because spawning a new process cost wrt. allocating resources, aka. overhead.


This is an implementation of kNN, as a multithreading example

kNN algoriths is;
Calculate distance from point x, to all other points
take the majority of the  k closest points to x, and assign x the majority class or regression value

We can benefit from multithreading, by allowing parallel calculation of distances
'''
import math, time, multiprocessing
import numpy as np
from queue import PriorityQueue
from multiprocessing.managers import SyncManager

'''
Threading setup to share priorityQueue
'''

class kNNManager(SyncManager):
    pass

kNNManager.register("PriorityQueue", PriorityQueue)

def Manager():
    m = kNNManager()
    m.start()
    return m

'''
The script actually starts here
'''


def find_neighbors(x, examples, dist_nbrs=None):
    dist_to_neighbors = PriorityQueue()
    if dist_nbrs:
        dist_to_neighbors = dist_nbrs
 
    for ex in examples:
        temp_sum = 0
        for i, ai in enumerate(ex[:-1]): # skip the target value
            temp_sum += pow(ai - x[i], 2)
        dist_to_neighbors.put((math.sqrt(temp_sum), ex[-1], ex[:-1]))
       
    return dist_to_neighbors

def classify(k, dist_to_neighbors):
    voting = {}
    for nbr in range(k):
        vote = dist_to_neighbors.get()[1]
        voting[vote] = voting.get(vote, 0) + 1

    target = max(voting, key=voting.get)
    return target
        

def k_nn_single(x, k, examples):
    start_time = time.time()
    dist_to_nbrs = find_neighbors(x, examples)
    target = classify(k, dist_to_nbrs)
    end_time = time.time()
    
    print("Single threaded got target {}\n used {}s".format(target, end_time - start_time))

def k_nn_multi(x, k, examples):
    # we can only thread the operation of finding distances to neighbours
    num_processes = 2
    jobs = []
    m = Manager()

    example_distributions = np.array_split(examples, num_processes)
    dist_nbrs = m.PriorityQueue()    
    for i in range(num_processes):
        process = multiprocessing.Process(target=find_neighbors,
                                         args=(x, example_distributions[i], dist_nbrs))
        jobs.append(process)

    start_time = time.time()
    # start the processes of finding neighbors distance
    for p in jobs:
        p.start()

    # wait for all the processes to be done
    for p in jobs:
        p.join()

    # Now we just need to classify
    target = classify(k, dist_nbrs)
    
    end_time = time.time()
    print("Multi threaded got target {}\n used {}s".format(target, end_time - start_time))



if __name__ == "__main__":
    d = np.loadtxt("data/data.txt", dtype=float, comments="#", delimiter=",")
    
    k_nn_single(x=[1,2], k=2,  examples=d)
    k_nn_multi(x=[1,2], k=2, examples=d)



