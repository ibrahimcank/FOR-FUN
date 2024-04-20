class Hayvanlar():
    def __init__(self,bacak_sayisi,uzunluk,agirlik,yasam_alani,tur):
        self.bacak_sayisi=bacak_sayisi
        self.uzunluk=uzunluk
        self.agirlik=agirlik
        self.yasam_alani=yasam_alani
        self.tür=tur
class Köpek(Hayvanlar):
    def __init__(self, bacak_sayisi, uzunluk, agirlik, yasam_alani,tur):
        super().__init__(bacak_sayisi, uzunluk, agirlik, yasam_alani,tur)
class Kus(Hayvanlar):
    def __init__(self, bacak_sayisi, uzunluk, agirlik, yasam_alani,tur):
        super().__init__(bacak_sayisi, uzunluk, agirlik, yasam_alani,tur)
class At(Hayvanlar):
    def __init__(self, bacak_sayisi, uzunluk, agirlik, yasam_alani,tur):
        super().__init__(bacak_sayisi, uzunluk, agirlik, yasam_alani,tur)

köpek1=Köpek(4,"80cm","20kg","kara","köpek")
kuş1=Kus(2,"10cm","1kg","hava","kuş")
at1=At(4,"2mt","100kg","kara","at")

print(f"bacak sayisi: {köpek1.bacak_sayisi}, uzunluk: {köpek1.uzunluk}, ağırlık: {köpek1.agirlik}, yaşam alanı: {köpek1.yasam_alani}, {köpek1.tür}")
print(f"bacak sayisi: {kuş1.bacak_sayisi}, uzunluk: {kuş1.uzunluk}, ağırlık: {kuş1.agirlik}, yaşam alanı: {kuş1.yasam_alani}, {kuş1.tür}")
print(f"bacak sayisi: {at1.bacak_sayisi}, uzunluk: {at1.uzunluk}, ağırlık: {at1.agirlik}, yaşam alanı: {at1.yasam_alani}, {at1.tür}")
