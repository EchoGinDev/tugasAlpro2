gajiPer_jam = float(input("Masukkan gaji per jam yang diinginkan: "))
jamKerja_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))

gajiKotor = gajiPer_jam * (5*jamKerja_per_minggu)
gajiBersih = gajiKotor - (gajiKotor*0.14)
pembelian_pakaian_aksesoris = gajiBersih - (gajiBersih*0.10)
pembelian_alatTulis = pembelian_pakaian_aksesoris - (gajiBersih * 0.1)
sedekah = pembelian_alatTulis - (pembelian_alatTulis*0.25)
sedekahYatim = ((sedekah * 0.30) // 1000) * 100
dhuafa = sedekah - sedekahYatim

print("1. Pendapatan Budi selama liburan musim panas sebelum melakukan pembayaran pajak:", gajiKotor)
print("2. Pendapatan Budi selama liburan musim panas setelah melakukan pembayaran pajak:", gajiBersih)
print("3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris:", pembelian_pakaian_aksesoris)
print("4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis:", pembelian_alatTulis)
print("5. Jumlah uang yang akan Budi sedekahkan:", sedekah)
print("6. Jumlah uang yang akan diterima anak yatim:", sedekahYatim)
print("7. Jumlah uang yang akan diterima kaum dhuafa:", dhuafa)


