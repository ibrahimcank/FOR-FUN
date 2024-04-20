def anafonksiyon(islem_adi):

    def toplama(*args):
        toplam=0
        for i in args:
            toplam=toplam+i
        return toplam
    def çarpım(*args):
        çarpım=1
        for i in args:
            çarpım=çarpım*i
        return çarpım
    if islem_adi == "toplama":
        return toplama
    else:
        return çarpım
fonk= anafonksiyon("toplama")
print(fonk(1,2,3,4,5,6,7))
fonk2= anafonksiyon("çarpım")
print(fonk2(1,2,3,4,5,6,7))
#argüman olarak gönderme

def toplama(a,b):
    return a+b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a*b
def bölme(a,b):
    return a/b
def anafonksiyon(func1,func2,func3,func4,islem_adi):
    if islem_adi=="toplama":
        print(func1(3,4))
    elif islem_adi=="çıkarma":
        print(func2(10,3))
    elif islem_adi=="çarpma":
        print(func3(3,5))
    elif islem_adi=="bölme":
        print(func4(10,4))
    else:
        print("geçersiz islem")
anafonksiyon(toplama,çıkarma,çarpma,bölme,"toplama")
anafonksiyon(toplama,çıkarma,çarpma,bölme,"çarpma")
anafonksiyon(toplama,çıkarma,çarpma,bölme,"çıkarma")
anafonksiyon(toplama,çıkarma,çarpma,bölme,"bölme")