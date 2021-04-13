tugas = int(input('Masukkan nilai tugas : '))
mid = int(input('Masukkan nilai mid : '))
final = int(input('Masukkan nilai final : '))

nilaiAkhir = (tugas*0.20) + (mid*0.30) + (final*0.50)

if nilaiAkhir >= 85:
    print('Nilai Akhir adalah A', nilaiAkhir)
elif 84 >= nilaiAkhir >= 70:
    print('Nilai Akhir adalah B', nilaiAkhir)
elif 55 >= nilaiAkhir >= 69:
    print("Nilai Akhir andalah C", nilaiAkhir)
else:
    print("Nilai Akhir andalah E", nilaiAkhir)