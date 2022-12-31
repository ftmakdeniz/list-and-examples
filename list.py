### LİST###


"""
liste = list()       #bos liste
liste2 = []          #bos liste pek tavsiye edilmez
liste3 = [2,"mehmet",2.5, False]

print(liste3)
for element in liste3:
    print(element)

#Listeye eleman eklemek

print(liste)
liste.append("Kelime") #Tavsiye edilen yöntem
liste +=[6]   #Tavsiye edilmeyen yöntem
print(liste)

"""

"""
liste = [1,2,3,4,"Muz","True"]

#listenin icindeki herhangi bir degere index numarasiyla erismek
print(liste[5])
sonuc = liste[5]
print(sonuc)

#Listeden eleman silme
del liste[1]  #tavsiye edilmeyen yöntem (deger arama ile)
print(liste)

liste.remove(3)   #tavsiye edilen (deger arama ile)
print(liste)

"""

"""
#Coklu veri ekleme
liste = list()

#1. yontem tavsiye edilmeyen
liste += ["Veli","Ali","Kenan"]
print(liste)

#2. yöntem tavsiye edilen
liste.append("Kerim")
liste.append("Kemal")
liste.append("Kadir")
print(liste)

#Eleman sayısına ulasmak
print(len(liste))
print(liste[-2]) #Tersten eleman okuma (index no ya göre)

#Liste parçalama
print(liste[0:2])   #id si 0 ve 1 olan elemanları alır ve liste olarak döner
print(liste[:2])    #id si en baştan 2'ye kadar olan eleman al 2 ye sahip olanı alma
print(liste[2:])    #id si 2 den sonraki elemanları al ve liste olarak dön
"""

"""
# listeye verilen index veri eklemem
rakamlar = [1,2,3,4,5,6,7,8]
print(rakamlar)
print(rakamlar[4])

#index değiştirme  index i 4 olan silip yerine Mavi kelimesini ekledik.
rakamlar[4] = "mavi"
print(rakamlar[4])
print(rakamlar)

#Araya eleman  eklemek
rakamlar.append("pembe")
print(rakamlar)
"""

"""
##Listedeki değerin index ine ulaşma
rakamlar = [1,2,3,4,5]
print(rakamlar.index(3))

sayilar = [10,20,40,10,30,60,10,20,40]
print(sayilar.index(20))    #ilk gördüğü 20 nın index ini verir
print(sayilar.index(10,3))  # aramaya 3 elemandan sonra baslar

### Listedeki bi değerin kaç defa tekrar ettiğini verir
print(sayilar.count(10))
"""
"""


#SORU: listedeki 10 değerlerin indexlerinii verir
sayilar = [10,20,40,10,30,60,10,20,40]

for sayi in range(len(sayilar)):
    if sayilar[sayi] == 10:
        print(sayi)
"""

"""

####LİSTE SIRALAMA#######
rakamlar = [1,5,4,6,9,2]
rakamlar.sort()     #küçükten büyüğe sırlama
print(rakamlar)

rakamlar.sort(reverse=True) #büyükten küçüğe sıralama
print(rakamlar)
"""

"""
###TÜRKÇE DİLİ AYARLAMA

import locale
locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")

sehirler = ["ZONGULDAK", "ÇANKIRI", "SİVAS","OSMANİYE","BURSA"]
sehirler.sort(key=locale.strxfrm)
print(sehirler)

sehirler.sort(key=locale.strxfrm, reverse=True)
print(sehirler) 
"""
"""

####listeden değer dışarı atma
rakamlar = [1,52,41,635,885,9663,852,741,54888]
print(rakamlar)
rakamlar.pop()  #varsayılan olarak son elemanı lısteden siler
print(rakamlar)

rakamlar.pop(2)  #index e göre elemanı siler
print(rakamlar)

rakamlar.remove(52)  #Yazılan değere göre siler
print(rakamlar)

## Bir değerrin listede olup olmadığını kontrol etmek
deger =545485
if deger in rakamlar:
    rakamlar.pop(rakamlar.index(deger))
print(rakamlar)

sehirler = ["ZONGULDAK", "ELAZIĞ", "İZMİR", "ANTALYA" ]

if "ELAZIĞ" in sehirler:
    print("Elazığ listede")

"""

