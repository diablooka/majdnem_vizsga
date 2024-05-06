class Verseny:
    def __init__(self, ev, orszag, varos, arany, ezust, bronz):
        self.ev = ev
        self.orszag = orszag
        self.varos = varos
        self.arany:int = arany
        self.ezust:int = ezust
        self.bronz:int = bronz

aranyerem = 0
m_ermek = 0
versenyek = []
file = open("paralimpia.txt", "r", encoding="utf-8")
for sor in file:
    lista = sor.strip().split(";")
    v = Verseny(lista[0], lista[1], lista[2], int(lista[3]), int(lista[4]), int(lista[5]))
    versenyek.append(v)
    m_ermek += (v.arany + v.ezust + v.bronz)
    if v.arany > 0:
        aranyerem += 1
file.close()
print(f"ennyi verseny volt osszesen: {len(versenyek)}")
print(f"az elso versenyt ez az orszag rendezte: {versenyek[0].orszag}")
print(f"osszesen a magyarok ennyi ermet szereztek: {m_ermek}")
print(f"ennyi versenyen szereztek aranyermet a magyarok: {aranyerem}")
        