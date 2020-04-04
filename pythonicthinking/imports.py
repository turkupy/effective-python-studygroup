# Relative import
from .encapsulation import Cat

# Relative import - other module (file) of the same package (folder)
from . import encapsulation

# Absolute import from package "pythonicthinking" (best practice)
from pythonicthinking.encapsulation import Cat

maikken = Cat("Maikken", "Jussi", "nakki")
