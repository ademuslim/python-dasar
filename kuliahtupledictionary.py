## Tupel
print ('Tupel___________________________________')

angka = (1,2,3,4,5,6,7,8,9,10)
print ('Data angka index ke-3 adalah {}'.format(angka [3]))
print ('Tipe data angka adalah',type(angka))

## Dictionary
print ('\nDictionary______________________________')

bilangan = {
        'genap':[2,4,6,8,10],
        'ganjil':[1,3,5,7,9]
}
print ('Angka pada data bilangan \n-ganjil adalah {}'.format(bilangan['ganjil']))
print ('Tipe data bilangan adalah {}'.format(type(bilangan)))

hewan = {
        'kucing': ['anggora','garong'],
        'ikan'  : ['koki','hiu'],
        'burung': ['pleci','jalak','elang']
}
print ('\nMacam2 burung \n-adalah {}'.format(hewan ['burung']))