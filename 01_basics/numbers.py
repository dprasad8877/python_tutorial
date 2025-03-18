# # # x = 2
# # # y=3
# # # z=4
# # # # print(x+y+z)
# # # # print(x+y*z)
# # # # print(40+2.32)
# # # # print("chain"+"ing")
# # # # print(1,2,3,x,y,z)
# # # # print(1,2,3,x,y,z,sep=":")
# # # # print(y%2)
# # # # print(y//2)
# # # # print(y**2)
# # # #====================================================================================================
# # # result = 1/3.0
# # # print(result)
# # # #====================================================================================================
# # # print(1<2)
# # # print(x < y < z)
# # # print(x < y and y < z)
# # # print(x < y or y < z)
# # # print("==============================================")
# # # print(1 == 2 < 3)
# # # print(1 == 2 and 2 < 3)

# # # print("==============================================")
# # # import math
# # # print(math.floor(32.9))
# # # print(math.ceil(32.3))
# # # print(math.trunc(- 32.6))
# # # print("==============================================")
# # # l= 2+1j
# # # print(l)
# # # print(l.real)   # real part
# # # print(l.imag)   # imaginary part
# # # print(l.conjugate())  # conjugate
# # # print(abs(l))   # absolute value
# # # print(l*3)
# # # print("==============================================")

# # octal=0o177
# # print(octal)
# # hexa=0x9ff
# # print(hexa)
# # binary=0b101010
# # print(binary)
# # print(oct(64))
# # print(hex(64))
# # print(bin(64))

# # print(int("64"))
# # print(int("100",8))
# # print(int("40",16))
# # print(int("1000000",2))
# # print("==============================================")
# # x=1
# # print(x << 2)
# # print(x | 2)
# # print(x & 1)
# # print(~x)
# # print(x ^ 1)
# # print("==============================================")

# import random
# print(random.random())
# print(random.randint(1,10))
# print(random.choice(["apple","banana","cherry","date"]))
# print(random.shuffle(["apple","banana","cherry","date"]))
# print("==============================================")
# from fractions import Fraction
# print(Fraction(1,3))
# print(Fraction(1,3)+Fraction(1,3))
# print(Fraction(1,3)+2)
# print(Fraction(1,3)+2.0)
# print(Fraction(1,3)+0.5)
# print(Fraction(1,3)+Fraction(4,6))
# print(Fraction(1,3)+Fraction(4,6))
# print(Fraction(1,3)*Fraction(4,6))
# print(Fraction(1,3)/Fraction(4,6))
# print(Fraction(1,3)**3)
# print(Fraction(1,3)**-3)
# print(Fraction(1,3)**0)
# print(Fraction(1,3)**1)
# print(Fraction(1,3)**2)

# print("==============================================")
# from decimal import Decimal
# print(decimal.Decimal(1)/decimal.Decimal(3))

# print(decimal.Decimal(1)/decimal.Decimal(3))
# print(decimal.Decimal(1)/decimal.Decimal(3))
# print(decimal.Decimal(1)/decimal.Decimal(3))
# print(decimal.Decimal(1)/decimal.Decimal(3))

# print(decimal.Decimal(1)/decimal.Decimal(3))
# print(decimal.Decimal(1)/decimal.Decimal(3))
# print(decimal.Decimal(1)/decimal.Decimal(3))
setone = {1,2,3,4,5}
settwo = {4,5,6,7,8}
print(setone)
print(settwo)
print(setone | settwo)
print(setone & settwo)
print(setone - settwo)
print(setone - setone)
print(setone ^ settwo)
print(setone <= settwo)
print(setone < settwo)
print(setone >= settwo)

print("==============================================")
print(type(setone))
print(type(True))
print(True + 4)
