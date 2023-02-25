# This is a sample Python script.
import math
import time
from substr_search import RabinKarp

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pattern, text = 'test', 'this is a test'
    algorithm = RabinKarp(pattern, text)
    print(algorithm)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/