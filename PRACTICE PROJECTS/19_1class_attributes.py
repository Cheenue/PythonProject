class Puppy:
    # This is a Class Attribute (shared by ALL puppies)
    species = 'canine'

    def __init__(self, name):
        # These are Instance Attributes (unique to EACH puppy)
        self.name = name
        self.tricks = []


# METHODS

class Puppy:
    species = 'canine' # Class Attribute

    @classmethod
    # This is a decorator
    def register_anon(cls):
        # cls here is the Puppy class itself
        # This returns a new Puppy named 'unknown'
        return cls('unknown')

    def __init__(self, name):
        self.name = name
        self.tricks = []