import random

# Fungsi untuk mengubah angka menjadi teks
def angka_ke_teks(angka):
    if angka == 0:
        return "Batu"
    elif angka == 1:
        return "Gunting"
    elif angka == 2:
        return "Kertas"

# Fungsi untuk menentukan pemenang
def tentukan_pemenang(pemain, komputer):
    if pemain == komputer:
        return "Seri!"
    elif (pemain == 0 and komputer == 1) or (pemain == 1 and komputer == 2) or (pemain == 2 and komputer == 0):
        return "Anda menang!"
    else:
        return "Komputer menang!"

# Daftar pilihan
pilihan = ["Batu", "Gunting", "Kertas"]

# Mulai permainan
print("Selamat datang di permainan Gunting Batu Kertas!")
print("Pilih: 0 untuk Batu, 1 untuk Gunting, 2 untuk Kertas")

# Input pemain
while True:
    try:
        pilihan_pemain = int(input("Masukkan pilihan Anda (0/1/2): "))
        if pilihan_pemain < 0 or pilihan_pemain > 2:
            print("Pilihan tidak valid! Harap masukkan 0, 1, atau 2.")
            continue
        break
    except ValueError:
        print("Input tidak valid! Harap masukkan angka 0, 1, atau 2.")

# Pilihan komputer secara acak
pilihan_komputer = random.randint(0, 2)

# Tampilkan pilihan
print(f"\nAnda memilih: {angka_ke_teks(pilihan_pemain)}")
print(f"Komputer memilih: {angka_ke_teks(pilihan_komputer)}")

# Tentukan pemenang
hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
print(hasil)
