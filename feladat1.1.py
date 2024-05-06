x = int(input("kerem az elso szamot: "))
y = int(input("kerem a masodik szamot: "))

eredmeny = abs(x-y)
if eredmeny % 3 == 0:
    print(f"a ket szam kulonbsege oszthato harommal.")
else:
    print("a ket szam kulonbsege nem oszthato harommal.")