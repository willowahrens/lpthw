class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "Child override()"

    def altered(self):
        print "CHILD BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD AFTER PARENT altered()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# lpthw(master)[ 3 ] > python ex44d.py
# PARENT implicit()
# PARENT implicit()
# PARENT override()
# Child override()
# PARENT altered()
# CHILD BEFORE PARENT altered()
# PARENT altered()
# CHILD AFTER PARENT altered()