"""

#Liste Birleştirme
liste1 = [1,2,3]
liste2 = [4,5,6]
birlesmis = liste1 + liste2  #birinci yöntem
print(birlesmis)

#İkinci Yöntem
listem = list()
for i in liste1:
    listem.append(i)
for i in liste2:
    listem.append(i)
print(listem)
print(max(listem)) #listedeki en büyük eleman degerini verir
print(min(listem)) #listedeki en küçük elemanın degerini veriri
"""

"""
# Tek satırda for yazma işlemi
liste = list()

for sayi in range(1,11):
    liste.append(sayi)

print(liste)

rakamlar = [ sayi for sayi in range(1,11) ]
print(rakamlar)

"""
"""
### SORU 10 ile 100 arasındaki çift sayıları bir listeye atın
rakamlar = [sayi for sayi in range(10, 101, 2)]
print(rakamlar)

cift_sayilar = list()
for sayi in range(10, 101 ,2):
    cift_sayilar.append(sayi)
print(cift_sayilar)
"""

liste = [44, 33, 55, 66, 77]

"""
liste2 = liste  #liste değişkenin ramdaki adresi
liste.append("Ali")
print(liste2)

liste2 = liste.copy()  #yeni adres olustur ve içine listedeki degeri atar
print(liste)
print(liste2)
liste.append("Fatma")
print(liste)
"""

"""
###  ALISTIRMALAR  ###
# SORU 1 : kullanıcıdan 10 adet sayı alıp listeye atın
# sonrasında listenin aritmetik ortalamasını bulun

sayi_listesi = list()
for i in range(1,11):
    sayi = int(input(f"{i}.sayinizi:"))
    sayi_listesi.append(sayi)
print(sum(sayi_listesi)/len(sayi_listesi))
"""

"""
## SORU 2 : 1-150 arasında 20 adet rastgele sayi üretin ve
# aynı numara içerde olmayan listeye atın.

import random
sayilar = list()
while len(sayilar)<20:
    sayi = random.randint(1,150)
    if sayi not in sayilar:
        sayilar.append(sayi)
print(sayilar)

sayilar2 = list()
for i in range(1,40):
    if len(sayilar2) < 20:
        sayi =random.randint(1,20)
        if sayi not in sayilar2:
            sayilar2.append(sayi)
        else:
             continue
    else:
        break
print(len(sayilar))
print(len(sayilar2))

tek_sayilar =list()
cift_sayilar =list()
for i in sayilar:
    if i %2 ==0:
        cift_sayilar.append(i)
    else:
        tek_sayilar.append(i)
print(tek_sayilar)
print(cift_sayilar)
"""
"""
### SORU 3: klavyeden alınan 5 kelimeyi bir listeye atın.
# Girilen 7. kelimenin listede olup olmadığını ekrana yazdırınız.

sayac = 1
kelimeler = list()

while sayac < 7:
    kelime = input("kelimeyi girin")
    if sayac < 7:
        if kelime not in kelimeler:
            kelimeler.append(kelime)
            sayac +=1
        else:
            print(f"Bu kelime zaten listede mevcut KELİME: {kelime}")
    else:
        if kelime in kelimeler:
            print(f"{kelime} kelimesi kelimeler listesinde mevcut")
            break
        else:
            print(f"{kelime} kelime kelimeler listesinde mevcut değil")
            break
"""

"""
####  COK BOYUTLU LİSTELER   ###
cokBoyutlu = [[1,2, [9,8,7]],[4,5,6]] # 2x3 matris(liste)
print(cokBoyutlu[0][0])
print(cokBoyutlu[0][1])
print(cokBoyutlu[0][2])
print(cokBoyutlu[1][0])
print(cokBoyutlu[1][1])
print(cokBoyutlu[1][2])

print(cokBoyutlu[0][2][2])

"""
