'''>>>>>>>> OPERATORS <<<<<<<<<<< '''

'''-----Arithmetic OPERATORS-------'''
# Addtion (+)
a=2+3
print("Addtion",a)
# Subtraction (-)
a=2-3
print("Subtraction",a)
# Multiplication (*)
a=2*3
print('Multiplication',a)
# Division (/)
a=12/3
print("Division",a)
# Module (%)
a=12%5
print("Module",a)
# Floor Division (/)
a=12//5
print("Floor Division",a)
# Power (**)
a=2**5
print("Power",a)


''' -----Relational OPERATORS-------'''
# <
a=5<2
print(a)
# >
a=5>2
print(a)
# <=
a=5<=2
print(a)
# >=
a=5>=2
print(a)
# ==
a=5==2
print(a)
# !=
a=5!=2
print(a)


''' ------Logical OPERATORS---------'''
# and
a= 2<3 and 2
print(a)

# or
a= 2>3 or 2==2
print(a)

# not
a=not(5>2)
print(a)


'''------Assignment OPERATORS---------'''
# =
a=10
print(a)
# +=
a=10
a+=20
print(a)
# -=
a=10
a-=20
print(a)
# *=
a=10
a*=20
print(a)
# /=
a=10
a/=20
print(a)
# %=
a=10
a%=20
print(a)
# **=
a=5
a**=2
print(a)
# //=
a=10
a//=20
print(a)


'''--------Bitwise OPERATORS---------'''
# &
a=5 & 3
print("Bit-And",a)
# |
a=5 | 3
print("Bit-Or",a)
# ^
a=5^3
print("Bit-XOR",a)
# ~
a=~5
print("Bit-NOT",a)
# <<
a=5<<2
print("Bit-LeftShift",a)
# >>
a=20>>2
print("Bit-RightShift",a)


'''-------Membership OPERATORS-------'''
# in
a="Hardik"
print('H'in a)
# not in
a="Hardik"
print('ar'not in a)


'''-------Identity OPERATORS--------'''

# is
a=10
b=10
print(a is b)
# is not
a=10
b=10
print(a is not b)