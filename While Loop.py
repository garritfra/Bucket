#Zahlen von 1 bis 10
from sys import *
try:
    a = int(input("kleinste Zahl: ")) 

    b = int(input("Höchste Zahl: "))
except ValueError or NameError:
    #print ("Der eingegebene Wert ist nicht nummerisch")
    pass
  
  

while a < 10:
  a = a + 1
  print(a)
