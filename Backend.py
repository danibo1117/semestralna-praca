import json
from pacient import Pacient

def saveToJson(pacienti):
    novy_pacienti = []
    for pacient in pacienti:
        novy_pacienti.append(pacient.toDict())
    
    final_dict = {"Pacienti": novy_pacienti}
    json.dump(final_dict, open("pacientdata.json", "w"), indent=6)

def loadFromJson():
    pacienti = []
    final_dict = json.load(open("pacientdata.json","r"))
    novy_pacienti = final_dict["Pacienti"]
    for pacient in novy_pacienti:
        pacient_objekt = Pacient(pacient["id"], pacient["meno"],pacient["priezvisko"],pacient["datumnarod"], pacient["posledna_navs"],pacient["diagnoza"], pacient["predpis_liek"])
        pacienti.append(pacient_objekt)
    return pacienti





