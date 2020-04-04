# Chapter 1: Pythonic Thinking

Python runtimes? (Do we always use CPython? Is IPython a runtime?)

- protected and private instance members (see `encapsulation.py`)
- falsy values without checking len()
- relative imports with `from .package_name import asd`  
- import sections (separated with one blank line) are standard lib modules, third-party modules and own modules in alphabetical order

- Encoding and decoding (raw 8-bit values in bytes vs Unicode in str) - is this relevant in webdev?
- Helper functions are good
- List slicing results in a new list *with references in tact*, but modifying the result of slicing won't affect the original list

- List comprehensions: syntax for deriving one list from another (see `comprehensions.py`)
- Why use generator expressions: memory? List comprehensions keep the whole new list in-mem, meaning that large lists could use up way too much memory, leading to your program crashing
- Generator expressions: an iterator that yields one item at a time from the expression
- If you need a list item as well as it's index, use `enumerate()`
- Try-except-else-finally (what did that else do again...?)

Sidenote: package names should be all lowercase, short and if needed with underscores. Module names should be short and all lowercase, underscores are discouraged.
