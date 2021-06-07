f = open("../text/10000.txt", "r")
i=0
for z in f:
    if z.rstrip().isdigit():
        i=i+1
        print(z)

        if z.__eq__("1234"):
            print("Hallo")


print("Es gib "+str(i)+" Nummereische Passwörter")