people = 40
cars = 15
buses = 15


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people >buses:
	print "Alright, let's just take the buses."
else:
	print "fine, let's stay home then."


# 	lpthw(master)[ 2 ] > python ex30.py
# We should take the cars.
# Maybe we could take the buses.
# Alright, let's just take the buses.