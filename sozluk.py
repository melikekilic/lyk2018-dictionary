sozluk={"elma":"apple",
	"havuç":"carrot",
	"muz":"banana",
	"üzüm":"graps"}
ters={}

for a,b in sozluk.items():
	ters[b]=a
print(ters)
print(sozluk)
print("-----------------------------------")
kelime=input("çevirmek istediğiniz kelime : ")
print("-----------------------------------")
for x in sozluk:
	if(kelime==x):
		print(sozluk.get(kelime))
for y in ters:
	if(kelime==y):
		print(ters.get(kelime))
