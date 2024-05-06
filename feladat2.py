import random

cicanevek:list[str] = ['Áfonya', 'Apolló', 'Apacs', 'Babett', 'Britney', 'Borsó', 'Crazy', 'Csipesz', 'Doris', 'Espresso', 'Elektra', 'Falánk', 'Gomez', 'Hópihe', 'Hilton', 'Írisz', 'Kása', 'Lidérc', 'Love', 'Lucifer', 'Masni', 'Misa', 'Mugli', 'Nárcisz', 'Nelson', 'Pocok', 'Picur', 'Rubin', 'Szurok', 'Szüttyő', 'Tigris', 'Tepsi', 'Úrfi', 'Vanília', 'Yoda', 'Zselé', 'Zakó', 'Zeusz']


nev = random.choice(cicanevek)

print(f"itt van egy random cicanev : {nev}")

ebetu = 0
for i in range(len(nev)):
    if nev[i] == "e":
        ebetu += 1
print(f"itt van egy random cicanev : {nev}, ennyi e betu van benne: {nev.count('e')} ")


kerdes = input("tetszik a nev?(I/N): ")
while kerdes != "I":
    print(f"uj javaslat: {random.choice(cicanevek)}")
    kerdes = input("tetszik a nev?(I/N): ")
    if kerdes == "I":
        print("rendben van")





