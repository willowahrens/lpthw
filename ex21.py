def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d " % (a, b)
	return a / b


print "let's do  math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide (100, 2)

print "age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)



# print "here is a puzzle"

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print "that becomes: ", what, "can you do it by hand?"

# lpthw(master)[ 3 ] > python ex21.py
# let's do  math with just functions!
# ADDING 30 + 5
# SUBTRACTING 78 - 4
# MULTIPLYING 90 * 2
# DIVIDING 100 / 2
# age: 35, height: 74, weight: 180, iq: 50
# here is a puzzle
# DIVIDING 50 / 2
# MULTIPLYING 180 * 25
# SUBTRACTING 74 - 4500
# ADDING 35 + -4426
# that becomes:  -4391 can you do it by hand?


