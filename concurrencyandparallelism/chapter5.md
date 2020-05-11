# Chapter 5: Concurrency and Parallelism

- Concurrent: one CPU, seemingly many processes
- Parallel: many CPUs, actually many processes (speed up!)

### Use subprocess to manage child processes
- The `subprocess` built-in module contains the de facto tools for managing child processes in modern python
- Child processes run independently of the parent (python processor) and can be polled periodically, as in 
```py
proc = subprocess.Popen([‘sleep’, ‘0.3’])
while proc.poll() is None:
    print(‘Working…’)
    # Some time-consuming work here
    # …
print(‘Exit status’, proc.poll())
```
- This module also contains tools for managing the input and output streams for the child process
- Since python 3.3, `process.communicate(timeout=0.1)` has been available to set a timeout for child processes in case they are stuck hanging
- Real world use cases: running other stuff on that computer, maybe git, ffmpeg [see example by @akx](https://github.com/akx/gifify/blob/93f2cc796a81775331543a22b557d95e40bdeb5e/gifify.py)

### Use threads for blocking I/O
- CPython works by 1. Parse and compile source to byte code 2. Run that bytecode on a stack-based interpreter 
- CPython interpreter can be viewed as a stack-based (as opposed to registry-based) virtual machine. This means that python code is compiled for an imaginary or a virtual computer with a stack architecture.
- This is supervised by the GIL (global interpreter lock) which prevents CPython from pre-emptive (os controlled) multithreading so that the the interpretor state stays in tact
- The GIL, preventing multiple threads from executing Python bytecode at once, is needed because CPython memory management is not thread safe 
- The negative side of GIL is that (other than C# or Java), Python cannot actually have multiple threads on multiple CPUs, but instead only one process makes progress at a time
- Hence, threading with the standard CPython interpreter will not speed up the program
- So what is threading good for? Fairness between the processes, doing multiple things at the seemingly same time
- Also threading makes it possible to do blocking io and computation at the same time

#### Sidenote, asyncio vs threading?
- For I/O, using asyncio vs threading (asyncio is preferred)
- Asyncio is a single thread with a coordinator that coordinates the order of things
- Asyncio gives more control of the priority of tasks

### Use lock to prevent data races in threads
- Same objects should not be accessed from multiple threads simultaneously: the GIL won't be making sure things are kept in tact
- Use `with self.lock: # do stuff` when mutating stuff, otherwise multiple threads might be modifying the same object at the time, causing data races
- `threading.Lock` is Pythons standard mutual exclusive lock implementation

### Use Queue to coordinate work between threads
- In threading you need to use synchronization primitives (such as locks) to manage the shared data (same memory space)
- `Queue` contains all needed locking semantics and helps to share data between threads
- Queue also runs stuff sequentially
- Queues are lists that contain tasks to be preformed serially
- In producer-consumer (a pipe, one thread outputs what the next thread will need) thread situations (reader and writer?) you might heed to use queue 

### Consider coroutines to run many functions simultaneously
- The con of threading is the complexity and uneasiness of maintainance it introduces to the code
- Threads require a lot of memory (~8 MB per thread) => a dozen or so is fine, but thousands of threads is just a bad idea
- Also, in threads the main cost is starting them. 
- Coroutines: many seemingly simultaneous functions
- Coroutines as per Brett: the code consuming a generator can `send` a value back into the generator after a yield expression
- These are also known as simple coroutines (as opposed to native (async) coroutines)

```
while True:
    bla = yield # This coroutine will stop here? Each time .send() is called
    print('hello')
```
- In this way the code consuming the generator can take action after each yield expression in the coroutine
- See `coroutines.py`

### Concurrent.futures for TRUE PARALLELISM!
- Hitting an optimization wall: writing code into C modules and "getting closer to the metal" might help?
- `multiprocessing` is a built-in module allows to run additional interpreters as child processes
- Child processes are hence controlled by separate GILs and can fully utilize their own CPUs 
- `ProcessPoolExecutor`: serialize into binary, copy to a child process, run, serialize the results and copy them back via a socket, deserialize back into parent process
- All this serializing and deseralizing is heavy work: multiprocessing is best suited for cases where computation is heavy and serialized data relatively small
- Heavy inter-process communication => cannot multiprocess, prefer threading/asyncio
```
pool = ProcessPoolExecutor(max_workers=2) # pool w 2 cpus
```  

More reads:  
https://realpython.com/python-concurrency/  
https://realpython.com/intro-to-python-threading/  
https://dev.to/codemouse92/dead-simple-python-generators-and-coroutines-21ll  





