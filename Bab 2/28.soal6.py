pilihan = 'y'
while pilihan == 'y':
    print("""
    =================================

    SELAMAT DATANG
    DI KEDAI CEPAT SAJI
    ---------------------------------
    1. Burger           Rp. 5000,-
    2. Pizza Slice      Rp. 4500,-
    3. Kentang Goreng   Rp. 3000,-
    4. Soft Drink       Rp. 2500,-
    5. Milk Shake       Rp. 4000,-
    6. Air Mineral      Rp. 1500,-

    =================================
    """)

    pesan = int(input('Masukkan list nombor menu pesanan anda : '))
    jumlah_pesanan = int(input('Masukkan jumlah pesanan anda : '))
    if pesan == 1:
        nama = 'Burger'
        harga = 5000 * jumlah_pesanan
        ppn = harga * 0.1
        total = harga + ppn
    elif pesan == 2:
        nama = 'Pizza Slice'
        harga = 4500 * jumlah_pesanan
        ppn = harga * 0.1
        total = harga + ppn
    elif pesan == 3:
        nama = 'Kentang Goreng'
        harga = 3000 * jumlah_pesanan
        ppn = harga * 0.1
        total = harga + ppn
    elif pesan == 4:
        nama = 'Soft Drink'
        harga = 2500 * jumlah_pesanan
        ppn = harga * 0.1
        total = harga + ppn
    elif pesan == 5:
        nama = 'Milk Shake'
        harga = 4000 * jumlah_pesanan
        ppn = harga * 0.1
        total = harga + ppn
    elif pesan == 6:
        nama = 'Air Minerel'
        harga = 1500 * jumlah_pesanan
        ppn = harga * 0.1
        total = harga + ppn
    else:
        print('Nomor yang ada masukkan salah!!!')
        pilihan = input('Menu tidak tersedia, Silakan Masukkan nombor menu yang tersedia, silakan ulangi kembali y/n : ')

    print('\n\t=================================')
    print('\t|  Kedai Cepat Saji\t\t|')
    print('\t---------------------------------')
    print('\t|  Menu :',nama,'\t\t|')
    print('\t|  Jumlah Pesan :', jumlah_pesanan,'\t\t|')
    print('\t|  Harga :', harga,'\t\t|')
    print('\t|  PPN :', round(ppn),'\t\t\t|')
    print('\t---------------------------------')
    print('\t|  Total Harga :', round(total),'\t\t|')
    print('\t=================================')
    pilihan = input('Apkah anda ingin memesan lagi, y/n : ')