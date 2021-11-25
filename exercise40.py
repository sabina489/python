# Modules, Classes and Object
# Modules are like Dictionaries
#mystuff = {'apple': "I like apple"}
# print(mystuff['apple'])


# Classes are like modules
# A class is a way to take a grouping of functions and data and place them inside a container so we can access them with the .(dot) operator

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics  # inside the function in a class, self is a variable for the object being accessed.
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_birthday = Song(["Happy birthday to you",])
bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])
person = Song(["His name is ram",])

happy_birthday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
person.sing_me_a_song()

    