from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)

print "does the output file exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "alright, all done"

out_file.close()
in_file.close()

# lpthw(master)[ 1 ] > python ex17.py ex15_sample.txt test.txt
# Copying from ex15_sample.txt to test.txt
# the input file is 7 bytes long
# does the output file exist? True
# ready, hit RETURN to continue, CTRL-C to abort

# alright, all done