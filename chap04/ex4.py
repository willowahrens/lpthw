cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "there are", cars, "cars available"
print "there are only", drivers, "drivers available"
print "there will be", cars_not_driven, "empty cars today"
print "we can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "we need to put about", average_passengers_per_car, "in each car"



# chap04(master)[ 1 ] > python ex4.py
# there are 100 cars available
# there are only 30 drivers available
# there will be 70 empty cars today
# we can transport 120.0 people today
# We have 90 to carpool today
# we need to put about 3 in each cars