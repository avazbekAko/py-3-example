print("Функсияи чор амал матиматики ! ")
import math as m
def func_hon(a, b, c):
      jam = (a+b)+c
      tarh = (a-b)-c
      zarb = (a*b)*c
      taqsim = (a/b)/c
      return (jam, tarh, zarb, taqsim)
a = int (input("a: "))
b = int (input("b: "))
c = int (input("c: "))
print("Javob : ",func_hon(a,b,c))

