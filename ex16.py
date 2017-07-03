from sys import argv

script, filename = argv

print "we're going to erase %r." % filename
print "if you dont want that, hit CTRL-C (^C)."
print "if you do want that, hit RETURN."

raw_input ("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating the file.  Goodbye!"
target.truncate()

print "now im going to ask you for three lines."

line1 = raw_input("line 1: why")
line2 = raw_input("line 2: how")
line3 = raw_input("line 3: who")

print "im going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it."
target.close()



# lpthw(master) > python ex16.py ex15_sample.txt
# we're going to erase 'ex15_sample.txt'.
# if you dont want that, hit CTRL-C (^C).
# if you do want that, hit RETURN.
# ?
# opening the file...
# truncating the file.  Goodbye!
# now im going to ask you for three lines.
# line 1: why
# line 2: how
# line 3: who
# im going to write these to the file
# and finally, we close it.