# Chapter 7: Collaboration
- There are some best practices to making maintainable code, and those practices vary across programming languages

## Docstrings for functions, classes and modules
- You can then see the docs by using the `help` builtin function
- This standard documentation way makes it easier to use docs tools like [Sphinx](https://www.sphinx-doc.org/en/master/) (auto-generate documentation) 

- Modules: have a top-level docstring that intros the module and it's contents (available functions, etc..)
- Classes: have a docstring at the beginning of a class definition that lists it's public attributes, maybe also describing how to create subclasses
- Functions: description, args and returns, possible raised exceptions, yielded values...

- Use `doctest` buildin module to test that your docs are up to date! 

## Use packages to organize modules
- So that the folder exports things using an `__init__.py` file that looks like:
```
from .cucumber import Cucumber
```
- A package is a module that contains other modules
- The `__all__` special attribute can be used to define which parts of the module are exported: `__all__ = ['simulate_collision']`

## Define a root exception for your module
- Then it's easier to tell if the exception was raised on purpose by your code (was this the correct way to use this API)
```
except my_module.Error as e: 
    logging.error(‘Bug in the calling code: %s’, e)
except Exception as e:
    logging.error(‘Bug in the API code: %s’, e)
```

## Circular dependencies
- Use dynamic imports: import at the beginning of a method/function (so the import happens when the code is running, not when the modules are being initialized)
- But don't do this in loops, it does have a performance impact

## Virtual environments
- Do start by activating a virtualenv and then installing the needful
```
python3 -m venv venv
source venv/bin/activate
deactivate
```
- A requirements.txt file helps in reproing what you need `pip install -r requirements.txt`
- Also, `requirements.in` and maybe `requirements-dev.txt`?

