#Zahlen von 1 bis 10
import sys

try:
    a = input("kleinste Zahl: ") 
    b = input("Höchste Zahl: ")

    if type(a) != int or type(b) != int:
      raise


except:
    print ("Der eingegebene Wert ist nicht nummerisch")
    sys.exit()
  
  

while a < 10:
  a = a + 1
  print(a)
