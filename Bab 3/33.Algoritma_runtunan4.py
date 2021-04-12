nama = str(input('Masukkan Nama Pegawai : '))
gajipokok = int(input('Masukkan Gaji Pokok : '))

tunjangan = 0.25 * gajipokok
pajak = 0.15 * (gajipokok + tunjangan)
gajibersih = gajipokok + tunjangan - pajak
print("Gaji Saudara :", nama)
print("adalah = Rp.", round(gajibersih))
