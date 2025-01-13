
class Pacient:
    def __init__(self,id, meno, priezvisko, datumnarod,  posledna_navs, diagnoza, predpis_liek):

        self.id = id
        self.meno = meno
        self.priezvisko = priezvisko
        self.datumnarod = datumnarod
        self.posledna_navs = posledna_navs
        self.diagnoza = diagnoza
        self.predpis_liek = predpis_liek

    def toDict(self):
        a = {}
        a["id"] = self.id
        a["meno"] = self.meno
        a["priezvisko"] = self.priezvisko
        a["datumnarod"] = self.datumnarod
        a["posledna_navs"] =  self.posledna_navs
        a["diagnoza"] = self.diagnoza
        a["predpis_liek"] = self.predpis_liek

        return a
    
    def getYear(self):
        a = self.datumnarod[-4:]

        return int(a)



    
  

