# ~~~OPERASI LOGIKA BOOLEAN~~~~~~~~~~~~~~~~~~~~~~~
# boolean (tipe data yang berisi True atau False)
# operasi logika not, or, and, xor
print ('\nOperasi Logika Boolean______________')

print ('\n_________ not ________')
a = True    #tipe dat bool
b = not a  #<-----b not a
print ('data bool A = ', a)
print ('data not  A = ', b)

print ('\n__________ or ________') #membedakan dua buah bool
# jika salah satu bernilai True maka hasilnya True, jika dua true tetap true
ade = True    #tipe data bool
lim = False
ms = ade or lim
print ('2 data bool = ', ade, 'dan', lim)
print ('data or dari 2 data bool: ', ms)
print (ade, 'or', lim, '=' ,ms)

print ('\n_________ and ________') #membedakan dua buah bool
# jika salah satu bernilai False maka hasilnya False
x = False    #tipe data bool
y = True
z = x and y
print ('2 data bool =',x, 'dan', y)
print ('data and dari 2 data bool =', z)
print (x, 'dan', y, '=', z)

print ('\n_________ xor ________') #membedakan dua buah bool
# akan true jika salah satu true, sisanya false
g = True    #tipe data bool
h = True
i = g ^ y #<------- simbol xor(^)
print ('2 data bool =', g, 'dan', h)
print ('data xor dari 2 data bool =', i)
print (g, 'xor', h, '=', i)





print ('\n-->Sumber Kelas Terbuka')












