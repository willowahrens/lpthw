
states = {
    'Oregan': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
    }


cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}


cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'


print '-' * 10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']


print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']


print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has ", cities[states['Florida']]


print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)


print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)


print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
			state, abbrev, cities[abbrev])

print '-' * 10

state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas"


city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city 





# lpthw(master)[ 1 ] > python ex39.py
# ----------
# NY State has: New York
# OR State has: Portland
# ----------
# Michigan's abbreviation is:  MI
# Florida's abbreviation is:  FL
# ----------
# Michigan has:  Detroit
# Florida has  Jacksonville
# ----------
# Florida is abbreviated FL
# Michigan is abbreviated MI
# New York is abbreviated NY
# Oregan is abbreviated OR
# California is abbreviated CA
# ----------
# FL has the city Jacksonville
# CA has the city San Francisco
# MI has the city Detroit
# OR has the city Portland
# NY has the city New York
# ----------
# Florida state is abbreviated FL and has city Jacksonville
# Michigan state is abbreviated MI and has city Detroit
# New York state is abbreviated NY and has city New York
# Oregan state is abbreviated OR and has city Portland
# California state is abbreviated CA and has city San Francisco
# ----------
# Sorry, no Texas
# The city for the state 'TX' is: Does Not Exist





