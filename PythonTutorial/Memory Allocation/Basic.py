# #1.Simple Variable Memory Allocation with reference count
#
# x = 10
# print(id(x))
##When x = 10 is executed an integer object 10 is created in memory and its reference is assigned to variable x, this is because everything is object in Python.

#-----------------------------------------------------------------------------------

# #2.Two different Varibale but same Value:
# x = 10
# y = x
#
# if id(x) == id(y):
#     print("x and y refer to the same object")
#
# #x and y refer to the same object
# #In the above example,
# # y = x will create another reference variable y which will refer to the same object because
# # Python optimizes memory utilization by allocation the same object reference to a new variable
# # if the object already exists with the same value.

#-----------------------------------------------------------------------------------

# #3.Let’s change the value of x and see what happens.
# x = 10
# y = x
# x += 1
#
# if id(x) != id(y):
#     print("x and y do not refer to the same object")
#
# #x and y do not refer to the same object
# #So now x refer to a new object x and the link between x and 10 disconnected but y still refer to 10.

#-----------------------------------------------------------------------------------


##Memory Allocation
#Stack and Heap


# #Work of Stack Memory
# def func():
#     # All these variables get memory
#     # allocated on stack
#     a = 20
#     b = []
#     c = ""

#-----------------------------------------------------------------------------------


# #Work of Heap Memory
# # This memory for 10 integers
# # is allocated on heap.
# a = [0]*10

#-----------------------------------------------------------------------------------


#Garbage Collection Thresold
# # loading gc
# import gc
#
# # get the current collection
# # thresholds as a tuple
# print("Garbage collection thresholds:",
#       gc.get_threshold())
# #This means when the number of allocations vs. the number of deallocations is greater than 700
# # the automatic garbage collector will run.

#-----------------------------------------------------------------------------------

#Manual Garbage Collection

# # Importing gc module
# import gc
#
# # Returns the number of
# # objects it has collected
# # and deallocated
# collected = gc.collect()
#
# # Prints Garbage collector
# # as 0 object
# print("Garbage collector: collected",
#       "%d objects." % collected)
