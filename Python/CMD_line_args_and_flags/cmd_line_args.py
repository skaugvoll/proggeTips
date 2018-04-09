import argparse

'''
if added argument IS NOT prefixed with anything, its a must have
and the order is important. they must be given on cmd line
in the same order as given in code. This then gives that we
can not call the script with the argument name then the values
only the values
ALLOWED : cmd_line_args.py thisIsMustHave_order_1_Value
DISSALOWED: cmd_line_args.py musthave_order_1 thisIsMustHave_order_1_Value
DISSALOWED: cmd_line_args.py -musthave_order_1 thisIsMustHave_order_1_Value

If added argument IS prefixed with '-' or '--' it's optinal
and must be checked if present or not. The order given on cmd line
is not important

Docs:  https://docs.python.org/2/library/argparse.html#module-argparse
HowTo: https://docs.python.org/3.6/howto/argparse.html#id1
'''

parser = argparse.ArgumentParser()
parser.add_argument("musthave_order_1", help="This must be specified before mustahve_order_2")
parser.add_argument("musthave_order_2", help="This must be specified after mustahve_order_2")
parser.add_argument("-optional_1_order_not_important", help="must be after musthave_args_but_can_be_before_or_after_-optional_2_order_not_important")
parser.add_argument("-optional_2_order_not_important", help="must be after musthave_args_but_can_be_before_or_after_-optional_1_order_not_important")
args = parser.parse_args()
print(args.training)

if not args.training:
    print(" oo")
