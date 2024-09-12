game_character = {
    'name': 'Thalion',
    'class': 'Warrior',
    'level': 45,
    'health': 1200,
    'mana': 300,
    'strength': 85,
    'agility': 50,
    'intelligence': 30,
    'equipment': {
        'weapon': 'Sword of Valor',
        'armor': 'Dragon Scale Armor',
        'shield': 'Aegis Shield'
    },
    'skills': [
        {'name': 'Cleave', 'damage': 150, 'mana_cost': 20},
        {'name': 'Shield Bash', 'damage': 100, 'mana_cost': 15},
        {'name': 'Battle Cry', 'buff': 'increases strength by 20 for 10 seconds', 'mana_cost': 25}
    ],
    'quests_completed': 23,
    'reputation': {
        'faction': 'Knights of the Silver Hand',
        'status': 'Honored'
    }
}


foo = game_character['skills'][0]['damage']
print(foo)