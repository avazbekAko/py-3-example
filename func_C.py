def factorial (n):
      summa = 1
      for i in range(2,n+1):
            summa *= i
      return summa
      
n = int (input("n = "))
m = int (input("m = "))
print((factorial(n)) / (factorial(m) * factorial(n-m)))
