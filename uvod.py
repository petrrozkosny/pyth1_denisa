import requests
import numpy



web = str('https://www.google.cz')
cislo = str(1)
cislo2 = 1.5
kontrola = True

print(requests.get(web).status_code)
print("ahoj svete")
web = 'https://www.seznam.cz'
print(web)
kuba = 5


ucastnici = ['Ivo','Honza',5,'Honza']
ucastnici_rada = {'Ivo':1,'Honza':1}
ucastnici_tuple = ('Katka','Tomas','Kuba')
ucastnici_set = {'Ivo','Honza','Kuba'}

ucastnici.append('Katka')

print(ucastnici)
ucastnici.remove('Katka')
print(ucastnici)

ucastnici_rada['Katka'] = 1
print(ucastnici_rada)

radky_sloupce = (5,5)
print(set(ucastnici))
print(ucastnici[1])


print(ucastnici)

