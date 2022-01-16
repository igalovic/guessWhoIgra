
import spade
import random

class Osoba:
    def __init__(self,ime,spol,imaBrkove,imaNaocale,imaBradu,imaKosu,imaKapu,bojaKape,bojaBrkova,bojaKose,bojaBrade,bojaNaocala,bojaOciju):
        self.ime = ime
        self.spol = spol
        self.imaBrkove = imaBrkove
        self.imaNaocale = imaNaocale
        self.imaBradu = imaBradu
        self.imaKosu = imaKosu
        self.imaKapu = imaKapu
        self.bojaKape = bojaKape
        self.bojaBrkova = bojaBrkova
        self.bojaKose = bojaKose
        self.bojaBrade = bojaBrade
        self.bojaNaocala = bojaNaocala
        self.bojaOciju = bojaOciju

    def ucitajOsobe():
        o1 = Osoba("Alex","muskarac",True,False,False,True,False,"", "Crna","Crna","","","Smeda")
        o2 = Osoba("Alfred","muskarac",True,False,False,True,False,"","Narancasta","Narancasta","","","Zelena")
        o3 = Osoba("Anita","zena",False,False,False,True,False,"","","Plava","","","Plava")
        o4 = Osoba("Anne","zena",False,False,False,True,False,"","","Crna","","","Smeda")
        o5 = Osoba("Bernard","muskarac",False,False,False,True,True,"Siva","","Smeda","","","Smeda")
        o6 = Osoba("Bill","muskarac",False,False,True,False,False,"","","Narancasta","Narancasta","","Smeda")
        o7 = Osoba("Charles","muskarac",True,False,False,True,False,"","Plava","Plava","","","Smeda")
        o8 = Osoba("Claire","zena",False,True,False,True,True,"Zuta","","Narancasta","","Plava","Smeda")
        o9 = Osoba("David","muskarac",False,False,True,True,False,"","","Plava","Plava","","Zelena")
        o10 = Osoba("Eric","muskarac",False,False,False,True,True,"Plava","","Plava","","","Smeda")
        o11 = Osoba("Frans","muskarac",False,False,False,True,False,"","","Narancasta","","","Smeda")
        o12 = Osoba("George","muskarac",False,False,False,True,True,"Siva","","Bijela","","","Zelena")
        o13 = Osoba("Herman","muskarac",False,False,False,False,False,"","","","","","Smeda")
        o14 = Osoba("Joe","muskarac",False,True,False,True,False,"","","Plava","","Crvena","Zelena")
        o15 = Osoba("Maria","zena",False,False,False,True,True,"Zelena","","Smeda","","","Smeda")
        o16 = Osoba("Max","muskarac",True,False,False,True,False,"","Crna","Crna","","","Smeda")
        o17 = Osoba("Paul","muskarac",False,True,False,True,False,"","","Bijela","","Bijela","Smeda")
        o18 = Osoba("Peter","muskarac",False,False,False,True,False,"","","Bijela","","","Plava")
        o19 = Osoba("Philip","muskarac",False,False,True,True,False,"","","Crna","Crna","","Smeda")
        o20 = Osoba("Richard","muskarac",True,False,True,False,False,"","Smeda","","Smeda","","Smeda")
        o21 = Osoba("Robert","muskarac",False,False,False,True,False,"","","Smeda","","","Plava")
        o22 = Osoba("Sam","muskarac",False,True,False,False,False,"","","","","Crna","Smeda")
        o23 = Osoba("Susan","zena",False,False,False,True,False,"","","Bijela","","","Zelena")
        o24 = Osoba("Tom","muskarac",False,True,False,False,False,"","","","","Smeda","Plava")
    
        listaKorisnikaSaImenima = []
        listaKorisnikaSaImenima.extend((o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17,o18,o19,o20,o21,o22,o23,o24))
        #print(listaKorisnikaSaImenima)
        return listaKorisnikaSaImenima



