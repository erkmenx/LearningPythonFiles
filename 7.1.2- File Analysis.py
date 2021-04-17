### Diyelim ki kaç satır olduğunu bulmak istiyoruz. ####


erko23 = open ("mail.txt", "r")
sayac = 0
for peynir in erko23:
    sayac=sayac+1

print("Toplam satir sayisi:",sayac)

#### Bütün metni bir string halinde okuyabiliriz.

erko2323 = open ("mail.txt")
giris = erko2323.read()
print(len(giris)) ##veya
print(giris[:90]) ##olarak okunabilir

##### dosya içerisinde satırın başlama stringine göre arama yapma:
erko31 = open("mail.txt")
for satir in erko31:
    if satir.startswith('From stephe'):
        print(satir)

### fakat goruldugu uzere bir cok bos satır geliyor. sebebi print fonksiyonunun hali hazırda
### \n karakterine sahip olması. ama satırların sonunda da\n olduğundan \n\n oluyor.
### strip ile bunu çözebiliriz.

erko31 = open("mail.txt")
for satir in erko31:
    if satir.startswith('From stephe'):
        print(satir.rstrip())
#### in kullanarak da seçebiliriz.
erko31 = open("mail.txt")
for satir in erko31:
    satir=satir.rstrip()
    if not '@uct.ac.za' in satir:
        continue
    print(satir)

### ## INPUT'TAN DOSYA SEÇTİRİP OKUMAK

dosyaadi = input("Dosya adi giriniz:  ")
dosya = open(dosyaadi)
sayac=0
for satir in dosya:
    if satir.startswith("Subject"):
        sayac=sayac +1
print("There were", sayac, "subject lines")

dosyaadi = input("nabtin iyimisin")


### quit() try: dosyayı açma except: quit() olarak kodu kesebiliriz.
