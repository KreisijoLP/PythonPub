import  os

file = open("daten/Belegung.txt")
z1 = 1

rowNames = []
rowTypes = []
rowData = []

for z in file:

    rowI = 0

    for row in z.split("\t"):
        if z1==1:
            rowNames.append(row.rsplit())
            rowData.append([])
        if z1==2:
            rowTypes.append(row.rsplit())
        if z1>2:
            rowData[rowI].append(row.rsplit())
            rowI=rowI+1

    z1=z1+1


ar = 1
print(rowNames)
print(rowTypes)
print(rowData[ar].__len__())
print(rowData[ar])

str = ""
str += "CREATE TABEL Belegung ("

for i in range(rowNames.__len__()):
    print(rowNames[i])
    if i>0:
        str += ", "
    str += rowNames[i][0]
    str +=" "
    str += rowTypes[i][0]
    str +=""

str +=", PRIMARY KEY("
str += rowNames[0][0]
str += "))"
print(str)

insert = ""
insert += "INSERT INTO Belgung ("

for i in range(rowNames.__len__()):
    #print(rowNames[i])
    if i>0:
        insert += ", "
    insert += rowNames[i][0]
    #insert +=" "
    #insert += rowTypes[i][0]
    #insert +=""

insert += ") VALUES ("

Strings = []
insertSTR = ""

#for i in range(rowNames.__len__()):
lenData = len(rowData[0])
for i in range(lenData):
    insertSTR = ""
    Strings.append("")
    Strings[i] = ""
    a = 0
    for s in rowData:
        try:
            #print(i)
            if a>0:
                insertSTR += ","
            #print(s[i][0])
            insertSTR += "\'"
            insertSTR += s[i][0]
            insertSTR += "\'"
            a+=1
            #print("#####")
        except:
            insertSTR += "ERROR"
    Strings[i] += insertSTR



for s in Strings:

    if not s.__contains__("ERROR"):
        p = ""
        p += insert
        p += s
        p += ")"
        print(p)
