class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# lpthw(master)[ 1 ] > python ex44a.py
# PARENT implicit()
# PARENT implicit()