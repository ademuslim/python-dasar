### ~~~Latihan Komparasi dan Logika~~~~~~~~~~~~~~~~~~~~~~
### membuat area rentang dari angka
print ('\nKomparasi dan Logika___________________')

## +++++++3-----------10++++++++++
## memeriksa angka <3 atau >10)

inputUser = float (input('\nMasukan angka kurang dari 3\natau lebih dari 10--> '))
# +++++3-----------------
# memeriksa kurang dari 3
data_kurang_dari = inputUser < 3
print ('kurang dari 3 =' , data_kurang_dari)

# ------------10+++++++++
# memeriksa lebih dari 10
data_lebih_dari = inputUser > 10
print ('lebih dari 10 =' , data_lebih_dari)

# koreksi dari kedua syarat menggunakan or
koreksi = data_kurang_dari or data_lebih_dari
print ('Angka yang anda masukan adalah =', koreksi)


##-------3+++++++++++10-----------
##(memeriksa angka irisan antara rentang >3 dan <10 )
print ('\n_______________________________________')

inputUser1 = float (input('Masukan angka lebih dari 3\ndan kurang dari 10--> '))
# ------3+++++++++++++
# memeriksa lebih dari 3
data_lebih_dari_ = inputUser1 > 3
print ('lebih dari 3   =', data_lebih_dari_)

# ------------10+++++++++
# memeriksa kurang dari 10
data_kurang_dari_ = inputUser1 < 10
print ('kurang dari 10 =' , data_kurang_dari_)

# koreksi dari kedua syarat menggunakan and
koreksi2 = data_lebih_dari_ and data_kurang_dari_
print ('Angka yang anda masukan adalah =' ,koreksi2)
print ('\n_______________________________________')


### ----------0+++++++5--------8++++++++11--------
## syarat1 lebih dari 0 dan kurang dari 5 
## syarat2 lebih dari 8 dan kurang dari 11
print ('\n---0+++++5------8+++++11---')

data_ade = float(input('Masukan angka (>0,<5,>8,<11)--> '))
# syarat1 lebih dari 0 dan kurang dari 5
syaratA = data_ade >0
syaratB = data_ade <5
print ('data lebih dari 0   =', syaratA)
print ('data kurang dari 5  =', syaratB)
syarat1 = syaratA and syaratB 
print ('Syarat 1(>0,<5)     =', syarat1)

# syarat2 lebih dari 8 dan kurang dari 11
syaratX= data_ade >8
syaratY= data_ade <11
print ('data lebih dari 8   =', syaratX)
print ('data kurang dari 11 =', syaratY)
syarat2= syaratX and syaratY
print ('Syarat 2(>8,<11)    =', syarat2)

# eksekusi syarat 1 dan syarat 2
eksekusi = syarat1 or syarat2
print ('Angka yang anda masukan adalah =', eksekusi)
print ('\n_______________________________________')



## ++++++++0--------5++++++8--------11++++++
## syaratSatu kurang dari 0 (atau) lebih dari 11 
## syaratDua lebih dari 5 (dan) kurang dari 8
print ('\n+++0----5+++8----11+++')
data_mslm = float(input('Masukan angka (<0,>5,<8,>11)--> '))

# syaratSatu kurang dari 0 atau lebih dari 11
syaratP= data_mslm <0
syaratO= data_mslm >11
print ('data kurang dari 0 =', syaratP)
print ('data lebih dari 11 =', syaratO)
syaratSatu= syaratP or syaratO 
print ('Syarat1(<0,>5)     =', syaratSatu)

# syaratDua lebih dari 5 dan kurang dari 8
syaratF= data_mslm >5
syaratG= data_mslm <8
print ('data lebih dari 5  =', syaratF)
print ('data kurang dari 8 =', syaratG)
syaratDua = syaratF and syaratG 
print ('Syarat (>5,<11)    =', syaratDua)

# eksekusi syarat 7 dan syarat 8
eksekusi1 = syaratSatu or syaratDua
print ('Angka yang anda masukan adalah =', eksekusi1)


print ('\n-->Sumber Kelas Terbuka')



