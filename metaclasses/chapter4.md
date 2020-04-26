# Chapter 4: Metaclasses and attributes

## Short note before we begin...
- Metaprogramming = a program having knowledge of itself (implemented in python as metaclasses)
- Essentially metaclasses are 99% black magic that should rarely be used
- In python 3, an objects type is it's class: previously this wasn't so
- An instance's type is the class instantiated, but the type of the class itself is "type" `type(type)` returns `<class 'type'>`
- Type is one of Pythons metaclasses

### Use plain attributes instead of getters and setters
- Coming from for example Java, one might be tempted to create encapsulation by using getters and setters
- Getters and setters are "not Pythonic" => for example incrementing is much cleaner when one just has public attributes
See `setters.py`
- If special behaviour on access and update is needed, use the @property decorator + @name.setter

### Use @property for refactoring (but use common sense)
- Sometimes using the special functionality provided by property can make a neater solution than layering the logic elsewhere
- Also a nice incremental embetterment tool?

### Descriptors and reusable @property methods
- Issue with @property is that those methods cannot be reused
- Use descriptors (classes that implement `__get__`, `__set__` or `__delete__`) for reusable functionality

### Using `__getattr__`, `__setattr__`...
- Called every time an attribute is accessed and it cannot be found in the objects instance dictionary
- "Load only on access"
- Similarly-ish, `__getattribute__` is a method that is called always when an attribute of an object is accessed
- Use `hasattr` to check if an attribute exists (`AttributeError` is raised when accessing an attribute that doesn't exist)
- `setattr` is always called when setting attrib values, this can be used for example when logging
- "Lazy loading" implementation: use `setattr` inside `getattr` to set it only when it's accessed
- Avoid infinite recursion in `getattribute` and `setattr` by using the object class `super` 

### Validate subclasses with metaclasses
- Define a metaclass by inheriting from `type`
- `__new__` recieves contents of the associated class when it is defined (not when it is instantiated)
- See metavalidation.py 
