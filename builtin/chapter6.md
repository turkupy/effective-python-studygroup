# Chapter 6: Built-in Modules
The Python standard library is "batteries included": it contains many important modules for common use of the language.

### Function wrappers with `functools.wraps`
- Decorators: run code before and after the wrapped function is ran
```
def trace(func): 
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) # Log every time a function is called
        print(‘%s(%r, %r) -> %r’ % (func.__name__, args, kwargs, result))
        return result
    return wrapper

# This can now be used as a decorator:
@trace
def fibonacci...
```
- Use the `@wraps` decorator to write your own decorators, it copies all the metadata from your inner function to the outer one so that you can access the decorated function (fibonacci) as usual even though it is wrapped in a decorator

### Reusable `try/finally` behaviour with `contextlibs` `with`-statement
- For example 
```
lock = Lock()
with lock: 
    ...
```
is actually the equivalent of 
```
lock.acquire()
try:
    print(‘Lock is held’)
finally:
    lock.release()
```
- Also use with when working with files: to avoid manually opening and closing them
- Likewise, avoid manually setting and resetting a log level by using `with loglevel.INFO`
- You can create a settable logger by using the `contextmanager` decorator to define a logger that fetches the logger and then sets the log level

### Pickle is fickle without `copyreg`
- Pickle is a module for serializing Python objects into streams of bytes
- Pickle can be used to construct malicious payloads (contains instructions on how to reconstruct the original Python object), contra to the safer `json` serializer (only contains a description of object hierarchy)
- Serializing objects between trusted programs, pickle comes in handy
- Copyreg can add missing attribute values, allow versioning of classes and provide stable import paths (more control over the unpickling process)

### Use datetime instead of time for local clocks
- Previously the `time` module has been the de facto way to go about time in python, but has now been triumphed by the community-built `pytz / datetime` module
- Datetime allows conversion to local time
- Also conversions between local times
```
eastern = pytz.timezone(‘US/Eastern’)
nyc_dt = eastern.localize(nyc_dt_naive)
```

### Use built-in algorithms and data structures
TLDR; don't write these yourself, since they are hard to do right

- With large amounts of data, programs start slowing down due to algorithmic complexity
- `dequeue` - double-ended queue is ideal for FIFO queues much faster than adding and removing to a list:
```
fifo = deque()
fifo.append(1) # Producer
x = fifo.popleft() # Consumer
```
- `ordereddict` is a dict that keeps track of key insertion order, giving iterating over the keys a predictable behaviour
- `defaultdict` is a dict that gives a default value when a key doesn't exist
```
stats = defaultdict(int) # Return 0 whenever a number doesn't exist
stats[‘my_counter’] += 1
```
- `heapq` gives tools to push, pop etc. The heap is always popped starting with the lowest value (lowest prio)
- Heap manipulation takes a logarithmic time, contra list manipulations linear time
- `bisect` provides efficient binary search (logarithmic, ie. 1 million searches in the same time as 14 linear searches)
- `itertools` contains tools to link, filter and combine 

### Use `decimal` when precision is paramount 
- Also, use it's `quantize` method and a specific `rounding`
- Limitation: If dealing with fractions that should have no approximations, use `Fraction` instead of decimal

### Where to find community-built modules
- https://pypi.org/ and use pip for this
- Use the correct version of pip 
- Installed by default in Python 3.4, in older versions you must install it yourself

