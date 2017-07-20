from sys import exit

def gold_room():
	print "This room if full of silver, how much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("That's not very nice.")
	if how_much < 100:
		print "You're very selfless, yay! You win!"
		exit(0)
	else:
		dead("You're selfish, you LOSE!")



def snake_room():
	print "There is a snake here... uh oh."
	print "The snake has very large fangs."
	print "The snake slithers to a different door."
	print "How do you move the snake?"
	snake_moved = False

	while True:
		next = raw_input("< ")

		if next == "Rip his fangs out.":
			dead("The snake sees you and bites you with its venomous fangs. You die.")
		elif next == "taunt snake" and not snake_moved:
			print "The snake has slithered away from your door, you may enter."
			snake_moved = True
		elif next == "taunt snake" and snake_moved:
			dead("The snake opens its wide mouth and squints his eyes, he's pissed.")
		elif next == "open door" and snake_moved:
			gold_room()
		else:
			print "Wait.... whuuut?"


def mouse_room():
	print "Here you see the evil mouse."
	print "He prances to you, and stares. You start going insane."
	print "Do you run to save yourself or will you battle this evil mouse?"

	next = raw_input("> ")

	if "run" in next:
		start()
	elif "battle" in next:
		dead("You win!")
	else:
		mouse_room()


def dead(why):
	print why, "GOOD JOB!!!"
	exit(0)

def start():
	print "You are in a poorly lit room."
	print "There are two doors, one to your left and one to your right."
	print "Which one do you choose?"

	next = raw_input("> ")

	if next == "left":
		snake_room()
	elif next == "right":
		mouse_room()
	else:
		dead("You look around the room and realize you'll die from starvation.")


start()

# lpthw(master)[ 1 ] > python ex36.py
# You are in a poorly lit room.
# There are two doors, one to your left and one to your right.
# Which one do you choose?
# > left
# There is a snake here... uh oh.
# The snake has very large fangs.
# The snake slithers to a different door.
# How do you move the snake?
# < taunt snake
# The snake has slithered away from your door, you may enter.
# < open door
# This room if full of silver, how much do you take?
# > all of it
# That's not very nice. GOOD JOB!!!


# lpthw(master)[ 1 ] > python ex36.py
# You are in a poorly lit room.
# There are two doors, one to your left and one to your right.
# Which one do you choose?
# > right
# Here you see the evil mouse.
# He prances to you, and stares. You start going insane.
# Do you run to save yourself or will you battle this evil mouse?
# > battle
# You win! GOOD JOB!!!