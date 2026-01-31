# {
#     "name": 'zaius',
#     "breed": 'australian shep',
#     "tricks": ['sit', 'down'],
#     "available": True
# }

# class Puppy:
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []
#
#
# elton = Puppy("dog")
# print(elton.name)
# 'zaius'
# elton.tricks
# []

class Dog:
    def __init__(self, name, breed, location):
        # SELF is just the variable of the OBJECT we created
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    def bark(self):
        print(f'{self.name} says WOOF')

    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

otter = Dog("Otter", "Huskey", 94921)
# OTTER is SELF
print(otter.name)
print(otter.breed)
print(otter.location)



jules = Dog("Jules", "Corgi", 10254)
# JULES is SELF
print(jules.name)
print(jules.breed)
print(jules.location)

print("*" *50)

tina = Dog("Tina", "mutt", 56824)
tina.bark()

print("*" *50)

Bru = Dog('Bruno', 'greyhound', 21368)
Bru.learn_trick('sit')
tr = Bru.tricks
print(tr)

Bru.tricks.append('spit')
# this added SPIT to the tricks of BRU
tri = Bru.tricks
print(tri)