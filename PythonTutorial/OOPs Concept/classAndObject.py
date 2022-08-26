# class MyClass:
#     """A simple example class"""
#     i = 12345  # Class Variable
#     def f(self):
#         return ('hello world')
#
# #creates a new instance of the class and assigns this object to the local variable x
# x = MyClass()


# class MyClass(object):
#     """A simple example class"""
#     i = 12345
#     def f(self):
#         return ('hello world')
#
# #creates a new instance of the class and assigns this object to the local variable x
# y = MyClass()

# class Test:
#     # Class Variable
#     a = None
#     b = None
#
#     def __init__(self, a):
#         print (self.a)  #doesn't find an instance variable and thus returns the class variable
#         self.a = a  # Local Variable
#         self._x = 123 # protected Variable
#         self.__y = 123 # private variables
#         b = 'meow' # Local Variable


# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#     def __init__(self, name, salary):
#          self.name = name
#          self.salary = salary
#          Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount
#     def displayEmployee(self):
#         print "Name : ", self.name, ", Salary: ", self.salary
#
# "This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print ("Total Employee %d" % Employee.empCount)
