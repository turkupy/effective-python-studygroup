# Chapter 2: Functions

### What should functins return?
- Return values of functions: don't return `None` to signify a specific meaning
- Return values could be a tuple that signifies success status and result, i.e. `(True, 0.3)` or `(False, 0)`? Pros: you will know if it was successful, cons: you need to get the result out of the tuple
- Rather raise an exception if there could be situations in which the function is not successful + catch in caller
- Using type hints for params and return types? (see `typed.py`)

### "Functions are first-class objects"
- A first class object is an entity that can be dynamically created, destroyed, passed to a function, returned as a value, and have all the rights as other variables in the programming language have.
- Functions are first class objects in Python: can be stored in variables, passed as arguments and returned as return values of other functions (see `firstclassobjects.py`)

### Closures
- Inner can access outer, but not modify
- Attempted modification of out-of-scope variable leads to creation of a new variable instead (see `scopes.py`)
- One could use `nonlocal` to signify the outer scope, however, better pass as parameters to create a pure (simple) function instead?
- Side effects of `nonlocal` can be hard to follow...

### Using generators instead of returning lists
- Generators allow to keep only current iterator in memory => more efficient than keeping all values

### Be defensive when iterating over arguments multiple times
- Argument could be a list or some other iterable (maybe generator) and could thus be exhausted
- Being defensive: iterators can be exhausted (seen = gone)
- You can implement a custom iterable container class (any class implementing the `__iter__` method as a generator (it should `yield` the values one by one))
- This iterable container can then be used instead of the individual exhaustible iterators (calling `iter` on a container twice will not produce the same result)
- See `itering.py`

### Variable positional arguments
- `*my_param` (star args) can be used to signify a variable number of pos arguments
- Why this would be better than passing a list: you don't need to pass an empty list in case you don't want to pass in anything
- Should be a known number, not huge (since all in it will be converted to a tuple and held in mem)
- Would you use this..?

### Keyword args and default values
- Adds clarity
- Especially helpful with multiple 'flags'
- Adds optional params through default values
- If default value is dynamic (list, dict), use `None` instead
