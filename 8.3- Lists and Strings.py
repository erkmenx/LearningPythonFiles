### Split Method ###

abc= 'Uc kelimeden olusur'

ornek=abc.split()
print(ornek)            ### Görüldüğü üzere split methodu bütün kelimeleri ayırıp listeye koydu.

for kelime in ornek:
    print(kelime)       ### Alt alta yazdırabiliyoruz


#### Split metodunda istediği kadar boşluk olsun, bütün boşlukları siler ve ayırır.

abc= 'Cok uzun              bosluk biraktin'

ornek2=abc.split()
print(ornek2)

### noktalama isaretleri alınır. split() içerisine , koyarsan değişir.

abc= 'naber, iyi senden , kanka'
ornek3=abc.split()
print(ornek3)
ornek3=abc.split(',')
print(ornek3)
####


### Uygulamada bir örnek.

dosya = open('shortmail.txt')
for line in dosya:
    line=line.rstrip()
    if not line.startswith('From '): continue  ###Eğer From ile başlamayan bir cümle varsa for'a geri dönüyor
    words = line.split()
    emails = words[1]
    usernames = emails.split('@')
    something = usernames[0]
    print(something)
