class Cat:
    def __init__(self, name, owner, favorite_snack):
        self.name = name
        self.favorite_snack = favorite_snack
        self.owner = owner

    def meow(self):
        print("MEOOOOW")

    # Protected instance member, only accessible from withing the class or any subclasses
    # HOX: this is only BY CONVENTION following the single underscore in the name
    def _change_owner(self, new_owner):
        self.owner = new_owner
        return f"{new_owner} has been set as owner"

    # Private instance member
    def __change_favorite_snack(self, new_favorite_snack):
        self.favorite_snack = new_favorite_snack
        return f"{new_favorite_snack} has been set as fav snack"


john = Cat("John", "Maikki", "tunafish")

# PyCharm warns against this!
john._change_owner("niina")

# Results in AttributeError: 'Cat' object has no attribute '__change_favourite_snack'
# john.__change_favourite_snack("ham")