class PrviAgent(spade.agent.Agent):   
    class PosaljiIPrimiPoruku(spade.behaviour.PeriodicBehaviour):
        async def on_start(self):
            self.grupnaPitanja = ["Jesi li muskarac ? ","Jesi li zena ? ","Imas li kosu ? ","Imas li bradu ? ","Imas li kapu ? ","Imas li brkove ? ","Imas li naocale ? ", "Imas li plave oci ? ","Imas li zelene oci ? ","Imas li smede oci ? "]
            self.listaImena = []
            self.listaSpolova = []
            self.listaBrkova = []
            self.listaNaocala = []
            self.listaBrade = []
            self.listaKapa = []
            self.listaKose = []
            self.osobe = Osoba.ucitajOsobe()
            self.odgovor = ""
            for i in range(len(self.osobe)):
                self.listaImena.append(self.osobe[i].ime) 
                self.listaSpolova.append(self.osobe[i].spol)
                self.listaBrkova.extend((self.osobe[i].imaBrkove,self.osobe[i].bojaBrkova))
                self.listaKose.extend((self.osobe[i].imaKosu,self.osobe[i].bojaKose))
                self.listaNaocala.extend((self.osobe[i].imaNaocale,self.osobe[i].bojaNaocala))
                self.listaBrade.extend((self.osobe[i].imaBradu,self.osobe[i].bojaBrade))
                self.listaKapa.extend((self.osobe[i].imaKapu,self.osobe[i].bojaKape))
            self.mojaKartica = random.choice(self.listaImena)
            for osoba in self.osobe:
                if(osoba.ime == self.mojaKartica):
                    self.mojaOsoba = osoba
            print(f" Prvi agent je osoba {self.mojaKartica}")
        async def run(self):
            karticaProtivnika = ""
            substringPoruke = ";"
            if len(self.osobe) == 1:
                for i in range(len(self.osobe)):
                    karticaProtivnika = self.osobe[i].ime
                nazivProtivnika = spade.message.Message(
                to="ares@rec.foi.hr",
                body = f"Ti si {karticaProtivnika} !",
                metadata={
                "ontology":"tvojaKartica",
                "language":"hrvatski"
                        }
                )
                await self.send(nazivProtivnika)
            osobeZaIzbrisati = []
            msg = await self.receive(timeout=5)
            if not self.grupnaPitanja:
                randomOsoba = random.choice(self.listaImena)
                grupnoPitanje = "Ti si " + randomOsoba + " !"
                for osoba in self.osobe:
                    if(osoba.ime== randomOsoba):
                        self.osobe.remove(osoba)
            else: 
                grupnoPitanje = random.choice(self.grupnaPitanja)
                if(grupnoPitanje == "Jesi li muskarac ? " or grupnoPitanje == "Jesi li zena ? "):
                    self.grupnaPitanja.remove("Jesi li muskarac ? ")
                    self.grupnaPitanja.remove("Jesi li zena ? ")
                if(grupnoPitanje == "Imas li kosu ? "):
                    self.grupnaPitanja.remove("Imas li kosu ? ")
                if(grupnoPitanje == "Imas li bradu ? " ):
                    self.grupnaPitanja.remove("Imas li bradu ? ")
                if(grupnoPitanje == "Imas li kapu ? "):
                    self.grupnaPitanja.remove("Imas li kapu ? ")
                if(grupnoPitanje == "Imas li brkove ? "):
                    self.grupnaPitanja.remove("Imas li brkove ? ")
                if(grupnoPitanje == "Imas li naocale ? "):
                    self.grupnaPitanja.remove("Imas li naocale ? ")
            if msg:
                if substringPoruke in msg.body:
                    cijelaPoruka = msg.body.split(";")
                    odgovorProtivnika = cijelaPoruka[0]
                    pitanjeProtivnika = cijelaPoruka[1]
                    rijeci = pitanjeProtivnika.split() 
                else:
                    odgovorProtivnika = msg.body
                    rijeci = odgovorProtivnika.split()
                if odgovorProtivnika == "Pogodio si moju karticu. Cestitke pobijedio si!":
                    await self.agent.stop()
                print(f"Prvi agent : Primio sam poruku sadržaja: {msg.body}")
                if odgovorProtivnika == "Jesam, muskarac sam !":
                    for osoba in self.osobe:
                        if(osoba.spol == "zena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nisam muskarac ":
                    for osoba in self.osobe:
                        if(osoba.spol=="muskarac"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Jesam, zena sam":
                    for osoba in self.osobe:
                        if(osoba.spol=="muskarac"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nisam zena":
                    for osoba in self.osobe:
                        if(osoba.spol=="zena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam kosu":
                    for osoba in self.osobe:
                        if(osoba.imaKosu ==True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam kosu":
                    self.grupnaPitanja.extend(("Imas li plavu kosu ? ", "Imas li crnu kosu ? ", "Imas li narancastu kosu ? ", "Imas li bijelu kosu ? ", "Imas li smedu kosu ? "))
                    for osoba in self.osobe:
                        if(osoba.imaKosu==False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam naocale":
                    for osoba in self.osobe:
                        if(osoba.imaNaocale==True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam naocale":
                    self.grupnaPitanja.extend(("Imas li plave naocale ? ", "Imas li crne naocale ? ", "Imas li crvene naocale ? ", "Imas li bijele naocale ? ", "Imas li smede naocale ? "))
                    for osoba in self.osobe:
                        if(osoba.imaNaocale == False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam bradu":
                    for osoba in self.osobe:
                        if(osoba.imaBradu == True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam bradu":
                    self.grupnaPitanja.extend(("Imas li narancastu bradu ? ", "Imas li plavu bradu ? ", "Imas li crnu bradu ? ","Imas li smedu bradu ? "))
                    for osoba in self.osobe:
                        if(osoba.imaBradu == False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam kapu":
                    for osoba in self.osobe:
                        if(osoba.imaKapu == True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam kapu":
                    self.grupnaPitanja.extend(("Imas li zelenu kapu ? ", "Imas li plavu kapu ? ", "Imas li zutu kapu ? ", "Imas li sivu kapu ? "))
                    for osoba in self.osobe:
                        if(osoba.imaKapu == False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam brkove":
                    for osoba in self.osobe:
                        if(osoba.imaBrkove == True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam brkove":
                    self.grupnaPitanja.extend(("Imas li crne brkove ? ", "Imas li narancaste brkove ? ", "Imas li plave brkove ? ", "Imas li smede brkove ? "))
                    for osoba in self.osobe:
                        if(osoba.imaBrkove == False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plave naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plave naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam crvene naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Crvena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam crvene naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Crvena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam bijele naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Bijela"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam bijele naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Bijela"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam crne naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam crne naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam smede naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam smede naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam smede oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju != "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam smede oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju == "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam zelene oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju != "Zelena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam zelene oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju == "Zelena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plave oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plave oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam narancastu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade != "Narancasta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam narancastu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade == "Narancasta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plavu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plavu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam crnu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade != "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam crnu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade == "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam smedu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade != "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam smedu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade == "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam crne brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova != "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam crne brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova == "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam narancaste brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova != "Narancasta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam narancaste brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova == "Narancasta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plave brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plave brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam smede brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova != "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam smede brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova == "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam zelenu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape != "Zelena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam zelenu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape == "Zelena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plavu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plavu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam zutu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape != "Zuta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam zutu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape == "Zuta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam sivu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape != "Siva"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam sivu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape == "Siva"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Ti si " + self.mojaKartica + " !":
                    self.agent.stop()
                
                if(grupnoPitanje == "Imas li plave oci ? " and odgovorProtivnika=="Imam plave oci"):
                    self.grupnaPitanja.remove("Imas li plave oci ? ")
                    self.grupnaPitanja.remove("Imas li zelene oci ? ")
                    self.grupnaPitanja.remove("Imas li smede oci ? ")
                elif(grupnoPitanje == "Imas li plave oci ? " and odgovorProtivnika=="Nemam plave oci"):
                    self.grupnaPitanja.remove("Imas li plave oci ? ")
                elif(grupnoPitanje == "Imas li zelene oci ? " and odgovorProtivnika=="Imam zelene oci"):
                    self.grupnaPitanja.remove("Imas li plave oci ? ")
                    self.grupnaPitanja.remove("Imas li zelene oci ? ")
                    self.grupnaPitanja.remove("Imas li smede oci ? ")
                elif(grupnoPitanje == "Imas li zelene oci ? " and odgovorProtivnika=="Nemam zelene oci"):
                    self.grupnaPitanja.remove("Imas li zelene oci ? ")
                elif(grupnoPitanje == "Imas li smede oci ? " and odgovorProtivnika=="Imam smede oci"):
                    self.grupnaPitanja.remove("Imas li plave oci ? ")
                    self.grupnaPitanja.remove("Imas li zelene oci ? ")
                    self.grupnaPitanja.remove("Imas li smede oci ? ")
                elif(grupnoPitanje == "Imas li smede oci ? " and odgovorProtivnika=="Nemam smede oci"):
                    self.grupnaPitanja.remove("Imas li smede oci ? ")
                elif(grupnoPitanje == "Imas li plave naocale ? " and odgovorProtivnika=="Imam plave naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li plave naocale ? " and odgovorProtivnika=="Nemam plave naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                elif(grupnoPitanje == "Imas li crvene naocale ? " and odgovorProtivnika=="Imam crvene naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li crvene naocale ? " and odgovorProtivnika=="Nemam crvene naocale"):
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                elif(grupnoPitanje == "Imas li bijele naocale ? " and odgovorProtivnika=="Imam bijele naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li bijele naocale ? " and odgovorProtivnika=="Nemam bijele naocale"):
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                elif(grupnoPitanje == "Imas li crne naocale ? " and odgovorProtivnika=="Imam crne naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li crne naocale ? " and odgovorProtivnika=="Nemam crne naocale"):
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                elif(grupnoPitanje == "Imas li smede naocale ? " and odgovorProtivnika=="Imam smede naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li smede naocale ? " and odgovorProtivnika=="Nemam smede naocale"):
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li narancastu bradu ? " and odgovorProtivnika=="Imam narancastu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li narancastu bradu ? " and odgovorProtivnika=="Nemam narancastu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                elif(grupnoPitanje == "Imas li plavu bradu ? " and odgovorProtivnika=="Imam plavu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li plavu bradu ? " and odgovorProtivnika=="Nemam plavu bradu"):
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                elif(grupnoPitanje == "Imas li crnu bradu ? " and odgovorProtivnika=="Imam crnu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li crnu bradu ? " and odgovorProtivnika=="Nemam crnu bradu"):
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                elif(grupnoPitanje == "Imas li smedu bradu ? " and odgovorProtivnika=="Imam smedu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li smedu bradu ? " and odgovorProtivnika=="Nemam smedu bradu"):
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li crne brkove ? " and odgovorProtivnika=="Imam crne brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li crne brkove ? " and odgovorProtivnika=="Nemam crne brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                elif(grupnoPitanje == "Imas li narancaste brkove ? " and odgovorProtivnika=="Imam narancaste brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li narancaste brkove ? " and odgovorProtivnika=="Nemam narancaste brkove"):
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                elif(grupnoPitanje == "Imas li plave brkove ? " and odgovorProtivnika=="Imam plave brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li plave brkove ? " and odgovorProtivnika=="Nemam plave brkove"):
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                elif(grupnoPitanje == "Imas li smede brkove ? " and odgovorProtivnika=="Imam smede brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li smede brkove ? " and odgovorProtivnika=="Nemam smede brkove"):
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li zelenu kapu ? " and odgovorProtivnika=="Imam zelenu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                elif(grupnoPitanje == "Imas li zelenu kapu ? " and odgovorProtivnika=="Nemam zelenu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                elif(grupnoPitanje == "Imas li plavu kapu ? " and odgovorProtivnika=="Imam plavu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                elif(grupnoPitanje == "Imas li plavu kapu ? " and odgovorProtivnika=="Nemam plavu kapu"):
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                elif(grupnoPitanje == "Imas li zutu kapu ? " and odgovorProtivnika=="Imam zutu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                elif(grupnoPitanje == "Imas li zutu kapu ? " and odgovorProtivnika=="Nemam zutu kapu"):
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                elif(grupnoPitanje == "Imas li sivu kapu ? " and odgovorProtivnika=="Imam sivu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                elif(grupnoPitanje == "Imas li sivu kapu ? " and odgovorProtivnika=="Neman sivu kapu"):
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                
                
                
                #print(rijeci[-2])
                if(rijeci[-2]==self.mojaKartica):
                    poruka1 = spade.message.Message(
                    to="ares@rec.foi.hr",
                    body = "Pogodio si moju karticu. Cestitke pobijedio si!",
                    metadata={
                    "ontology":"pitanje",
                    "language":"hrvatski"
                        }
                    )
                    await self.send(poruka1)
                    print("Drugi agent je pobijedio!")   
                    await self.agent.stop()
                if(rijeci[-2]=="muskarac"):
                    if(self.mojaOsoba.spol == "muskarac"):
                        self.odgovor = "Jesam, muskarac sam !;"
                    else:
                        self.odgovor = "Nisam muskarac;",
                        
                if(rijeci[-2]=="zena"):
                    if(self.mojaOsoba.spol == "zena"):
                        self.odgovor = "Jesam, zena sam !;"
                        
                    else:
                        self.odgovor = "Nisam zena;"
                        
                if(rijeci[-2]=="kosu" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaKosu == True):
                        self.odgovor = "Imam kosu;"
                      
                    else:

                        self.odgovor = "Nemam kosu;"

                if(rijeci[-2]=="naocale" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaNaocale == True):
                        self.odgovor = "Imam naocale;"
                    else:
                        self.odgovor = "Nemam naocale;"

                if(rijeci[-2]=="brkove" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaBrkove == True):
                        self.odgovor = "Imam brkove;"
                    else:
                        self.odgovor = "Nemam brkove;"

                if(rijeci[-2]=="kapu" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaKapu == True):
                        self.odgovor = "Imam kapu;"
                    else:
                        self.odgovor = "Nemam kapu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaBradu == True):
                        self.odgovor = "Imam bradu;"
                    else:
                        self.odgovor = "Nemam bradu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="narancastu"):
                    if(self.mojaOsoba.bojaBrade=="Narancasta"):
                        self.odgovor = "Imam narancastu bradu;"
                    else:
                        self.odgovor = "Nemam narancastu bradu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="plavu"):
                    if(self.mojaOsoba.bojaBrade=="Plava"):
                        self.odgovor = "Imam plavu bradu;"
                    else:
                        self.odgovor = "Nemam plavu bradu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="crnu"):
                    if(self.mojaOsoba.bojaBrade=="Crna"):
                        self.odgovor = "Imam crnu bradu;"
                    else:
                        self.odgovor = "Nemam crnu bradu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="smedu"):
                    if(self.mojaOsoba.bojaBrade=="Smeda"):
                        self.odgovor = "Imam smedu bradu;"
                    else:
                        self.odgovor = "Nemam smedu bradu;"
                if(rijeci[-2]=="naocale" and rijeci[-3]=="plave"):
                    if(self.mojaOsoba.bojaNaocala=="Plava"):
                        self.odgovor = "Imam plave naocale;"

                    else:
                        self.odgovor = "Nemam plave naocale;"
                if(rijeci[-2]=="naocale" and rijeci[-3]=="crvene"):
                    if(self.mojaOsoba.bojaNaocala=="Crvena"):
                        self.odgovor = "Imam crvene naocale;"           
                    else:
                        self.odgovor = "Nemam crvene naocale;"
                if(rijeci[-2]=="naocale" and rijeci[-3]=="bijele"):
                    if(self.mojaOsoba.bojaNaocala=="Bijela"):
                        self.odgovor = "Imam bijele naocale;"
                    else:
                        self.odgovor = "Nemam bijele naocale;"
                if(rijeci[-2]=="naocale" and rijeci[-3]=="crne"):
                    if(self.mojaOsoba.bojaNaocala=="Crna"):
                        self.odgovor = "Imam crne naocale;"

                    else:
                        self.odgovor = "Nemam crne naocale;"
        
                if(rijeci[-2]=="naocale" and rijeci[-3]=="smede"):
                    if(self.mojaOsoba.bojaNaocala=="Smeda"):
                        self.odgovor = "Imam smede naocale;"
                    else:
                        self.odgovor = "Nemam smede naocale;"
                if(rijeci[-2]=="oci" and rijeci[-3]=="smede"):
                    if(self.mojaOsoba.bojaOciju=="Smeda"):
                        self.odgovor = "Imam smede oci;"
                    else:
                        self.odgovor = "Nemam smede oci;"
                if(rijeci[-2]=="oci" and rijeci[-3]=="zelene"):
                    if(self.mojaOsoba.bojaOciju=="Zelena"):
                        self.odgovor = "Imam zelene oci;"
                    else:
                        self.odgovor = "Nemam zelene oci;"
                if(rijeci[-2]=="oci" and rijeci[-3]=="plave"):
                    if(self.mojaOsoba.bojaOciju=="Plava"):
                        self.odgovor = "Imam plave oci;"
                    else:
                        self.odgovor = "Nemam plave oci;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="smede"):
                    if(self.mojaOsoba.bojaBrkova=="Smeda"):
                        self.odgovor = "Imam smede brkove;"
                    else:
                        self.odgovor = "Nemam smede brkove;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="crne"):
                    if(self.mojaOsoba.bojaBrkova=="Crna"):
                        self.odgovor = "Imam crne brkove;"
                    else:
                        self.odgovor = "Nemam crne brkove;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="narancaste"):
                    if(self.mojaOsoba.bojaBrkova=="Narancasta"):
                        self.odgovor = "Imam narancaste brkove;"
                    else:
                        self.odgovor = "Nemam narancaste brkove;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="plave"):
                    if(self.mojaOsoba.bojaBrkova=="Plava"):
                        self.odgovor = "Imam plave brkove;"
                    else:
                        self.odgovor = "Nemam plave brkove;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="narancaste"):
                    if(self.mojaOsoba.bojaBrkova=="Narancasta"):
                        self.odgovor = "Imam narancaste brkove;"
                    else:
                        self.odgovor = "Nemam narancaste brkove;"
                if(rijeci[-2]=="kapu" and rijeci[-3]=="zelenu"):
                    if(self.mojaOsoba.bojaKape=="Zelena"):
                        self.odgovor = "Imam zelenu kapu;"
                    else:
                        self.odgovor = "Nemam zelenu kapu;"
                if(rijeci[-2]=="kapu" and rijeci[-3]=="plavu"):
                    if(self.mojaOsoba.bojaKape=="Plava"):
                        self.odgovor = "Imam plavu kapu;"
                    else:
                        self.odgovor = "Nemam plavu kapu;"
                if(rijeci[-2]=="kapu" and rijeci[-3]=="zutu"):
                    if(self.mojaOsoba.bojaKape=="Zuta"):
                        self.odgovor = "Imam zutu kapu;"
                    else:
                        self.odgovor = "Nemam zutu kapu;"
                if(rijeci[-2]=="kapu" and rijeci[-3]=="sivu"):
                    if(self.mojaOsoba.bojaKape=="Siva"):
                        self.odgovor = "Imam sivu kapu;"
                    else:
                        self.odgovor = "Nemam sivu kapu;"
            


            #osoba = random.choice(self.listaImena)
            #specificnaOsobaPitanje = "Jesi li ti mozda " + osoba + " ?"
            
            #self.osobe.remove(osoba) 
            msg = spade.message.Message(
                to="ares@rec.foi.hr",
                body = self.odgovor + grupnoPitanje,
                metadata={
                    "ontology":"pitanje",
                    "language":"hrvatski"
                }
            )
            await self.send(msg)
            print("Prvi agent: Pitanje poslano!")                



    async def setup(self):
        print("Prvi agent: Pokrećem se!")
        ponasanje = self.PosaljiIPrimiPoruku(period=5)
        #ponasanje2 = self.PrimiPoruku(period=20)
        self.add_behaviour(ponasanje)
        #self.add_behaviour(ponasanje2)

class DrugiAgent(spade.agent.Agent):
    class PrimiIPosaljiPoruku(spade.behaviour.PeriodicBehaviour):
        async def on_start(self):
            self.grupnaPitanja = ["Jesi li muskarac ? ","Jesi li zena ? ","Imas li kosu ? ","Imas li bradu ? ","Imas li kapu ? ","Imas li brkove ? ","Imas li naocale ? ", "Imas li plave oci ? ","Imas li zelene oci ? ","Imas li smede oci ? "]
            self.listaImena = []
            self.listaSpolova = []
            self.listaBrkova = []
            self.listaNaocala = []
            self.listaBrade = []
            self.listaKapa = []
            self.listaKose = []
            self.odgovor = ""
            self.osobe = Osoba.ucitajOsobe()
            for i in range(len(self.osobe)):
                self.listaImena.append(self.osobe[i].ime) 
                self.listaSpolova.append(self.osobe[i].spol)
                self.listaBrkova.extend((self.osobe[i].imaBrkove,self.osobe[i].bojaBrkova))
                self.listaKose.extend((self.osobe[i].imaKosu,self.osobe[i].bojaKose))
                self.listaNaocala.extend((self.osobe[i].imaNaocale,self.osobe[i].bojaNaocala))
                self.listaBrade.extend((self.osobe[i].imaBradu,self.osobe[i].bojaBrade))
                self.listaKapa.extend((self.osobe[i].imaKapu,self.osobe[i].bojaKape))
            self.mojaKartica = random.choice(self.listaImena)
            for osoba in self.osobe:
                if(osoba.ime == self.mojaKartica):
                    self.mojaOsoba = osoba
            print(f" Drugi agent je osoba {self.mojaKartica}")
        async def run(self):
            karticaProtivnika = ""
            if len(self.osobe) == 1:
                for i in range(len(self.osobe)):
                    karticaProtivnika = self.osobe[i].ime
                nazivProtivnika = spade.message.Message(
                to="posiljatelj@rec.foi.hr",
                body = f"Ti si {karticaProtivnika} !",
                metadata={
                "ontology":"tvojaKartica",
                "language":"hrvatski"
                        }
                )
                await self.send(nazivProtivnika)
            osobeZaIzbrisati = []
            substringPoruke = ";"
            msg = await self.receive(timeout=5)
            if not self.grupnaPitanja:
                randomOsoba = random.choice(self.listaImena)
                grupnoPitanje = "Ti si " + randomOsoba + " !"
                for osoba in self.osobe:
                    if(osoba.ime== randomOsoba):
                        self.osobe.remove(osoba)
            else: 
                grupnoPitanje = random.choice(self.grupnaPitanja)
                if(grupnoPitanje == "Jesi li muskarac ? " or grupnoPitanje == "Jesi li zena ? "):
                    self.grupnaPitanja.remove("Jesi li muskarac ? ")
                    self.grupnaPitanja.remove("Jesi li zena ? ")
                if(grupnoPitanje == "Imas li kosu ? "):
                    self.grupnaPitanja.remove("Imas li kosu ? ")
                if(grupnoPitanje == "Imas li bradu ? " ):
                    self.grupnaPitanja.remove("Imas li bradu ? ")
                if(grupnoPitanje == "Imas li kapu ? "):
                    self.grupnaPitanja.remove("Imas li kapu ? ")
                if(grupnoPitanje == "Imas li brkove ? "):
                    self.grupnaPitanja.remove("Imas li brkove ? ")
                if(grupnoPitanje == "Imas li naocale ? "):
                    self.grupnaPitanja.remove("Imas li naocale ? ")
            #osoba = random.choice(self.listaImena)
            #specificnaOsobaPitanje = "Jesi li ti mozda " + osoba + " ?"
            grupnoPitanje = random.choice(self.grupnaPitanja)
            if(grupnoPitanje == "Jesi li muskarac ? " or grupnoPitanje == "Jesi li zena ? "):
                self.grupnaPitanja.remove("Jesi li muskarac ? ")
                self.grupnaPitanja.remove("Jesi li zena ? ")
            if(grupnoPitanje == "Imas li kosu ? "):
                self.grupnaPitanja.remove("Imas li kosu ? ")
            if(grupnoPitanje == "Imas li bradu ? " ):
                self.grupnaPitanja.remove("Imas li bradu ? ")
            if(grupnoPitanje == "Imas li kapu ? "):
                self.grupnaPitanja.remove("Imas li kapu ? ")
            if(grupnoPitanje == "Imas li brkove ? "):
                self.grupnaPitanja.remove("Imas li brkove ? ")
            if(grupnoPitanje == "Imas li naocale ? "):
                self.grupnaPitanja.remove("Imas li naocale ? ")


            if msg:
                if substringPoruke in msg.body:
                    cijelaPoruka = msg.body.split(";")
                    odgovorProtivnika = cijelaPoruka[0]
                    pitanjeProtivnika = cijelaPoruka[1]
                    rijeci = pitanjeProtivnika.split() 
                else:
                    odgovorProtivnika = msg.body
                    rijeci = odgovorProtivnika.split()
                if odgovorProtivnika == "Pogodio si moju karticu. Cestitke pobijedio si!":
                    await self.agent.stop()
                print(f"Drugi agent : Primio sam poruku sadržaja: {msg.body}")
                if odgovorProtivnika == "Jesam, muskarac sam !":
                    for osoba in self.osobe:
                        if(osoba.spol == "zena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nisam muskarac ":
                    for osoba in self.osobe:
                        if(osoba.spol=="muskarac"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Jesam, zena sam":
                    for osoba in self.osobe:
                        if(osoba.spol=="muskarac"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nisam zena":
                    for osoba in self.osobe:
                        if(osoba.spol=="zena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam kosu":
                    for osoba in self.osobe:
                        if(osoba.imaKosu ==True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam kosu":
                    self.grupnaPitanja.extend(("Imas li plavu kosu ? ", "Imas li crnu kosu ? ", "Imas li narancastu kosu ? ", "Imas li bijelu kosu ? ", "Imas li smedu kosu ? "))
                    for osoba in self.osobe:
                        if(osoba.imaKosu==False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam naocale":
                    for osoba in self.osobe:
                        if(osoba.imaNaocale==True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam naocale":
                    self.grupnaPitanja.extend(("Imas li plave naocale ? ", "Imas li crne naocale ? ", "Imas li crvene naocale ? ", "Imas li bijele naocale ? ", "Imas li smede naocale ? "))
                    for osoba in self.osobe:
                        if(osoba.imaNaocale == False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam bradu":
                    for osoba in self.osobe:
                        if(osoba.imaBradu == True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam bradu":
                    self.grupnaPitanja.extend(("Imas li narancastu bradu ? ", "Imas li plavu bradu ? ", "Imas li crnu bradu ? ","Imas li smedu bradu ? "))
                    for osoba in self.osobe:
                        if(osoba.imaBradu == False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam kapu":
                    for osoba in self.osobe:
                        if(osoba.imaKapu == True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam kapu":
                    self.grupnaPitanja.extend(("Imas li zelenu kapu ? ", "Imas li plavu kapu ? ", "Imas li zutu kapu ? ", "Imas li sivu kapu ? "))
                    for osoba in self.osobe:
                        if(osoba.imaKapu == False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam brkove":
                    for osoba in self.osobe:
                        if(osoba.imaBrkove == True):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam brkove":
                    self.grupnaPitanja.extend(("Imas li crne brkove ? ", "Imas li narancaste brkove ? ", "Imas li plave brkove ? ", "Imas li smede brkove ? "))
                    for osoba in self.osobe:
                        if(osoba.imaBrkove == False):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plave naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plave naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam crvene naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Crvena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam crvene naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Crvena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam bijele naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Bijela"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam bijele naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Bijela"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam crne naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam crne naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam smede naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala != "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam smede naocale":
                    for osoba in self.osobe:
                        if(osoba.bojaNaocala == "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam smede oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju != "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam smede oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju == "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam zelene oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju != "Zelena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam zelene oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju == "Zelena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plave oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plave oci":
                    for osoba in self.osobe:
                        if(osoba.bojaOciju == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam narancastu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade != "Narancasta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam narancastu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade == "Narancasta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plavu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plavu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam crnu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade != "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam crnu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade == "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam smedu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade != "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam smedu bradu":
                    for osoba in self.osobe:
                        if(osoba.bojaBrade == "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam crne brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova != "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam crne brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova == "Crna"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam narancaste brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova != "Narancasta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam narancaste brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova == "Narancasta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plave brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plave brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam smede brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova != "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam smede brkove":
                    for osoba in self.osobe:
                        if(osoba.bojaBrkova == "Smeda"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam zelenu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape != "Zelena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam zelenu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape == "Zelena"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam plavu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape != "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam plavu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape == "Plava"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam zutu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape != "Zuta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam zutu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape == "Zuta"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Imam sivu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape != "Siva"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Nemam sivu kapu":
                    for osoba in self.osobe:
                        if(osoba.bojaKape == "Siva"):
                            osobeZaIzbrisati.append(osoba)
                    for osoba in osobeZaIzbrisati:
                        self.osobe.remove(osoba)
                elif odgovorProtivnika == "Ti si " + self.mojaKartica + " !":
                    self.agent.stop()

                if(grupnoPitanje == "Imas li plave oci ? " and odgovorProtivnika=="Imam plave oci"):
                    self.grupnaPitanja.remove("Imas li plave oci ? ")
                    self.grupnaPitanja.remove("Imas li zelene oci ? ")
                    self.grupnaPitanja.remove("Imas li smede oci ? ")
                elif(grupnoPitanje == "Imas li plave oci ? " and odgovorProtivnika=="Nemam plave oci"):
                    self.grupnaPitanja.remove("Imas li plave oci ? ")
                elif(grupnoPitanje == "Imas li zelene oci ? " and odgovorProtivnika=="Imam zelene oci"):
                    self.grupnaPitanja.remove("Imas li plave oci ? ")
                    self.grupnaPitanja.remove("Imas li zelene oci ? ")
                    self.grupnaPitanja.remove("Imas li smede oci ? ")
                elif(grupnoPitanje == "Imas li zelene oci ? " and odgovorProtivnika=="Nemam zelene oci"):
                    self.grupnaPitanja.remove("Imas li zelene oci ? ")
                elif(grupnoPitanje == "Imas li smede oci ? " and odgovorProtivnika=="Imam smede oci"):
                    self.grupnaPitanja.remove("Imas li plave oci ? ")
                    self.grupnaPitanja.remove("Imas li zelene oci ? ")
                    self.grupnaPitanja.remove("Imas li smede oci ? ")
                elif(grupnoPitanje == "Imas li smede oci ? " and odgovorProtivnika=="Nemam smede oci"):
                    self.grupnaPitanja.remove("Imas li smede oci ? ")
                elif(grupnoPitanje == "Imas li plave naocale ? " and odgovorProtivnika=="Imam plave naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li plave naocale ? " and odgovorProtivnika=="Nemam plave naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                elif(grupnoPitanje == "Imas li crvene naocale ? " and odgovorProtivnika=="Imam crvene naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li crvene naocale ? " and odgovorProtivnika=="Nemam crvene naocale"):
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                elif(grupnoPitanje == "Imas li bijele naocale ? " and odgovorProtivnika=="Imam bijele naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li bijele naocale ? " and odgovorProtivnika=="Nemam bijele naocale"):
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                elif(grupnoPitanje == "Imas li crne naocale ? " and odgovorProtivnika=="Imam crne naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li crne naocale ? " and odgovorProtivnika=="Nemam crne naocale"):
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                elif(grupnoPitanje == "Imas li smede naocale ? " and odgovorProtivnika=="Imam smede naocale"):
                    self.grupnaPitanja.remove("Imas li plave naocale ? ")
                    self.grupnaPitanja.remove("Imas li crvene naocale ? ")
                    self.grupnaPitanja.remove("Imas li bijele naocale ? ")
                    self.grupnaPitanja.remove("Imas li crne naocale ? ")
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li smede naocale ? " and odgovorProtivnika=="Nemam smede naocale"):
                    self.grupnaPitanja.remove("Imas li smede naocale ? ")
                elif(grupnoPitanje == "Imas li narancastu bradu ? " and odgovorProtivnika=="Imam narancastu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li narancastu bradu ? " and odgovorProtivnika=="Nemam narancastu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                elif(grupnoPitanje == "Imas li plavu bradu ? " and odgovorProtivnika=="Imam plavu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li plavu bradu ? " and odgovorProtivnika=="Nemam plavu bradu"):
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                elif(grupnoPitanje == "Imas li crnu bradu ? " and odgovorProtivnika=="Imam crnu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li crnu bradu ? " and odgovorProtivnika=="Nemam crnu bradu"):
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                elif(grupnoPitanje == "Imas li smedu bradu ? " and odgovorProtivnika=="Imam smedu bradu"):
                    self.grupnaPitanja.remove("Imas li narancastu bradu ? ")
                    self.grupnaPitanja.remove("Imas li plavu bradu ? ")
                    self.grupnaPitanja.remove("Imas li crnu bradu ? ")
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li smedu bradu ? " and odgovorProtivnika=="Nemam smedu bradu"):
                    self.grupnaPitanja.remove("Imas li smedu bradu ? ")
                elif(grupnoPitanje == "Imas li crne brkove ? " and odgovorProtivnika=="Imam crne brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li crne brkove ? " and odgovorProtivnika=="Nemam crne brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                elif(grupnoPitanje == "Imas li narancaste brkove ? " and odgovorProtivnika=="Imam narancaste brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li narancaste brkove ? " and odgovorProtivnika=="Nemam narancaste brkove"):
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                elif(grupnoPitanje == "Imas li plave brkove ? " and odgovorProtivnika=="Imam plave brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li plave brkove ? " and odgovorProtivnika=="Nemam plave brkove"):
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                elif(grupnoPitanje == "Imas li smede brkove ? " and odgovorProtivnika=="Imam smede brkove"):
                    self.grupnaPitanja.remove("Imas li crne brkove ? ")
                    self.grupnaPitanja.remove("Imas li narancaste brkove ? ")
                    self.grupnaPitanja.remove("Imas li plave brkove ? ")
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li smede brkove ? " and odgovorProtivnika=="Nemam smede brkove"):
                    self.grupnaPitanja.remove("Imas li smede brkove ? ")
                elif(grupnoPitanje == "Imas li zelenu kapu ? " and odgovorProtivnika=="Imam zelenu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                elif(grupnoPitanje == "Imas li zelenu kapu ? " and odgovorProtivnika=="Nemam zelenu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                elif(grupnoPitanje == "Imas li plavu kapu ? " and odgovorProtivnika=="Imam plavu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                elif(grupnoPitanje == "Imas li plavu kapu ? " and odgovorProtivnika=="Nemam plavu kapu"):
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                elif(grupnoPitanje == "Imas li zutu kapu ? " and odgovorProtivnika=="Imam zutu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                elif(grupnoPitanje == "Imas li zutu kapu ? " and odgovorProtivnika=="Nemam zutu kapu"):
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                elif(grupnoPitanje == "Imas li sivu kapu ? " and odgovorProtivnika=="Imam sivu kapu"):
                    self.grupnaPitanja.remove("Imas li zelenu kapu ? ")
                    self.grupnaPitanja.remove("Imas li plavu kapu ? ")
                    self.grupnaPitanja.remove("Imas li zutu kapu ? ")
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                elif(grupnoPitanje == "Imas li sivu kapu ? " and odgovorProtivnika=="Neman sivu kapu"):
                    self.grupnaPitanja.remove("Imas li sivu kapu ? ")
                
                #rijeci = msg.body.split()
                #print(rijeci[-2])
                if(rijeci[-2]==self.mojaKartica):
                    poruka1 = spade.message.Message(
                    to="posiljatelj@rec.foi.hr",
                    body = "Pogodio si moju karticu. Cestitke pobijedio si!",
                    metadata={
                    "ontology":"pitanje",
                    "language":"hrvatski"
                        }
                    )
                    await self.send(poruka1)
                    print("Prvi agent je pobijedio!")   
                    await self.agent.stop()
                if(rijeci[-2]=="muskarac"):
                    if(self.mojaOsoba.spol == "muskarac"):
                        self.odgovor = "Jesam, muskarac sam !;"
                    else:
                        self.odgovor = "Nisam muskarac;",
                        
                if(rijeci[-2]=="zena"):
                    if(self.mojaOsoba.spol == "zena"):
                        self.odgovor = "Jesam, zena sam !;"
                        
                    else:
                        self.odgovor = "Nisam zena ;"
                        
                if(rijeci[-2]=="kosu" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaKosu == True):
                        self.odgovor = "Imam kosu;"
                      
                    else:

                        self.odgovor = "Nemam kosu;"

                if(rijeci[-2]=="naocale" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaNaocale == True):
                        self.odgovor = "Imam naocale;"
                    else:
                        self.odgovor = "Nemam naocale;"

                if(rijeci[-2]=="brkove" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaBrkove == True):
                        self.odgovor = "Imam brkove;"
                    else:
                        self.odgovor = "Nemam brkove;"

                if(rijeci[-2]=="kapu" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaKapu == True):
                        self.odgovor = "Imam kapu;"
                    else:
                        self.odgovor = "Nemam kapu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="li"):
                    if(self.mojaOsoba.imaBradu == True):
                        self.odgovor = "Imam bradu;"
                    else:
                        self.odgovor = "Nemam bradu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="narancastu"):
                    if(self.mojaOsoba.bojaBrade=="Narancasta"):
                        self.odgovor = "Imam narancastu bradu;"
                    else:
                        self.odgovor = "Nemam narancastu bradu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="plavu"):
                    if(self.mojaOsoba.bojaBrade=="Plava"):
                        self.odgovor = "Imam plavu bradu;"
                    else:
                        self.odgovor = "Nemam plavu bradu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="crnu"):
                    if(self.mojaOsoba.bojaBrade=="Crna"):
                        self.odgovor = "Imam crnu bradu;"
                    else:
                        self.odgovor = "Nemam crnu bradu;"
                if(rijeci[-2]=="bradu" and rijeci[-3]=="smedu"):
                    if(self.mojaOsoba.bojaBrade=="Smeda"):
                        self.odgovor = "Imam smedu bradu;"
                    else:
                        self.odgovor = "Nemam smedu bradu;"
                if(rijeci[-2]=="naocale" and rijeci[-3]=="plave"):
                    if(self.mojaOsoba.bojaNaocala=="Plava"):
                        self.odgovor = "Imam plave naocale;"

                    else:
                        self.odgovor = "Nemam plave naocale;"
                if(rijeci[-2]=="naocale" and rijeci[-3]=="crvene"):
                    if(self.mojaOsoba.bojaNaocala=="Crvena"):
                        self.odgovor = "Imam crvene naocale;"           
                    else:
                        self.odgovor = "Nemam crvene naocale;"
                if(rijeci[-2]=="naocale" and rijeci[-3]=="bijele"):
                    if(self.mojaOsoba.bojaNaocala=="Bijela"):
                        self.odgovor = "Imam bijele naocale;"
                    else:
                        self.odgovor = "Nemam bijele naocale;"
                if(rijeci[-2]=="naocale" and rijeci[-3]=="crne"):
                    if(self.mojaOsoba.bojaNaocala=="Crna"):
                        self.odgovor = "Imam crne naocale;"

                    else:
                        self.odgovor = "Nemam crne naocale;"
        
                if(rijeci[-2]=="naocale" and rijeci[-3]=="smede"):
                    if(self.mojaOsoba.bojaNaocala=="Smeda"):
                        self.odgovor = "Imam smede naocale;"
                    else:
                        self.odgovor = "Nemam smede naocale;"
                if(rijeci[-2]=="oci" and rijeci[-3]=="smede"):
                    if(self.mojaOsoba.bojaOciju=="Smeda"):
                        self.odgovor = "Imam smede oci;"
                    else:
                        self.odgovor = "Nemam smede oci;"
                if(rijeci[-2]=="oci" and rijeci[-3]=="zelene"):
                    if(self.mojaOsoba.bojaOciju=="Zelena"):
                        self.odgovor = "Imam zelene oci;"
                    else:
                        self.odgovor = "Nemam zelene oci;"
                if(rijeci[-2]=="oci" and rijeci[-3]=="plave"):
                    if(self.mojaOsoba.bojaOciju=="Plava"):
                        self.odgovor = "Imam plave oci;"
                    else:
                        self.odgovor = "Nemam plave oci;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="smede"):
                    if(self.mojaOsoba.bojaBrkova=="Smeda"):
                        self.odgovor = "Imam smede brkove;"
                    else:
                        self.odgovor = "Nemam smede brkove;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="crne"):
                    if(self.mojaOsoba.bojaBrkova=="Crna"):
                        self.odgovor = "Imam crne brkove;"
                    else:
                        self.odgovor = "Nemam crne brkove;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="narancaste"):
                    if(self.mojaOsoba.bojaBrkova=="Narancasta"):
                        self.odgovor = "Imam narancaste brkove;"
                    else:
                        self.odgovor = "Nemam narancaste brkove;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="plave"):
                    if(self.mojaOsoba.bojaBrkova=="Plava"):
                        self.odgovor = "Imam plave brkove;"
                    else:
                        self.odgovor = "Nemam plave brkove;"
                if(rijeci[-2]=="brkove" and rijeci[-3]=="narancaste"):
                    if(self.mojaOsoba.bojaBrkova=="Narancasta"):
                        self.odgovor = "Imam narancaste brkove;"
                    else:
                        self.odgovor = "Nemam narancaste brkove;"
                if(rijeci[-2]=="kapu" and rijeci[-3]=="zelenu"):
                    if(self.mojaOsoba.bojaKape=="Zelena"):
                        self.odgovor = "Imam zelenu kapu;"
                    else:
                        self.odgovor = "Nemam zelenu kapu;"
                if(rijeci[-2]=="kapu" and rijeci[-3]=="plavu"):
                    if(self.mojaOsoba.bojaKape=="Plava"):
                        self.odgovor = "Imam plavu kapu;"
                    else:
                        self.odgovor = "Nemam plavu kapu;"
                if(rijeci[-2]=="kapu" and rijeci[-3]=="zutu"):
                    if(self.mojaOsoba.bojaKape=="Zuta"):
                        self.odgovor = "Imam zutu kapu;"
                    else:
                        self.odgovor = "Nemam zutu kapu;"
                if(rijeci[-2]=="kapu" and rijeci[-3]=="sivu"):
                    if(self.mojaOsoba.bojaKape=="Siva"):
                        self.odgovor = "Imam sivu kapu;"
                    else:
                        self.odgovor = "Nemam sivu kapu;"




            

            #self.osobe.remove(osoba) 
            msg = spade.message.Message(
                to="posiljatelj@rec.foi.hr",
                body = self.odgovor + grupnoPitanje,
                metadata={
                    "ontology":"pitanje",
                    "language":"hrvatski"
                }
            )
            await self.send(msg)
            print("Drugi agent: Pitanje poslano!")    
            
        
    async def setup(self):
        print("Drugi agent: Pokrećem se!")
        ponasanje = self.PrimiIPosaljiPoruku(period=5)
        #ponasanje2 = self.PrimiPoruku(period=20)
        self.add_behaviour(ponasanje)
        #self.add_behaviour(ponasanje2)
        
if __name__ == '__main__':
    tkoPrviIgra = random.uniform(1,2)
    osobe =[]
    #osobe.append(Osoba.ucitajKartice())
    grupnaPitanja = ["Jesi li muskarac ? ","Jesi li zena ? ","Imas li kosu ? ","Imas li bradu ? ","Imas li kapu ? ","Imas li brkove ? ","Imas li naocale ? "]
    specificnaPitanja = ["Imas li plavu kosu ? ","Imas li crnu kosu ? ","Imas li narancastu kosu ? ","Imas li bijelu kosu ? ", "Imas li sivu kapu ? ", "Imas li zelenu kapu ? ", "Imas li zutu kapu ? "," Imas li plavu kapu ? ","Imas li crne brkove ? ","Imas li smede brkove ? "]

    #if(tkoPrviIgra == 1):
     #   prviAgent = PrviAgent()
    #else:
        #drugiAgent = DrugiAgent
    prviAgent = PrviAgent("posiljatelj@rec.foi.hr","tajna")
    prviAgent.start()
    drugiAgent = DrugiAgent("ares@rec.foi.hr", "ratnik")
    drugiAgent.start()
    input("Press ENTER to exit.\n")
    prviAgent.stop()
    drugiAgent.stop()
    spade.quit_spade()
