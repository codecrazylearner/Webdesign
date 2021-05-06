from cs50 import get_int

height=get_int("Height: ")
while ((height<1) or (height>8)):
    height=get_int("\n Invalid number -- enter the height again")
for i in range(0,height):
  for j  in range(0,height-i+1):
      print(" ",end="")
  for l in range(0,i+1):
      print("#",end="")
  print(" ",end="")
  for k in range(0,i+1):
       print("#",end="")
  print("\r")

