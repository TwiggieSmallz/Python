import sys
sys.path.insert(0, r'C:\ProgramData\Anaconda3')

import re


print("Welcome! Calculator is ready.\n Type 'quit' to exit.\n")

previous = 0
run = True
equation = ''


def performMath():
    global run
    global previous
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        run = False
        print("Now exiting calculator")
    else:
        equation = re.sub('[a-zA-Z,:_" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()