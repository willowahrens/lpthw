x = "there are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" % (binary, do_not)

print x
print y

print "i said: %r." % x
print "i also said: '%s'." % y

hilarious = Fsalse
joke_evaluation = "isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "this is the left side of..."
e = "a string with a right side"

print w + e


# chap06(master)[ 2 ] > python ex6.py
# there are 10 types of people
# those who know binary and those who don't
# i said: 'there are 10 types of people'.
# i also said: 'those who know binary and those who don't'.
# isn't that joke so funny?! False
# this is the left side of...a string with a right side