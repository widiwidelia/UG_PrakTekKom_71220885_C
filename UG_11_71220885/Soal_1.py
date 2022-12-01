print("=========================")
print("Operasi Matematika")
print("1. Jumlah [+]")
print("2. Kurang [-]")
print("3. Kali [*]")
print("4. Bagi [/]")
print("=========================")
pilih = int(input("Pilih operasi (1/2/3/4): "))
print("=========================")

def penjumlahan(pertama, kedua):
    tambah = pertama + kedua
    return tambah

def pengurangan(pertama, kedua):
    kurang = pertama - kedua
    return kurang

def perkalian(pertama, kedua):
    kali = pertama * kedua
    return kali

def pembagian(pertama, kedua):
    bagi = pertama / kedua
    return bagi

pertama = int(input("Masukkan bilangan pertama: "))
kedua = int(input("Masukkan bilangan kedua: "))

if pilih == 1:
    print("Hasil operasi dari",pertama,"+",kedua,"=",penjumlahan(pertama, kedua))
elif pilih == 2:
    print("Hasil operasi dari",pertama,"-",kedua,"=",pengurangan(pertama, kedua))
elif pilih == 3:
    print("Hasil operasi dari",pertama,"*",kedua,"=",perkalian(pertama, kedua))
elif pilih == 4:
    print("Hasil operasi dari",pertama,"/",kedua,"=",pembagian(pertama, kedua))
