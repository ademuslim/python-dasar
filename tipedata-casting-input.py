#~~~TIPE DATA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tipe data adlh macam2 data yg bisa d input dlm python
print ('\nTipe Data___________________')

# 1. tipe data integer (angka)
a = 12
print ("data variabel a :" , a, "\n-bertipe :", type(a))

# 2. tipe data float (angka dengan koma/desimal)
b = 12.5
print ("data variabel b :" , b, "\n-bertipe :", type(b))

# 3. tipe data string (karakter/hurup, harus pakai tanda kutip dua)
c = "ade muslim"
print ("data variabel c :" , c, "\n-bertipe :", type(c))

# 4. tipe data boolean (binner, hanya bernilai true/false)
d=True
print ("data variabel d :" , d, "\n-bertipe :", type(d))

# 5. tipe data khusus
# bilangan kompleks (contoh 10+5i i adalah imajiner)
e = complex(5,6)
print ("data variabel e :" , e, "\n-bertipe :", type(e))

#tipe data dari bahasa C U/ python (import terlebih dahulu)
from ctypes import c_double #tipe data bhs C double
f = c_double(10.5)
print ("data variabel f :" , f, "\n-bertipe :", type(f))


#~~~MENGAMBIL INPUT DATA USER & casting~~~~~~~~~~~~~~~~~~~
print ('\nInput Data___________________')

nama = input ('Masukan Nama : ')    #input u/ memasukan data
nim = int(input('Masukan NIM : '))  #data input nim dicasting menjadi integer (int)
print ('\nNAMA :', nama, '\nNIM :', nim)

#cek tipe data
print ('\nTipe data nama = ', type (nama))
print ('Tipe data nim = ', type (nim))

print ('\n-->Sumber Kelas Terbuka')
