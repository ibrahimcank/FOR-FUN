#bi bok anlamadım
def karelerial():
    sonuc=[]
    for i in range(1,6):
        sonuc.append(i**2)
    return sonuc
print(karelerial())

def karelerial():
    for i in range(1,6):
        yield i**2#bi bok anlamadım
generator=karelerial()
print(generator)
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
iterator2=iter(generator)
# print(next(iterator2))

liste=[i*3 for i in range(5)]
print(liste)
generator=(i*3 for i in range(5))
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield"{}x{}={}".format(i,j,i*j)
for i in carpimtablosu():
    print(i)
#hala bi bok anlamadım