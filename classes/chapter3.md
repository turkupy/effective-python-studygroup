# Chapter 3: Classes and inheritance 

### Knowing when to use classes instead of dicts
- When stuff starts feeling complex, it's time to refactor (dicts inside dicts etc.)
- Refactoring is easiest started at the bottom of the dependency tree (details first)
- Namedtuple can in some cases be used as a lightweight data container instead of a full class (see example in `namedtuples.py`)

### Using functions instead of classes for simple interfaces
- Use hooks (for example `key` in sort) as functions
- Example used a function to override the `__missing__()` function of defaultdict (https://docs.python.org/2/library/collections.html#defaultdict-objects)
- Stateful functions in hooks (harder to read than stateless) => maybe use `__call_`
- Using `__call__` to allow an object to be called like a function

### Use @classmethod to have "multiple constructors"
- Polymorphism: multiple classes in a hierarchy implement unique versions of a method
- Example uses mapreduce: 1. map (same computation across all data items at same time) 2. reduce (takes maps result and reduces it to a single value)
- So you would have a base class with `NotImplementedError` raised for the methods that the subclasses must implement
- Python only allows for a single ctor method (`init`) contra for example C#, that allows constructor overloading (multiple param combinations)
--> This leads to the trouble of having to have all those params in all subclasses!
- A class method (`@classmethod`) is bound to a class rather than to an object. (See `classmethods.py`.)

### Initialize parent classes with `super`
- Python allows for multiple inheritance: in this case, the order in which the init functions are run is not clear
- "Diamond inheritance" causes the "grandparent" classes ctor to run multiple times
- Python 2.2 added the `super` built-in function => solves these challenges by defining a MRO (method resolution order)
- You can find the mro in `MyClass.mro()`
- You only call super instead of calling all the inits of the inherited classes

### Use multiple inheritance only in mixins
- Mixin: small class that defines a set of additional methods which a class should provide
- Mixins don't define their own instance attributes and don't require calling init
- See also https://www.ianlewis.org/en/mixins-and-python

### Prefer public attributes
- Private attributes make it hard to override and access them in subclasses => prefer protected ones instead
- Document the classes to guide subclasses instead

### Inheriting from `collections.abc` for custom container types
- Built-in container types are: list, tuple, dict, set
- For simple use cases, inherit from these built-in container types
- To correctly implement custom container types, a large nr of methods is required...
- Inherit `collections.abc` to make sure your classes match required interfaces and behaviors => test whether it is hashable, mappable etc.
- See https://docs.python.org/3/library/collections.abc.html for more info


