from sys import argv

script, filename = argv

txt = open(filename)

print "Here's youre file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()


# lpthw(master)[ 1 ] > python ex15.py ex15_sample.txt
# Here's youre file 'ex15_sample.txt':
# This is stuff I typed into a file.
# It's not too cool.
# Where's the fun at.

# Type the filename again:
# > ex15_sample.txt
# This is stuff I typed into a file.
# It's not too cool.
# Where's the fun at.