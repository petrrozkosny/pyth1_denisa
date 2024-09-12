mesta = ['Praha','Brno','Ostrava']

# pro kazdou jednu polozku v listu mesta
# for i in mesta:
#     print('Ahoj, já jsem z města ' + i)

i = 0

# while i < len(mesta):
#     print(mesta[i], 'i se rovna', i)
#     #i += 1 # i rovna se i plus jedna

# pokracovat = 'Y'
# while pokracovat == 'Y':
#     mesto = input('Zadej mesto: ')

#     print(mesto in mesta)
#     pokracovat = input('Chces pokracovat? Y/N ')

# for i in mesta:
#     print(i)
#     if i == 'Brno':
#         # break ukonci cyklus
#         break
        
        
# for i in mesta:
#     if i == 'Brno':
#         # continue preskoci zbytek kodu a pokracuje dalsi iteraci
#         continue
#     print(i)

slovnik = {'Praha':1300000,'Brno':400000,'Ostrava':100000}

for i,j in slovnik.items():
    print('toto je klic', i)
    print(f'toto je hodnota {j}')
    print('toto je hodnota', j)
    

