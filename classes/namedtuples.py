import collections

# Create a "miniclass"
Name = collections.namedtuple('Name', ('first_name', 'last_name'))

# Create an instance of it
nina = Name('Nina', 'Mäki')

print(nina.first_name, nina.last_name, type(nina))