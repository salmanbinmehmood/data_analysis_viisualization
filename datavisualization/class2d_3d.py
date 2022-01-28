# class vector2d:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def __str__(self):
#         return f'{self.i} + {self.j}'
# class vector3d(vector2d):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def __str__(self):
#         return f'{self.i} + {self.j} + {self.k}'
# v2d=vector2d(2,3)
# v3d=vector3d(3,5,7)
# # print(v2d)
# print(v3d)

# class Animal:
#     def __init__(self):
#
#         print('im an Animal')
# class pet(Animal):
#     def __init__(self):
#         super().__init__()
#
#         print('In a Pet')
# class Dog(pet):
#     def __init__(self):
#
#         super().__init__()
#         print('im a dog')
#     def bark(self):
#         print('bhao bhaio bahao')
# animal=Animal()
# pet=pet()
# dog=Dog()
# dog.bark()

class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    @property
    def AfterIncrement(self):
        return self.salary * self.increment
    @AfterIncrement.setter
    def AfterIncrement(self,inc):
        self.increment=inc/ self.salary

e=Employee(1000,1.5)
print(e.AfterIncrement)
print(e.increment)
e.AfterIncrement=2000
print(e.increment)
print(e.AfterIncrement)
# print(e.AfterIncrement)







