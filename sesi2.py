# Menghitung uang kembalian berdasarkan total belanja
def hitung_kembalian(total_belanja,uang_dibayarkan):
    kembalian = uang_dibayarkan - total_belanja
    return kembalian 

total_belanja = float(input("masukkan total belanja: "))
uang_dibayarkan = float(input("masukan jumlah uang yang dibayarkan:"))

kembalian =hitung_kembalian(total_belanja,uang_dibayarkan)
print("kembalian yang harus diberikan adalah",kembalian)


# Menghitung uang kembalian dengan diskon jika belanja lebih dari 70 ribu
def hitung_kembalian_diskon(total_belanja,uang_dibayarkan):
    if total_belanja > 70000:
       total_belanja*= 0.9 #diskon 10%
       kembalian = uang_dibayarkan-total_belanja
       return kembalian
   
total_belanja = float(input("Masukkan total belanja:"))
uang_dibayarkan = float(input("Masukan jumlah uang yang dibayarkan:"))
 
kembalian = hitung_kembalian_diskon(total_belanja,uang_dibayarkan)

print("kembalikan yang harus diberikan adalah :",kembalian)

#menghitung gaji karyawan
def hitung_gaji(gaji_pokok,uang_transport,uang_makan,tunjangan_jabatan,jam_lembur):
    gaji = gaji_pokok + uang_transport + uang_makan + tunjangan_jabatan 
    lembur = 1.5 * 1.2 * jam_lembur * gaji_pokok #menggunakan aturan lembur yang diberikan 
    total_gaji = gaji +lembur
    return total_gaji

gaji_pokok = float(input("masukkan gaji pokok:"))
uang_transport = float(input("masukkan uang transport:"))
uang_makan =  float(input("masukkan uang makan harian:"))
tunjangan_jabatan = float(input("masukkan tunjangan jabatan:"))
jam_lembur = float(input("masukkan jam lembur:"))

total_gaji = hitung_gaji(gaji_pokok,uang_transport,uang_makan,tunjangan_jabatan,jam_lembur)
print("total gaji karyawan adalah:",total_gaji)