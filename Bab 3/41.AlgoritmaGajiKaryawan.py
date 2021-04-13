nama = str(input('Masukkan Nama Karyawan : '))
golongan = str(input('Masukkan Golongan-nya : '))
jamKerja = int(input('Masukkan jam kerjanya : '))

if golongan == 'A':
    upah = 5000
elif golongan == 'B':
    upah = 5000
elif golongan == 'C':
    upah = 7500
elif golongan == 'D':
    upah = 9000
else:
    upah = 0
    print('Golongannya Salah!')

if jamKerja > 150:
    lembur = (jamKerja - 150)*upah*1.25
    gaji = jamKerja * upah
    total = gaji + lembur
    print("Gaji yang diterima sdr:", nama,"adalah = Rp.",total)
elif jamKerja <= 150:
    gaji = jamKerja*upah
    print("Gaji yang diterima sdr:", nama,"adalah = Rp.",gaji)