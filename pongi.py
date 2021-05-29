# def myfuc(a, b, type='+', repeat=1) :
#     result=0
#     for i in range (repeat) :
#         if type =='+':
#             result += a + b
#         if type =='-':
#             result += a - b
#         if type =='*':
#             result += a * b
#         if type =='/':
#             result += a / b
#     return result
#
#
# number = myfuc (37, 33, type='+', repeat=2)
#
# print(number)



class Clac:
    def __init__(self, a, b):
        self.a= a
        self.b= b

    def plus (self):
        return self.a+self.b

    def minus (self):
        return self.a-self.b

    def multiple (self):
        return self.a*self.b

    def divide (self):
        return self.a/self.b

a= Clac(3.14,3.13)

print (a.a, a.b, a.plus(), a.minus(), a.multiple(), a.divide())



























