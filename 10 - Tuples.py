### Tuplelar, 2 değerli listeler olarak nitelendirebiliriz. Değerleri değşitirlemez.


x= ('erko', 'ahmet', 'mehmet')

print(x[2])

### Listeler [] ile, tuplelar () ile yazılır

print(max(x))

### .sort , .append, .reverse, .flip gibi commandler çalışmaz.


###tuplelarda 2li veri tutulabilir.

(x,y) = (4, 'erko')

print(x)
print(y)

### dictionaries'te .items() komutu bir tuple oluşturur.

s = dict()
s['erko']=1
s['23']=2
for (x,y) in s.items():
    print(x)
    print(y)


### Tuplelarda soldan sağa doğru karşılaştırma yapılabilir
d=(5,2,4)
b=(2,5,7)
print(d<b)


###Tuplelarda da büyükten küçüğe sıralama yapılabilir: sorted(tuple)

dic = {'erko':23, 'baba':34, 'ahaha':66}

dic.items()

print(sorted(dic.items()))

### sorted() kullanımı

for a,b in sorted(dic.items()):
    print(a,b)
