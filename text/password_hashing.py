import hashlib
def here():
    f = open("server.txt", "r")

    i = 0
    try:
        for z in f:
            if not z.startswith("#"):
                i = i + 1
                wert = z.rstrip().split("=")[1]
                if wert.__contains__("#") and wert.__contains__(" "):
                    if wert.split(" ")[0].__contains__("#"):
                        print(str(i)+".\t Parameter: "+z.rstrip().split("=")[0]+" \n\t\tWert: "+wert)
                    else:
                        wert = wert.split(" ")[0].rstrip()
                        print(str(i)+".\t Parameter: "+z.rstrip().split("=")[0]+" \n\t\tWert: "+wert)
                else:
                    print(str(i) + ".\t Parameter: " + z.rstrip().split("=")[0] + " \n\t\tWert: " + wert)

                if bool(z.rstrip().split("=")[1]) and z.rstrip().split("=")[0].__contains__("AI"):
                    print("Habe erkannt das es für die KI ist")
    except:
        print("Your Text-Data is corrupted!")
        print("The error is near line: "+str(i))
        #print("Line: "+str(i)+" {}".format(f[i]))

def getlines(line):
    f = open("10000.txt", "r")
    lines = []
    i = 0
    for z in f:
        i=i+1
        if i <= line:
            lines.append(z)
        else:
            return lines
    return lines

def getmaxlength():
    f = open("10000.txt", "r")
    i = 0
    for z in f:
        i=i+1
    return i

def iterFile(path):

    f = open(path, "r")

    for z in f:
        print(z.rstrip())

def order():

    f = open("toorder.txt", "r")

    list = []

    for z in f:
        list.append(z.rstrip().split("=")[0]+z.rstrip().split("=")[1])

    list = sorted(list)
    print(list)

#for z in f:
#    i=i+1f
#    print(i," ",z," Hash: ",hashlib.md5(z.encode()).hexdigest(),"\n\n")
#    hash_array.append(hashlib.md5(z.encode()))


#print("Bitte gebe nun ein Passwort ein: ")
#inStr = input()

#hash_wert = str(hashlib.md5(inStr.encode()))
#to_check_part = hash_wert[:len(hash_wert)/2]

#for z in hash_array:
#
#    if z[:len(z)/2] == to_check_part:
#        print("Your password can be compromised")
if __name__ == "__main__":
    here()
    #for z in getlines(11):
    #    print(z)




