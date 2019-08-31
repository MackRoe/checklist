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
#len(checklist)

def list_all_items():
	index = 0
	for list_item in checklist:
#formats output and accommodates different data types
		print("{} {}".format(index, list_item))
		index += 1

#to mark as completed
def mark_completed(index):
	if item_worn = true:
		print ("√ {}".format(list_item))


def test():
	# Add your testing code here
	def verify_index(checklist):
		for x in checklist(x):
			if x > len(checklist):
				print ("Error! There aren't that many items in the list.")
			else:
				print (read(x))

	create("purple sox")
	create("red cloak")

	print(read(0))
	print(read(1))

	update(0, "purple socks")
	destroy(1)

	print(read(0))
	list_all_items()



test()


# not sure about this next bit here

print ("Good morning, Cpt Rainbow. It's time to get dressed.")
# GET WORN ITEMS
worn_item = input("What would you like to wear first?")
create(worn_item)

#stopped work at <h2> select </h2>
#https://www.makeschool.com/academy/track/standalone/captain-rainbow-s-color-checklist/helper-functions





