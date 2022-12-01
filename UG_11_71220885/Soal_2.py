print("Pemeriksa Kelipatan 9")
angka = int(input("Masukkan Kelipatan 9 yang ingin diperiksa: "))

def kelipatan_sembilan(angka):
    hasil = angka % 9
    return hasil

if kelipatan_sembilan(angka) == 0:
    print("Benar")
else:
    print("Salah")
