import math
try:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print("x**y =", x ** y)
    print(math.log2(x))
except ArithmeticError:
    print("Arithmetic Error: Enter a valid integer")
except Exception:
    print("Exception: Enter an integer.")

