from datetime import datetime
import locale#çıktıyı türk.e yapmak için
locale.setlocale(locale.LC_ALL,"")#çıktıyı türk.e yapmak için
print(datetime.now())

şu_an=datetime.now()
print(şu_an.year)
print(şu_an.month)
print(şu_an.minute)
print(şu_an.microsecond)
print(şu_an.hour)

print(datetime.ctime(şu_an))

print(datetime.strftime(şu_an,"%y"))#sadeye yıl bilgisini almak için kullanılır
print(datetime.strftime(şu_an,"%B"))#ay bilgisi için
print(datetime.strftime(şu_an,"%A"))#gün ismi için
print(datetime.strftime(şu_an,"%X"))#saat bilgisi için
print(datetime.strftime(şu_an,"%D"))#gün bilgisi içib

print(datetime.strftime(şu_an,"%Y %B %A"))


saniye=datetime.timestamp(şu_an)#şu anki zamanın saniye cinsinden görmek
print(saniye)

şu_an2=datetime.fromtimestamp(saniye)#saniyeyi datetime objesine çevirir
print(şu_an2)

a=datetime.fromtimestamp(0)
print(a)
#çıktı olarak 1970 çıkıyor bilgisayarcılar için milad 1970 seçilmiştir

tarih=datetime(2019,12,1)
şimdi=datetime.now
print(şimdi-tarih)#2 tarih arasındaki farkı hesaplama