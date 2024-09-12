zeme = [
    {
        "kontinent": "Evropa",
        "zeme": {
            "Rusko": {"prumerna_teplota": -5, "doba_letu": {"praha": 3.5, "viden": 3.0}},
            "Ukrajina": {"prumerna_teplota": 9, "doba_letu": {"praha": 2.5, "viden": 2.0}},
            "Francie": {"prumerna_teplota": 11, "doba_letu": {"praha": 2.0, "viden": 1.5}}
        }
    },
    {
        "kontinent": "Afrika",
        "zeme": {
            "Alžírsko": {"prumerna_teplota": 25, "doba_letu": {"praha": 4.0, "viden": 4.5}},
            "DR Kongo": {"prumerna_teplota": 24, "doba_letu": {"praha": 8.0, "viden": 8.5}},
            "Súdán": {"prumerna_teplota": 29, "doba_letu": {"praha": 5.5, "viden": 6.0}}
        }
    },
    {
        "kontinent": "Asie",
        "zeme": {
            "Rusko": {"prumerna_teplota": -5, "doba_letu": {"praha": 3.5, "viden": 3.0}},
            "Čína": {"prumerna_teplota": 13, "doba_letu": {"praha": 10.0, "viden": 9.5}},
            "Indie": {"prumerna_teplota": 27, "doba_letu": {"praha": 8.0, "viden": 7.5}}
        }
    },
    {
        "kontinent": "Severní Amerika",
        "zeme": {
            "Kanada": {"prumerna_teplota": -2, "doba_letu": {"praha": 9.0, "viden": 8.5}},
            "Spojené státy": {"prumerna_teplota": 12, "doba_letu": {"praha": 10.0, "viden": 9.5}},
            "Mexiko": {"prumerna_teplota": 21, "doba_letu": {"praha": 12.0, "viden": 11.5}}
        }
    },
    {
        "kontinent": "Jižní Amerika",
        "zeme": {
            "Brazílie": {"prumerna_teplota": 25, "doba_letu": {"praha": 13.0, "viden": 12.5}},
            "Argentina": {"prumerna_teplota": 15, "doba_letu": {"praha": 14.0, "viden": 13.5}},
            "Peru": {"prumerna_teplota": 20, "doba_letu": {"praha": 13.5, "viden": 13.0}}
        }
    },
    {
        "kontinent": "Austrálie a Oceánie",
        "zeme": {
            "Austrálie": {"prumerna_teplota": 22, "doba_letu": {"praha": 22.0, "viden": 21.5}},
            "Papua-Nová Guinea": {"prumerna_teplota": 26, "doba_letu": {"praha": 21.5, "viden": 21.0}},
            "Nový Zéland": {"prumerna_teplota": 18, "doba_letu": {"praha": 24.0, "viden": 23.5}}
        }
    }
]


# zeme v Evropa s prumernou teplotou nad 10 a dobou letu z praha <=2

for k in zeme:
    if k['kontinent'] == 'Evropa':
        for z,v in k['zeme'].items():
          if v['prumerna_teplota'] > 10 and v['doba_letu']['praha'] <=2:
            print(z)
            
        break


