def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes_of_crackers!" % boxes_of_crackers
	print "man that's enough for a party!"
	print "get a blanket.\n"


print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use the variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "we can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



# lpthw(master)[ 1 ] > python ex19.py
# we can just give the function numbers directly:
# You have 20 cheeses!
# You have 30 boxes_of_crackers!
# man that's enough for a party!
# get a blanket.

# OR, we can use the variables from our script:
# You have 10 cheeses!
# You have 50 boxes_of_crackerss# man that's enough for a party!
# get a blanket.

# we can even do math inside too:
# You have 30 cheeses!
# You have 11 boxes_of_crackers!
# man that's enough for a party!
# get a blanket.

# and we can combine the two, variables and math:
# You have 110 cheeses!
# You have 1050 boxes_of_crackers!
# man that's enough for a party!
# get a blanket.