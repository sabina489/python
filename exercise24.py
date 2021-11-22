#More practise of Strings, Bytes and Character Encoding

print("Let's practice everything.")
print('You need to know about escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """ The lovely world
7 with logic so firmly planted
8 cannot discern \n the needs of love
9 nor comprehend passion from intuition
10 and requires an explanation
11 \n\t\twhere there is none."""

print("--------")
print(poem)
print("------")

five = 5 - 3 + 3 - 1
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

#Another way to format a string
print("With a starting point of: {}". format(start_point))

#Its just like with an f""" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

#This is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
