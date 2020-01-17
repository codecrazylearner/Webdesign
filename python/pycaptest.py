print(2 ** 3 ** 2 ** 1)
a = 0
b = a ** 0
if b < a + 1:
    c = 1
elif b == 1:
    c = 2
else:
    c = 3
print(a + b + c)

for i in range(1, 4, 2):
    print("*")

# Example 2
for i in range(1, 4, 2):
    print("*", end="")

for i in range(1, 4, 2):
    print("*", end="**")
print("\n")
for i in range(1, 4, 2):
    print("*", end="**")
print("***")
s = "Hello, Python!"
print(len(s),s[-14:15])

lst = [[c for c in range(r)] for r in range(3)]
print(lst)
for x in lst:
    for y in x:
        if y < 2:
            print('*', end='')


    def fun(a, b=0, c=5, d=1):
        return a ** b ** c


    print(fun(b=2, a=2, c=3))


# Example 1
x = 1
y = 0

z = x % y
print(z)

# Example 2
x = 1
y = 0

z = x / y
print(z)

x = 0

try:
    print(x)
    print(1 / x)
except ZeroDivisionError:
    print("ERROR MESSAGE")
finally:
    print(x + 1)
print(x + 2)

"""
class A:
    def a(self):
        print("A", end='')


class B(A):
    def a(self):
        print("B", end='')


class C(B):
    def b(self):
        print("B", end='')


a = A()
b = B()
c = C()
a.a()
b.a()
c.b()


try:
    print("Hello")
    raise Exception
    print(1/0)
except Exception as e:
    print(e)
"""