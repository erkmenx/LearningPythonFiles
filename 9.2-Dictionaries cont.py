### Fazla değer olduğu zaman dict kullan.


a=dict()
a['erko']=1
a['23']=1

a['23'] = a['23']+1             ###Bu şekilde sayım yapılabilir.
print(a)

if 'erko' in a:                 ### in operatörü, arama yapılarak Boolean olarak kullanılabilir.
    print("He var knk")


### Liste içini sayan bir kütüphane:

sayim = dict()
isimler = ['ali', 'ahmet', 'mehmet', 'veli','49','50']

for isim in isimler:
    if isim not in sayim:
        sayim[isim] = 1
    else:
        sayim[isim] = sayim[isim] + 1

print(sayim)

### .get() metodu ile sayım yapmak:
sayim2=dict()
for isim in isimler:
    sayim2[isim] = sayim2.get(isim, 0)+1

print(sayim2)
