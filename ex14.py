from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me,
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)


# lpthw(master)[ 1 ] > python ex14.py willow
# Hi willow, I'm the ex14.py script.
# I'd like to ask you a few questions.
# Do you like me willow?
# > sure
# Where do you live willow?
# > fayetteville
# What kind of computer do you have?
# > mac

# Alright, so you said 'sure' about liking me,
# You live in 'fayetteville'. Not sure where that is.
# And you have a 'mac' computer. Nice.
