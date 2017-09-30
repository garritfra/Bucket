#Zahlen von 1 bis 10
import sys

try:
    a = int(input("kleinste Zahl: "))
    b = int(input("Höchste Zahl: "))
    


except NameError:
    print ("Der eingegebene Wert ist nicht nummerisch")
    sys.exit()
  
  

while a < b:
  a = a + 1
  print(a)
