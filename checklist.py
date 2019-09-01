
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
        print(("{} {}").format(index, list_item))
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
        # potential crash warning item_index
    # print all items
        read(int(item_index))
    elif function_code == "P":
        list_all_items()
    else:
        print("Unknown Option")


def test():
    # Add your testing code here
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


color_list = ["red", "purple", "blue", "green", "yellow", "orange"]
clothing_items = ["pants", "shirt", "jacket", "hat", "socks", "shoes"]

# test()


# experimental learning exercize code

print("Good morning, Cpt Rainbow. It's time to get dressed.")
# GET WORN ITEMS
worn_item = input("What would you like to wear first?")
create(worn_item)
worn_color = ("What color is it? ")

# stopped work at <h2> select </h2>

# https://www.makeschool.com/academy/track/standalone/captain-rainbow-s-color-checklist/helper-functions


print("Is %s worn?") % worn_item
worn_confirm = input(":")


# verify item worn
def confirm():
    if worn_confirm == "yes" or "Yes" or "YES":
        print("%s %s is worn.") % worn_color, worn_item
        color_picked = color_picked.append(worn_color)
        if worn_color == color_list:
            print("You are done dressing. Have a FABULOUS day!")
