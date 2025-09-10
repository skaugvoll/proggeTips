'''
Since this is a cython file (.pyx) this must be compiled before runned

a .pyx file is compiled by Cython to a .c file
the .c file is compiled by a C compiler to a .so file (or a .pyd) file on windows

run the cythonize compiler command with your options and list of .pyx files to generate
$ cythonize -a -i your_file.pyx

:: -a gives a .html file
:: -i gives inplace, not sure what it means

This creates a your_file.c and a .so or .pyd

after running this command you can create another python file which imports
this module, and uses it.
see testing_fibonacci.py

def is basic python so it can be used in both python and cython

cdef function can be called from only Cython and C.

cpdef can be called from Cython and Python

The fibonacci sequence is:
seqNum: 1   2   3   4   5   6   7   8   9   10  11  12
        1,  1,  2,  3,  5,  8,  13 ,21, 34, 55, 89, 144
alt
        0,  1,  1,  2,  3 ...

Thus the algorithm is:
Fn = Fn-1 + fn - 2
F1 = 1, F2 = 1 or F0 = 0 F1 = 1

'''
import time

cpdef int fibonacci_cython_cpdef(int numInSeq):
    cdef int a, b
    a, b = 0, 1
    if numInSeq == a:
        return 0
    elif numInSeq == b:
        return 1

    return fibonacci_cython_cpdef(numInSeq - 1) + fibonacci_cython_cpdef(numInSeq - 2)



cpdef void main(int upToSequenceNUmber=30):
    ####
    # CYTHON
    ####
    cdef int numInSeq = 1
    cdef sequence = []
    start_cy_time = time.time()
    for numInSeq in range(upToSequenceNUmber):
        sequence.append(fibonacci_cython_cpdef(numInSeq))

    end_cy_time = time.time()
    print("Cython collecting seq used: {:.5f}s and the sequence is:\n{}".format(end_cy_time - start_cy_time, sequence))

if __name__ == "__main__":
    main()
