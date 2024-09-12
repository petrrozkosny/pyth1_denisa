zeme = [
    {"zeme": "Česko", "mena": "Koruna", "kontinent": "Evropa"},
    {"zeme": "Slovensko", "mena": "Euro", "kontinent": "Evropa"},
    {"zeme": "Maďarsko", "mena": "Forint", "kontinent": "Evropa"},
    {"zeme": "Egypt", "mena": "Libra", "kontinent": "Afrika"},
    {"zeme": "Francouzská Guyana", "mena": "Euro", "kontinent": "Jižní Amerika"}
]

# chci na dovolenou do zeme, kde se platí Euro a není v Evropa
for s in zeme:
    if s['mena'] == 'Euro' and s['kontinent'] != 'Evropa':
        print(s['zeme']) 