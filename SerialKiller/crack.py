data = '''Hhpnivraosgt5MzNw
jNieegoeecweteOzQ
Y5MDTZarnddCytoTW
kM2YWEhokasemiohv
iaN3Z2UziditYcypu
hcslTMjU4MsinuoiZ
poeafiQzQ5YXiaglu
ahhdrnldXZxM20scC
sotaeiNuaaskYGI=t'''

row = data.split('\n')
nrow = [r*2 for r in row]

# print(nrow)

count = 0
for i in range(0, len(row[0])):
    print(row[0][i], end='')
    # print(row[i], end='')
    for j in range(1, len(row)):
        print(nrow[j][i+(j*2)], end='')
    # print('\n')

    # count += 1
    # if count==2:
    #     break
