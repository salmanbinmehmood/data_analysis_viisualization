# # (a + bi)(c + di) = (ac−bd) + (ad + bc)i
#
# class complex:
#
#     def __init__(self,r,i):
#
#         self.r=r
#         self.i=i
#     def __add__(self,c):
#         return complex(self.r + c.r ,self.i + c.i)
#
#     def __mul__(self,c ):#(ac−bd)
#         mulreal=self.r*c.r-self.i*c.i
#         mulimg=self.r*c.i+self.i*c.r
#         return complex(mulreal,mulimg)
#     def __str__(self):
#         return f'{self.r } + { self.i}i'
#
#
# c1=complex(3,2)
# c2=complex(1,7)
# print(c1 + c2)
# print(c1 * c2)

class vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str=''
        index=0
        for i in self.vec:
            str+=f'{i}a{index} +'
            index+=1
        return str[:-1]
    def __add__(self, vec2):
        if len(self.vec)== len(vec2.vec) or len(vec2.vec )==len(self.vec):


            list=[]
            for i in range(len(self.vec)):

                list.append(self.vec[i]+vec2.vec[i])
            return vector(list)
        else:
            return 'adition falied'

    # def __mul__(self, vec2):
    #
    #     sum=0
    #     for i in range(len(self.vec)):
    #         sum+=self.vec[i] * vec2.vec[i]
    #     return sum
    def __len__(self):
        return len(self.vec)




v=vector([1,2])
v2=vector([1,2])
print(v+v2)
# print(v*v2)
print(len(v))




# class vector:
#     def __init__(self,vec):
#         self.vec=vec
#     def __str__(self):
#         str=''
#         for i in self.vec:
#             str+=f'{i} +'
#         return str[:-1]
# vec=vector(['7i^','8j^','10k^'])
# print(vec)

