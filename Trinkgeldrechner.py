

preis = 20
steuer = 0.19
trinkgeld = 0.05


print("Preis: %s€" %(preis))
print("Mehrwertsteuer: %s" %(steuer))


#Mehrwertsteuer addieren
preis = preis + (preis * steuer)

#Trinkgeld addieren
preis = preis + (preis * trinkgeld)



print("Zu zahlen: %s€" %(preis))

