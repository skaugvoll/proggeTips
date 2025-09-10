'''
A reguler expression (REGEX), is a sequence of characters that define a search pattern.

REGEX syntax has syntax, meaning some operators / keywords:

To use regeular exprexxsions (regex) in python, we need to import the module 're'

'''

import re # import regular expression module, so we can write regex's

def regex():
    '''
    There are many regular expression operators.
    Here are some of the most common, and their meaning.
    '''
    print("#### Boolean")
    print("The '{}' operator means 'or' as in boolean or").format('|')

    print("#### Operators")
    print("The '{}' operator matches 'all characters except new line'").format('.')
    print("The '{}' operator matches 'the start (first character/ word) of a string. Has to be placed BEFORE the character/word to match'").format('^')
    print("The '{}' operator matches 'the end of a string or just before the new line character. Has to be placed after the character/word to match'").format('$')

    print("##### Number of matches : matches as many as POSSIBLE - GREEDY - goes thrugh the entire string")
    print("The '{}' operator matches '0 or more repetitions of the PRECEDING REGEXString'").format('*')
    print("The '{}' operator matches '0 or 1 repetition of the preciding REGEXString'").format('?')
    print("The '{}' operator matches '1 or more repetition of the preciding REGEXString'").format('+')

    print("###### PRO TIP!")
    print("Adding ? after the regex search, will make it a non greedy search. - after found a match, stops searching in the string!")

    print("##### Number of matches : matches as many as WANTED")
    print("The '{}' operator returns true if the string search contains m-times EXACTLY of the preciding REGEXString''").format('{m}')
    print("The '{}' operator returns true if the string search contains MINIMUN-times of the preciding REGEXString''").format('{min,}')
    print("The '{}' operator returns true if the string search contains BETWEEN min and max times of the preciding REGEXString''").format('{min,max}')

    print("#### Groupings")
    print("The '{}' operator defines the scope and precedence of the operators").format('{()}')
    print("The '{}' .... ").format('{[]}')

def regex1():
    '''
    A boolean or in regex is expressed as '|'.
    '''
    stringToCheck = "does this include super or man"
    contains = re.search("super | man", stringToCheck) # returns a boolean regex object
    print(bool(contains)) # cast the boolean regex to a boolean

def regex2():
    '''
    Check if string is not empty or new line!
    '''
    stringToCheckTrue = "123456789"
    stringToCheckFalse = "\n"
    containsTrue = re.search(".", stringToCheckTrue)
    containsFalse = re.search(".", stringToCheckFalse)
    print("ContainsTrue: {}, and containsFalse: {}").format(bool(containsTrue), bool(containsFalse))

def regex3():
    '''
    Checks if the first word in a string is 'love'
    '''
    stringToCheck = "Love me tender"
    contains = re.search("^Love", stringToCheck)
    print(bool(contains))

def regex4():
    '''
    Checks if the last word in a string is 'love'
    '''
    stringToCheck = "Love me tender"
    contains = re.search("tender$", stringToCheck)
    print(bool(contains))

def regex5():
    '''
    Lets try to combine some regexes!
    Lets check if Love is the first word and tender is the last

    To do this, we have to combine a few operators and build up a regex string.
    So we start with a empty regex = ""

    1.The first thing we know, is that the string to check should have Love as the first word
        This we know how to write a regex for. so lets add it to our regex

    Now our regex looks like this "^Love"
    2.The next we know is that our string to check can have any number of any characters,
        This we also kow how to write a regex for '.*'  --> '.' is all characters, and '*' is any number of times.
        so lets add it to our regex!

    Now our regex looks like this "^Love.*"
    3.The last thing we know is that our string to check last word/characeter is tender,
    we know how to write a regex for this, so lets add it to our regex!

    Now finaly our regex looks like this: regex = "^Love.*tender$"
    '''
    stringToCheck = "Love me tender"
    contains = re.search("^Love.*tender$", stringToCheck)
    print(bool(contains))


def regex6():
    '''
    If we want to take regex5() a step further, to check that between Love and tender there are 4 characters (including white space)
    and that 2 of those characters are 'me'. we have to add to step 2 from regex5()

    regex = "^Love"

    1. One way of writing a regex to match: 1 whitespace, 'me' and 1 whitespace
    add: {1}me {1}  # NOTE the whitespace! - {1} means EXACTLY one of the preciding character/word, which here is a whitespace
    regex = "^Love {1}me {1}tender$"
    '''
    stringToCheck = "Love me tender"
    contains = re.search("^Love {1}me {1}tender$", stringToCheck)
    print(bool(contains))


def regex7():
    '''
    Regex to match a formatted Norwegian mobile number
    '''
    regex = "[0-9]{3} [0-9]{2} \d{3}" # \d == [0-9] == Any digit in range 0 to including 9
    stringToCheckTrue = "909 09 909"
    stringToCheckFalse = "90909909"
    StringToCheckFalse2 = "9090990a"
    containsTrue = re.match(regex, stringToCheckTrue)
    containsFalse = re.match(regex, stringToCheckFalse)
    containsFalse2 = re.match(regex, StringToCheckFalse2)
    print("CT : {}\nCF1: {}\nCF2: {}").format(bool(containsTrue), bool(containsFalse), bool(containsFalse2))


def main():
    # regex1()
    # regex2()
    # regex3()
    # regex4()
    # regex5()
    # regex6()
    regex7()


main()
