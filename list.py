print ('\nLIST_________________________________')
### LIST
#adalah struktur data pada python 
#yang mampu menyimpan lebih dari satu data

## Membuat list (variabel = [])
print ('\n________________________membuat list')
data1 = [2,4,8,16,32,64,128]
print (data1) 

## Mengambil data list
    #menggunakan index dari list dimulai dari 0
    #contoh: index data angka 8 pada list data1 adalah index ke 2
print ('\n_________________mengambil data list')
subdata1 = data1 [2] #ambil data index ke 2
subdata2 = data1 [-2] #minus untuk mengambil data dari belakang 
subdata3 = data1 [0:4] #ambil data dari index 0 sampai index(3)
subdata4 = data1 [-2:] #ambil dari belakang index 2 sampai kebelakang
subdata5 = data1 [2:] #ambil data dari index 2 sampai seterusnya
subdata6 = data1 [:4] #ambil data dari index 0 sampai 3
print ('Data index ke-2 adalah', subdata1)

## Menambah list
print ('\n__________________menambah data list')
data2 = [100,10,300,400,800,450]
data3 = data1 + data2
print (data3)

## Merubah data list
print ('\n___________________merubah data list')
print ('Data1 awal :', data1) 
data1 [4] = 1996 #ubah data1 index 3 dengan angka 1996 
print ('Data1 akhir:', data1)

    # Merubah dengan metode sliching
print ('\nData2 awal :', data2) 
data2 [2:4] = [77,44] #ubah data2 dari index 2 sampai 3 menjadi 77,44
print ('Data2 akhir:', data2)


## List dalam list
print ('\n_____________________list dalam list')
ldl = [data1, data2]
print ('list dlm list: ', ldl)

    #MENGAKSES LIST DALAM MULTIDIMENSIONAL LIST
akses = ldl [0][3]  #[0] memilih list data1, untuk kemilih list data2, isi [1]
                #[3] memilih dari data indek ke 3 dari list yg di pilih
print ('\nData1:', data1)
print ('Data2:', data2)
print ('Data akses dari list dlm list:', akses)

print ('\n')

## Beberapa method u/ memanipulasi list
print ('METODE MANIPULASI LIST_______________')
barang = ['hp','kamera','flashdisc']
print ('Data barang:', barang)

print ('\n_________________1.append')
barang.append ('mouse')  #menambah data (di akhir list)
print (barang)

print ('\n_________________2.extend')
barang.extend ('TG')
print (barang)


print ('\n_________________3.insert')
barang.insert (3,'mouse') #menambah data (bisa di tengah)
print (barang)


print ('\n__________________4.count')
jumlah = barang.count('mouse') #menghitung anggota dari list
print ('jumlah mouse pada list barang:',jumlah)


#menghapus data
print ('\n_________________5.remove')
barang.remove ('mouse') #hanya menghapus satu data di awal
print (barang)               #tidak menghapus semua data yang sama


#membalik isi list
print ('\n________________6.reverse')
barang.reverse ()
print (barang)

#MENGKOPI LIST KE DALAM LIST BARU
print ('\n________________kopi list')
ade = barang.copy()
ade.append ('sepatu')
print ('list barang =', barang)
print ('list ade =', ade)

#Menghitung banyaknya data dalam list
print ('\n______________________len')
n = [60,70,45,90,100,50,80,55]
a = len (n)
print ('Banyaknya data dlm list n adalah:' ,a)

print ('\n-->Sumber Kelas Terbuka')
