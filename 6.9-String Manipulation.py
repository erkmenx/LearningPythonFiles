fruit = 'bananas'
if 'x' in fruit:            #####   String içerisinde harf kontrolü
    print("Var")
else:
    print("Yok anam valla")
                            #### String karşılaştırma
if fruit == 'bananas':
    print("Aynisi be gulum")

selam = 'Nabiyon Len'

kucult = selam.lower()       ##### Harfleri küçülten fonksiyon, upper da büyültür.
print(kucult)

##Veya bu şekilde de çalışır
print(selam.lower())

### Bunun gibi metotları içeren site:  docs.python.org/3/library/stdtypes.html#string-methods.
## Büyük harfle başlat diğerlerini küçülten fonks:
print(fruit.capitalize())
print(selam.capitalize())

## String içerisinde arama yapma
meyve = 'ananas'
kactane = meyve.find('na')
print(kactane)                  #### ilk 'na' aramasını bulduğu indexi out olarak verir.

### Arama yapıp, yer değiştirme ###

yerdegis = meyve.replace('na','X')
print(yerdegis)                  ##### bütün 'na' ları 'X' ile değiştirir.


#### Başlardaki ya da sonlardaki boşlukları silme [STRIP] ####

boslukluyazi= '    Selamin aleykum   '
print(boslukluyazi.lstrip())
print(boslukluyazi.rstrip())
print(boslukluyazi.strip())

#### Başlangıç kontrolü .startswith('X') ####

print(meyve.startswith('ana'))

### Ayırma ve çıkarım yapmak ####

bilgi = "muhammederkmen@gmail.com tarafından 05.07.2021 tarihinde gönderildi"
kontrol = bilgi.find('@')
print(kontrol)            #### kontrol değeri, @'in index değerini vermektedir.
kontrol2 = bilgi.find(' ',kontrol)      ### @'ten sonraki kısımdaki ilk boşluğu arıyor.
print(kontrol2)         #kontrol2 indexi

saglayici = bilgi[kontrol+1:kontrol2]
print(saglayici)
