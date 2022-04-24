import openpyxl

file = open('admin_level_4.txt', 'r', encoding='utf-8')
text = file.read()
text2 = file.read()


Sp = '{"id":'
Sp2 = '"coordinates":[['
lastmas = []
mass = text.split(Sp)
mass2 = mass

mass.pop(0)
for i in range(len(mass)):
    mass[i] = mass[i].split(Sp2)

#print(mass[0][1])
#print(len(mass)) 88

for i in mass:
    lastmas = i[1]
print(lastmas)
#for i in range(len(lastmas)):
#    lastmas[i] = lastmas[i].replace(lastmas[i], ']]}}')

#print(lastmas[0])

Sp3 = '"Feature","name":"'
Sp4 = '","properties":{"ref":'
mass4 = mass2.split(Sp3)
mass3 = []
mass5 = []
mass6 = []

for i in mass4:
    mass3 = i[1]

mass6 = mass3.split(Sp4)
for i in mass6:
    mass5 = i[0]

print(mass5[0])
book = openpyxl.open("Dinamics.xlsx" , read_only = True)
file = open('regions.txt', 'w', encoding='utf-8')

sheet = book.active
for i in range(3,96):
    if sheet[i][1].value != None:
        file.write(sheet[i][1].value + '\n')
        print(sheet[i][1].value)