### Hafızayı kullanmanın birçok yolu var.

##Liste örneği


arkadaslar = ['Ahmet','Mehmet','Ali','Veli','49','50']
print(arkadaslar)
print(arkadaslar[1])
print(arkadaslar[2])        ## Bir liste boş olabilir: arkadaslar=[]

## Bir listenin içerisinde başka listeler olabilir

list = [2,3,4,[1,2,3],5]

print(list[3])


### Listeler değiştirilebilir, ekleme yapılabilir, çıkartma yapılabilir.

''' meyve = 'Muz'
meyve[0]='b' yaparsak çalışmayacaktır. '''

''' fakat '''

sayilar = [23,52,34,81]
print(sayilar)

sayilar[1]= 39
print(sayilar)       ### goruldugu üzere listler üzerinde değişiklik yapılabilir


### Listelerde kac eleman oldugunu bulma

print(len(sayilar))  ## Görüldüğü üzere 4 eleman var.


### For döngüsü yazma
index=0
for arkadas in arkadaslar:
    print('Happy Birthday',arkadas)
