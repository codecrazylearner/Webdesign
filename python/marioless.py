from cs50 import get_int

height=get_int("Height: ")
while ((height<1) or (height>8)):
    height=get_int("Invalid input-- Enter numbers from 1-8")
for i in range(0,height):
    for j in range(0,height-i+1):
       print(" ",end="")
    for k in range(0,i+1):
       print("#",end="")
    print("\r")