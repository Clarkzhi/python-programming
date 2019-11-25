#Inside this file define, a class called Movie The movie class should assign a title, genre, and running_time when initialized. The movie class also has a cast variable, which is an empty list initially.


class Moive:
    def __init__(self, t, g, r):
        self.title = t
        self.genre = g
        self.running_time = r
        self.moive = []

m = Moive('Batman', 'action', 140)
#Write an add_cast method to add an actor to the movie’s cast
    def add_cast(self, actor):
        new_moive = []
        new_moive['actor'] = actor
        self.moive.append(new_moive)
       
#write a method describe that prints the movie’s title, genre, running time and all its cast members

m1.add_cast('C')
print(m1.moive)
#Write a method called compare_to which compares one movie to another.This method accepts a movie object and compares it to the current movieobject. If the two movies have less than two actors in common, the method must return -1, otherwise it returns 1.
