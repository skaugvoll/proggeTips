'''
Rembember to compile the cython file (.pyx)
into .c and .so so that it becomes a compiled module!
$ cythonize -i cy_fibonacci.pyx

I have made this script compile the .pyx before it runs the main function

'''
import cy_fibonacci, py_fibonacci
import time, argparse, sys



def createCMD_arguments():
    parser = argparse.ArgumentParser(description="Compare Python and Cython on calculating fibonacci sequence up to given argument")
    parser.add_argument("calculateSequenceNumber", type=int, help="Specify which sequence number to find :: int")
    parser.add_argument("-collectUpTo", type=int, help="Specify how far sequence should collect :: int")
    try:
        args = parser.parse_args()
        return args
    except:
        parser.print_help()
        sys.exit(0)


def main(upToSequenceNumber=35, caluateUpTo=None):
    if caluateUpTo == None:
        caluateUpTo = upToSequenceNumber
    print("Now starting the show")
    ####
    # PYTHON
    ####
    start_py_time = time.time()
    py_fibonacci.fibonacci_python(upToSequenceNumber)
    end_py_time = time.time()
    print("Python used: {:.5f}s on finding sequence {}".format(end_py_time - start_py_time, upToSequenceNumber))
    ####
    # CYTHON CP DEF
    ####
    start_cy_time = time.time()
    cy_fibonacci.fibonacci_cython_cpdef(upToSequenceNumber)
    end_cy_time = time.time()
    print("Cython cpdef used: {:.5f}s on finding sequence {}".format(end_cy_time - start_cy_time, upToSequenceNumber))
    ####
    # PYTHON and CYTHON collecting sequence
    ####
    print("\nNow testing with collecting sequence upto {}\n".format(caluateUpTo))
    print("Now testing with python...")
    py_fibonacci.main(caluateUpTo)
    print
    print("Now testing with Cython...")
    cy_fibonacci.main(caluateUpTo)


if __name__ == "__main__":
    args = createCMD_arguments()
    import sys, os
    os.system("cythonize -i cy_fibonacci.pyx")

    main(args.calculateSequenceNumber, args.collectUpTo)
