# Tipe Data, Variabel, Nilai, dan Ekspresi,Contoh 3 Halaman 26 - 27

print('Menghitung gaya gravitasi di antara massa')

# Definisi variabel
G = 6.67*10**-11 #newton-m**2/kg**2

# Rincian Langkah
m1 = float(input('Masukkan massa 1 : '))
m2 = float(input('Masukkan massa 2 : '))
m3 = float(input('Masukkan massa 3 : '))

r12 = float(input('Masukkan jarak antara massa-1 dan massas-2 : '))
r13 = float(input('Masukkan jarak antara massa-1 dan massas-3 : '))
r23 = float(input('Masukkan jarak antara massa-2 dan massas-3 : '))\

# Meghitung Gaya Gravitasi
gaya = G*(m1*m2/r12+m1*m3/r13+m2*m3/r23)

print('Besar gaya di antara ketiga massa ini =', gaya)