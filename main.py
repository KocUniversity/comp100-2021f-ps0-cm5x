
#Raising a Number to a Power and Taking a Logarithm
import numpy as np

x = input("Please enter a number to define as x:")
y = input("Please enter a number to define as y:")


def PowerIt(a, b):
  return int(a)**int(b) 

def LogBased2(c):
  return np.log2(int(c))

print("Value of the x to the power of y is {}".format(PowerIt(x,y)))

print("2 based log of x is {}".format(LogBased2(x)))
print(" ")
print(" ")
print(" ")
print("0076571")