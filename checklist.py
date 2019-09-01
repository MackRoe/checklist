import sys
from termcolor import colored, cprint


checklist = list()


# CREATE
def create(item):
    checklist.append(item)


# READ
def read(index):
    return checklist[index]


# UPDATE
def update(index, item):
    checklist[index] = item


# DESTROY
def destroy(index):
    checklist.pop(index)

# Verify correct index
# len(checklist)


def list_all_items():
    index = 0
    for list_item in checklist:
        cprint("{} {}".format(index, list_item), "cyan", "on_magenta")
        # removed extra parenthesis around "{} {}" √
        # formats output and accommodates different data types
    index += 1


# to mark as completed
def mark_completed(index):
    if item_worn == true:
        print("√ {}".format(list_item))


def select(function_code):
    # CREATE ITEM
    if function_code == "C":
        input_item = input("Input item:")
        create(input_item)
    elif function_code == "R":
        item_index = input("Index number?")
        if int(item_index) > len(checklist):
            print("Index is out of range. Please choose an index less than " + len(checklist))
            item_index = input("Index: ")
        # potential crash warning item_index
    # print all items
        read(int(item_index))
        print(int(item_index))
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")


def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    # Add your testing code here
    #
    # commented out experimental learning function_code
    #
    # def verify_index(checklist):
    # for x in checklist(x):
    # if x > len(checklist):
    # print ("Error! There aren't that many items in the list.")
    # else:
    # print (read(x))
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    # New Testing code
    select("C")
    list_all_items()
    select("R")
    list_all_items()
    select("P")
    list_all_items()
    select(" ")
    list_all_items()

    user_value = user_input("Please enter a value: ")
    print(user_value)


color_list = ["red", "purple", "blue", "green", "yellow", "orange"]
clothing_items = ["pants", "shirt", "jacket", "hat", "socks", "shoes"]

test()


# experimental learning exercize code - extra code commented out

# print("Good morning, Cpt Rainbow. It's time to get dressed.")
# GET WORN ITEMS
# worn_item = input("What would you like to wear first?")
# if worn_item == clothing_items():
    # create(worn_item)
# else:
    # print("That item is not available to wear today.")
    # print("Please select one of the following:")
    # print(clothing_items())
# color_picked = input("What color is it? ")

# https://www.makeschool.com/academy/track/standalone/captain-rainbow-s-color-checklist/helper-functions


# print("Is %s worn?") % worn_item
# worn_confirm = input(":")


# verify item worn - extra code commented out
# def confirm():
    # if worn_confirm == "yes" or "Yes" or "YES":
        # print("%s %s is worn.") % worn_color, worn_item
        # color_picked = color_picked.append(worn_color)
        # if worn_color == color_list:
            # print("You are done dressing. Have a FABULOUS day!")
        # else:
            # print("Select another clothing item to continue dressing: ")
    # else:
        # print("Please wear selected item.")


running = True
while running:
    selection = input("Press C to add to list, R to read from list, P to display list, or Q to quit")
    running = select(selection)
