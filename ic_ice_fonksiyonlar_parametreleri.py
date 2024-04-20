def fonksiyon(*args):#istediğimiz sayıda argüman gönderebiliriz
    for i in args:
        print(i)
print(fonksiyon(1,2,3))

def fonksiyon(isim,*args):
    print("isim: ",isim)
    for i in args:
        print(i)
print(fonksiyon("ibo",1,2,3,4,5,6,7))

def fonksiyon(**kwargs):
    print(kwargs)

print(fonksiyon(isim="ibo",soyisim="kacar",numara=9866305098))

def fonksiyon(**kwargs):
    for i,j in kwargs.items():
        print("argüman ismi",i,"argüman değeri",j)
print(fonksiyon(isim="can",soyisim="k",numara=9066305090))

def fonksiyon(*args,**kwargs):
    for i in args:
        print(i)
    print("-----------")
    for i,j in kwargs.items():
        print(i,j)
print(fonksiyon(isim="can",soyisim="k",numara=9066305090))

#iç içe fonksiyonlar
def selamla(isim):
    print("selam",isim)
selamla("ayşe")
merhaba=selamla
merhaba("ibo")
#del selamla # selamla fonksiyonunu siler ama tanımlanmış merhaba silinmez

def fonksiyon():
    
    def fonksiyon2():#lokal bir fonksiyon dışardan erişilemez
        print("kucuk fonksiyondan herkese merhaba")
    fonksiyon2()
    print("buyuk fonksiyondan herkese merhaba")
fonksiyon()

def fonksiyon(*args):
    
    def toplama(args):
        toplam=0
        for i in args:
            toplam+=i
            return toplam
    print(toplama(args))
fonksiyon(1,2,3,4,5,6,7)