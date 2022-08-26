#Syntax:
'''class derived-class(base class):
    <class-suite>

class derive-class(<base class 1>, <base class 2>, ..... <base class n>):
    <class - suite>
'''

#Inharitence of class
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b;
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b;
# d = Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))

# issubclass method
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b;
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b;
# d = Derived()
# print(issubclass(Derived,Calculation2))
# print(issubclass(Calculation1,Calculation2))


#isinstance method
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b;
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b;
# d = Derived()
# print(isinstance(d,Derived))


#Method Overidding
# class Animal:
#     def speak(self):
#         print("speaking")
# class Dog(Animal):
#     def speak(self):
#         print("Barking")
# d = Dog()
# d.speak()


# Method Overloading
# # First product method.
# # Takes two argument and print their
# # product
# def product(a, b):
#     p = a * b
#     print(p)
#
#
# # Second product method
# # Takes three argument and print their
# # product
# def product(a, b, c):
#     p = a * b * c
#     print(p)
#
#
# # Uncommenting the below line shows an error
# # product(4, 5)
#
# # This line will call the second product method
# product(4, 5, 5)