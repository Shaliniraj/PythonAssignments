""" This program is used to find the different actions performed by a storage tank
"""

def do_action(present, redmark, bluemark):
    if present == redmark:
        print("The tank is less than 20% full, please buy more liquid")

    elif present == bluemark:
        print("The tank is more than 80% full, please raise an alarm")
    


def get_current_level():
    tankvalue = int(input("Please enter the current level of ethonol in the tank"))
    return tankvalue

capacity = 900
bluemark = 80
redmark = 20

high = bluemark > capacity
low = redmark < capacity
level = get_current_level() 

do_action(level, high, low)
