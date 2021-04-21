pilihan = 'y'
while pilihan == 'y':
    NaBar = str(input("Masukkan nama Barang : "))
    HaSat = int(input("Harga satuan barang Rp. "))
    jumlah = int(input("Jumlah barang masing-masing : "))
    pilihan = input('Masih ingin berbelanja y/n?')

# Proses Perhitungan
Juhar = jumlah * HaSat





# HASIL PRINT
print("\nToko Serba_Ada")
print("jln. Mesjid Raya 25 Makasar")
print("\n\t\t\tDaftar Pembelian Barang")
print(65*'-')
print("No\t Nama Barang\t Jumlah\t Harga Satuan\t Jumlah-Harga")
print(65*'-')
i = 1
while i < 3:
    print(i , "\t " , NaBar, "\t\t  " + str(jumlah) + '\t  ' + str(HaSat) + '\t\t  ' + str(Juhar))
    i += 1
print(65*'-')
print("\t\t\t\tTotal Harga = " +"\tRp. "+ "1000")