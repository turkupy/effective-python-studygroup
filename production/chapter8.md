# Chapter 8: Production

Pythonic practices for shifting from a development to production environment and making them bullet proof.

## Module-scoped code to configure envs
- Use some tool to know which packages and versions the different environments have (such as venv)
- Having different __main__ files for dev and prod might be a good way to make sure the different setups required by the different envs end up right
- ...and then using env variables to tell which db to connect to, etc.

## Types matter when printing
- `print(repr('5'))` keeps the type in tact unlike vanilla print, as it prints an actual representation of the value
- For your own classes, you can define `__repr__` methods which define a representation for printing
- You can also use the classes `obj.__dict__` method to print out the contents of a class

## Unittest
- Use the `unittest` builtin module to define tests
- For example the issues which could be raised by static typing could in python be checked by unit tests
- Use the module by having a class inherit `TestCase` and contain methods named `test_...`

## Interactive debugging with `pdb`
- To initiate the pdb interactive debugger, import it and call `pdb.set_trace()`
- This gives you a debugger prompt
- You can then inspect and modify the running program

## Profile before optimizing
- Python has a two builtin profilers: `profile` and `cProfile`
```
profiler = Profile()
profiler.runcall(test) # Run test()

stats = Stats(profiler) # Use stats to print out some cool stats!
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
```
- Out of these two profilers, cProfile should be preferred since it is lighter and will not skew the results like the pure python profiler might

## Using `tracemalloc` trace memory allocations for looking at memory leaks
- CPython uses reference counting: once all references have expired, the object is cleared
- There is also functionality for identifying and garbage collecting circular references
- Most memory management is taken care of by the CPython runtime in this way
- You can debug memory issues using the `gc.get_objects()` builtin, which will let you know which objects have been garbage collected at a given time
- Whereas `gc.get_objects()` won't tell you how objects were allocated, `tracemalloc.take_snapshot()` will

TLDR; 
- `gc` can tell you what exists
- `tracemalloc` can tell you the source of memory usage (how many KiB on each line of the program)








