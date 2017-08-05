class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "PARENT override()"

dad = Parent()
son = Child()

dad.override()
son.override()

# lpthw(master)[ 1 ] > python ex44b.py
# PARENT override()
# PARENT override()