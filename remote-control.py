import random
import time

class Kumanda():


    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if (self.tv_durum=="Açık"):
            print("televizyon zaten açık")
        else:
            print("televizyon açılıyor")
            self.tv_durum="açık"

    def tv_kapat(self):
        if (self.tv_durum=="kapalı"):
            print("televizyon zaten kapalı")
        else:
            print("tv kapanıyor")
            self.tv_durum="kapalı"
    def ses_ayarlari(self):
        while True:
            cevap=input("sesi azalt: <\nsesi arttır: >\n çıkış: çıkış ")

            if cevap=="<":
                if self.tv_ses !=0:
                    self.tv_ses-=1
                    print("ses",self.tv_ses)
            elif cevap==">":
                if self.tv_ses!=31:
                    self.tv_ses+=1
                    print("ses",self.tv_ses)
            else:
                print("ses güncellendi",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi")

    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele]

        print("şu anki kanal",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)
kumanda=Kumanda()  
print("""

Televizyon uygulaması

1.tv aç
2.tv kapat
3.ses ayarları
4.kanal ekle
5.kanal sayısını öpğrenme
6.rasgele kanal geçme

çıkmak için q yas basın



""")
            
while True:
    islem=input("işlemi seçiniz:")

    if islem=="q":
        print("kapatılıyor")
        break
    elif (islem=="1"):
        kumanda.tv_ac()
    elif (islem=="2"):
        kumanda.tv_kapat()
    elif (islem=="3"):
        kumanda.ses_ayarlari
    elif (islem=="4"):
        kumanda.kanal_listesi
    elif(islem=="5"):
        print("kanal sayisi",len(kumanda))
    elif(islem=="6"):
        kumanda.rastgele_kanal
    else:
        print("geçersiz islem")

