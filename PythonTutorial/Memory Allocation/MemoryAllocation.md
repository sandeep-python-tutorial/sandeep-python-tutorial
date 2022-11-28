## Memory Management In python
Memory management handle by Python Manager. Python Manager can handle two types of memory:

     1. Memory Allocation
     2. Memory De-Allocation

### Memory Allocation
Whenever any variable, class or method created python create memory for theam.
There are two types of memory allocation:
1. Static Memory Allocation
2. Dynamic Memory Allocation

**Static Memory Allocation**

Static memory allocation happens at the compiled time. Python Manager create a **Stack Allocation** .

It is the memory that is only needed inside a particular function or method call. When a function is called, it is added onto the program’s call stack. Any local memory assignments such as variable initializations inside the particular functions are stored temporarily on the function call stack, where it is deleted once the function returns, and the call stack moves on to the next task. This allocation onto a contiguous block of memory is handled by the compiler using predefined routines.

<code>
    def func():

        # All these variables get memory  
        # allocated on stack  
        a = 20
        b = [] 
        c = "" 
</code>

**Dynamic Memory Allocation**

Dynamic memory allocates the memory at the runtime to the program and memory allocation called **Heap Allocation**

The memory is allocated during the execution of instructions written by programmers. Note that the name heap has nothing to do with the heap data structure. It is called heap because it is a pile of memory space available to programmers to allocated and de-allocate. The variables are needed outside of method or function calls or are shared within multiple functions globally are stored in Heap memory.

<code>

    # This memory for 10 integers
    # is allocated on heap.
    a = [0]*10 
</code>


### Memory De-Allocation
In Python memory allocation and deallocation method is automatic as the Python developers created a garbage collector for Python so that the user does not have to do manual garbage collection.

**Garbage Collection** - Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.

Method of Garbage Collector:
1. Reference Counting
2. Automatic Garbage Collection of Cycles
3. Manual Garbage Collection

**Reference Counting**

Reference counting works by counting the number of times an object is referenced by other objects in the system. When references to an object are removed, the reference count for an object is decremented. When the reference count becomes zero, the object is deallocated.

**Automatic Garbage Collection of Cycles**

Because reference cycles take computational work to discover, garbage collection must be a scheduled activity. Python schedules garbage collection based upon a threshold of object allocations and object deallocations. When the number of allocations minus the number of deallocations is greater than the threshold number, the garbage collector is run. One can inspect the threshold for new objects (objects in Python known as generation 0 objects) by importing the gc module and asking for garbage collection thresholds: 

**Manual Garbage Collection**

Invoking the garbage collector manually during the execution of a program can be a good idea on how to handle memory being consumed by reference cycles. 

There are two ways for performing manual garbage collection: 
1. time-based garbage collection.
2. event-based garbage collection.

**time-based garbage collection** the garbage collector is called after a fixed time interval. 

**event-based garbage collection** calls the garbage collector on event occurrence. For example, when a user exits the application or when the application enters into idle state.

### Common Ways to Reduce the Space Complexity
1. Avoid List Slicing
2. Use List Indexing Carefully: "for item in array" instead of "for index in range(len(array))" 
3. String Concatenation: imutable, instead of '+' use .join() or .formate()
4. Use Iterators and Generators
5. Use the Built-in Library when Possible