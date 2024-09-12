
# seznam / list
mesta = ['Praha','Brno','Ostrava']
print(mesta[0])
# append pridava polozku na konec listu
mesta.append('Plzen')
# remove odebira polozku z listu
mesta.remove('Praha')
mesta.insert(0,'Viden')

# slovnik / dictionary
mesta = {'Praha':1300000,'Brno':400000,'Ostrava':100000}
# pridame klic hodnota do slovniku
mesta['Plzen'] = 100000
# smazeme polozku ze slovniku
del mesta['Praha']
# zmenime hodnotu klice
mesta['Brno'] = 500000
#vypise klice slovniku
print(mesta.keys())
#vypise hodnoty slovniku
print(mesta.values(500))
#vypise hodnotu klice
print(mesta['Brno'])



