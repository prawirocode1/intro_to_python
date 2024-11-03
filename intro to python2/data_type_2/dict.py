# Inisialisasi Data
# format dasar
# nama variabel = { key:value , key1:value2 }
biodata_simple = {
    "nama" : "Pra Wiro Winoto",
    "age" : 30,
    "tempat_lahir" : "Jakarta"
}

# cetak nilai
print(biodata_simple)

# mengambil nilai spesifik
# biodata_simple("nama")
print("Hello nama anda siapa : {nama}".format(nama= biodata_simple["nama"]))
# biodata_simple.get("age")
print("{nama} , saya berumur : {age}".format(nama= biodata_simple.get("nama"),age = biodata_simple.get("age")))

# menambahkan key dan value
# biodata_simple.([tanggal_lahir] = "02-May-1990")
print("Data Setelah di update")
print(biodata_simple)

# mengubah nilai
biodata_simple["tanggal_lahir"] = "02-May-1990"
print("Setelah diganti format tanggal lahirnya")
print(biodata_simple)

# menghapus nilai
del biodata_simple["tanggal_lahir"]
print("Data setelah dihapus")
print(biodata_simple)


# check key yang ada
print("List key : ")
print(biodata_simple.keys())
print("list Value : ")
print(biodata_simple.values())
