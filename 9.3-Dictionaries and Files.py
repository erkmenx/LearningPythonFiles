#### Sayım yapan doku:


print('Bir cumle giriniz:')
cumle = input('')

kelimeler = cumle.split()

print('Kelimeler:', kelimeler)
counter = dict()

for sayi in kelimeler:
    counter[sayi] = counter.get(sayi, 0) + 1


print(counter)




### for loop to a dictionary


for key in counter:
    print(key, counter[key])

print(list(counter))

print(counter.keys())

print(counter.items())  ##tuple yapısı


for aaa,bbb in counter.items():
    print(aaa,bbb)
