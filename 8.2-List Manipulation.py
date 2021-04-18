####Listeler birbiri ardına eklenebilir.
a=[1,2,3,4]
b=[5,6,7,8]

c= a+b
print(c)

#### Listeler bir noktadan kesilebilir.


print(c[:4])
print(c[4:])
print(c[1:2])

 ########### metodlar için: https://docs.python.org/3/tutorial/datastructures.html



### listenin sonuna .append(item) ile ekleme yapılabilir.

c.append(66)
print(c)


### Listenin içinde olup olmadığını kontrol edebilirsiniz. X in Y

d= 66 in c
print(d)

d= 78 not in c
print(d)


### liste.sort() ile listenin içindekileri büyükten küçüğe sıralayabilirsin

c= b+a
print(c)
c.sort()
print(c)


### Listelerde sum(list), max değerini max(list), min(list), len(list)
### gibi komutlar ile işlem yapılabilir.

print(sum(c))
print(max(c))


### Ortalama hesaplayıcı counter

total=0
counter=0

while True:
    veri=input("Sayıyı giriniz")
    if veri=='Done':
        break
    total=total+int(veri)
    counter=counter+1

average= total/counter
print("Average is", average)


### 
