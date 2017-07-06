def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)



def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
		print "arg1: %r" % arg1


def print_none():
		print "i got nothin"


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none



# lpthw(master)[ 1 ] > python ex18.py
# arg1: 'Zed', arg2: 'Shaw'
# arg1: 'Zed', arg2: 'Shaw'
# arg1: 'First!'
# i got nothin