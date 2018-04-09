import time

def fibonacci_python(numInSeq):
    if numInSeq == 0:
        return 0
    elif numInSeq == 1:
        return 1

    return fibonacci_python(numInSeq - 1) + fibonacci_python(numInSeq - 2)


def main(upToSequenceNumber=30):
    ####
    # PYTHON
    ####
    sequence = []
    start_py_time = time.time()
    for numInSeq in range(upToSequenceNumber):
        sequence.append(fibonacci_python(numInSeq))

    end_py_time = time.time()
    print("Python collecting seq used: {:.5f}s and the sequence is:\n{}".format(end_py_time - start_py_time, sequence))


if __name__ == "__main__":
    main()
