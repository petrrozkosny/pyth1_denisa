
mesta = ['Olomouc','Praha','Brno','Ostrava']


'''
Pokud narazime na Praha, vypisme 'hlavni mesto', jinak vypiseme 'krajske mesto'
'''

# for i in mesta:
#     if i == 'Praha':
#         print('hlavni mesto')
#     else:
# #         print('krajske mesto')

# for i in mesta:
#     if i == 'Praha':
#         print('hlavni mesto')
#     elif i == 'Brno':
#         print('brno')
#     else:
#         print('ostatni')


# for i in mesta:
#     match i:
#         case 'Praha':
#             print('hlavni mesto')
#         case 'Brno':
#             print('brno')
#         case _:
#             print('ostatni')

# print('ostrava' == 'praha')
# for i in mesta:
#     # FALSE and FALSE
#     if i == 'Praha' and i == 'Brno':
#         print('je to krasne mesto')
#     else:
#         print('je to mesto')

zeme = {'slovensko':{'mena':'eur','more':False},'chorvatsko':{'mena':'eur','more':True}}

# chci na dovolenou do zeme kde se plati eurem a ma more

# for k,v in zeme.items():
#     mena = v['mena']
#     more = v['more']
#     if mena == 'eur' and more == True:
#         print(k)

# # chci na dovolenou do zeme, ktera ma euro nebo more a neni to slovensko

# for k,v in zeme.items():
#     mena = v['mena']
#     more = v['more']
#     if (mena == 'eur' or more == True) and k !='slovensko':
#         print(k)




