# Tipe Data, Variabel, Nilai, dan Ekspresi, Halaman 26
# Susunan Algoritma yang membaca data barang berupa nama_barang, harga_lama, dan harga_baru, kemudian menghitung perubahan_harga serta persenmtase perubahan

print('Membaca data barang dan menampilkanperubahan harganya')

nama_barang = str(input('Masukkan nama barang : '))
harga_lama = int(input('Masukkan harga lama : '))
harga_baru = int(input('Masukkan harga baru : '))

perubahan = harga_baru - harga_lama
persentase = 100*(perubahan/harga_lama)

print(30*'=')

print('Nama Barang :', nama_barang)
print('Harga Lama :', harga_lama)
print('Harga Baru :', harga_baru)
print('Perubahan Harga :', perubahan)
print('Persentase Perubahan :', persentase)
if harga_lama < harga_baru:
    print('Perubahan Positif berarti kenaikan harga')
elif harga_lama > harga_baru:
    print('Perubahan Negatif berarti penurunan harga')
else:
    print('Tidak ada perubahan harga')