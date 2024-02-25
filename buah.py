# harga per kilo/buang untuk setiap jenis buah :
harga_jeruk = 15000
harga_apel = 30000
harga_mangga =20000
harga_manggis =7000
harga_durian =50000


#jummlah barang yang dibeli:
jumlah_jeruk = 3
jumlah_apel  = 2
jumlah_mangga = 0
jumlah_manggis = 5
jumlah_durian  = 2

#menghitung total pembayaran untuk setiap  jenis buah :
total_jeruk = harga_jeruk * jumlah_jeruk
total_apel = harga_apel * jumlah_apel
total_mangga = harga_mangga * jumlah_mangga
total_manggis = harga_manggis * jumlah_manggis
total_durian = harga_durian * jumlah_durian

#menghitung total pembayaran keseluruhan :
total_pembayaran = total_jeruk + total_apel + total_mangga + total_manggis + total_durian

#menampilkan total pembayaran :
print("total yang harus dibayar adalah")
print(f"{jumlah_jeruk}kilo jeruk = {total_jeruk}")
print(f"{jumlah_apel}kilo apel = {total_apel}")
print(f"{jumlah_mangga}kilo mangga = {total_mangga}")
print(f"{jumlah_manggis}kilo manggis = {total_manggis}")
print(f"{jumlah_durian}buah durian = {total_durian}")
print("total pembayaran:", total_pembayaran)