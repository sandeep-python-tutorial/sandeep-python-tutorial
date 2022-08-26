### Multiprocessing
trying to improve the performance of CPU-bound tasks

### Multithreading
If particular task is Input/Output bound, 
then we use multithreading to improve the performance of your applications.

### Pool

when it comes to longer running applications, 
it is better to create a pool of longer running processes. 
This avoids having to create and destroy a process every time 
you have a new task to execute and can subsequently improve the performance of your applications.

### Queues
Queue objects are a FIFO data structure that are thread and process safe which make them perfect for passing data between different processes without potentially corrupting data. 

### Process class
In multiprocessing, processes are spawned by creating a **Process object** and then calling its **start()** method.
Process follows the API of threading.Thread.

### Pipe
The two connection objects returned by Pipe() represent the two ends of the pipe. Each connection object has
send() and recv() methods (among others). Note that data in a pipe may become corrupted if two processes
(or threads) try to read from or write to the same end of the pipe at the same time.

### Locks
When we want that only one process is executed at a time in that situation Locks is use. That means that time blocks other process from executing similar code. Lock will be released after the process gets completed.