import requests

url = 'https://api.adviceslip.com/advice'
dalsi_rada = 'Y'
rady = []

while dalsi_rada == 'Y':
    obsah = requests.get(url)
    
    rada_text = obsah['slip']['advice']
    print(rada_text)
    rady.append(rada_text)
    dalsi_rada = input('Chce dalsi radu? Y/N: ' )

print(len(rady))

# CHCI VYDELIT DVE CISLA
