class Dog:
    def __init__(self, name, snacks):
        self._name = name
        self.snacks = snacks

    # Property is accessed through this method with the property decorator
    @property
    def name(self):
        return self._name

    # Defines a setter that is called when name is set
    @name.setter
    def name(self, new_name):
        # Check that the one renaming is the dogs owner and that the name is a proper name!
        print('Okay validating really hard here!')
        self._name = new_name


maikki = Dog('Maikki', 'pig ears')
maikki.name = 'Maiksu'
print(maikki.name)