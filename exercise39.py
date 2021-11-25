# Dictionaries 
# Dictionaries are another example of a data structure.
'''things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'b'
print(things[1])

person = {'name': 'John', 'age': 40, 'height': 4*7}
print(person['name'])

person.pop('age') '''

#Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Print out some cities
print('-' * 10)
print("NY State has: ",cities['NY'])
print("OR State has:", cities['OR'])

#Print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#Do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviations
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#Nov do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    print('-' * 10)

# Safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")