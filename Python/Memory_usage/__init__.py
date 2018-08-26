'''
Note this needs some external modules,
I recommend using anaconda and virtual environment
'''

from os import system

try:
    system("pip install -r requirements.txt")
except Error as e:
    print("Could not install requirements")
