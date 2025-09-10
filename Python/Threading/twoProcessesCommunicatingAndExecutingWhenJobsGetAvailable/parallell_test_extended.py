import time
import random
import numpy as np

from multiprocessing import Process, Queue, current_process, freeze_support

# MODEL Klassifisering
def worker(input_q, output, a, b, c):
    for window in iter(input_q.get, 'STOP'):
        print("worker executing", a, b ,c)
        if window[0] <= 5:
          res=(1, window)
          time.sleep(5.5)
        elif window[0] <= 13:
          res=(2, window)
          time.sleep(2.5)
        else:
          res=(3,window)
          time.sleep(0.05)

        # SUBMIT TASKS FOR ACTIVITY CLASSIFICATION
        output.put(res)
        print("worker done")

# AKTIVITET Klassifisering
def worker2(input_q):
  for window in iter(input_q.get, 'STOP'):
    model, w = window[0], window[1]
    time.sleep(0.5*random.random())
    print("MODEL: {}\nWINDOW: {}".format(model, w))

def paralle_run():
    NUMBER_OF_PROCESSES_models = 3
    NUMBER_OF_PROCESSES_class = 1
    windows = [
      [1,2],
      [3,4],
      [5,6],
      [7,8],
      [9,10],
      [11,12],
      [13,14],
      [15,16],
      [17,18],
      [19,20],
    ]

    # Create queues
    task_queue = Queue()
    done_queue = Queue()

    # Submit tasks for model klassifisering
    for window in windows:
        task_queue.put(window)

    # Lists to maintain processes
    processes_model = []
    processes_class = []

    # CREATEA worker processes on model klassifisering
    for i in range(NUMBER_OF_PROCESSES_class):
      processes_class.append(Process(target=worker2, args=(done_queue,)))

    # START the worker processes
    for process in processes_class:
      process.start()

    # CREATEA worker processes on model klassifisering
    for i in range(NUMBER_OF_PROCESSES_models):
        processes_model.append(Process(target=worker, args=(task_queue, done_queue, 1, 2, 3)))

    # START the worker processes
    for process in processes_model:
      process.start()


    # waith for tasks_queue to become empty before sending stop signal to workers
    while not task_queue.empty():
      pass

    # Tell child processes to stop waiting for more jobs
    for i in range(NUMBER_OF_PROCESSES_models):
        task_queue.put('STOP')

    # LET ALL PROCESSES ACTUALLY TERMINATE AKA FINISH THE JOB THEIR DOING
    while any([p.is_alive() for p in processes_model]):
        pass

    # waith for done_queue to become empty before sending stop signal to workers
    while not done_queue.empty():
      pass

    # Tell child processes to stop waiting for more jobs
    for i in range(NUMBER_OF_PROCESSES_class):
        done_queue.put('STOP')

    # LET ALL PROCESSES ACTUALLY TERMINATE AKA FINISH THE JOB THEIR DOING
    while any([p.is_alive() for p in processes_class]):
        pass

    all_processes = processes_model + processes_class

    # join the processes aka block the threads, do not let them take on any more jobs
    for process in all_processes:
      process.join()

    print("\nALL PROCESSES STATUS BEFORE TERMINATING:\n{}".format(all_processes))

    # Kill all the processes to release memory or process space or something. its 1.15am right now
    for process in all_processes:
        process.terminate()

    # continue the pipeline work
    # ...
    # ...
    # ...

if __name__ == '__main__':
    # freeze_support()
    paralle_run()

