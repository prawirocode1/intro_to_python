#membuat list
fruits = ["apple","pisang","salak","semangka"]
#mencetak semua nilai
print(fruits)
#mencetak salah satu nilai
#namaVariabel[posisi_value]
#contoh semangka
print(fruits[3])
#misal nilainya min 
# print nilai terakhir
print(fruits[-1])
#menambahkan nilai
fruits.append("jeruk")
print(fruits)
#menambahkan nilai
print("=== menambahkan nilai list ====")
fruits.append("jeruk")
print(fruits)
#menghapus nilai (delete)
print("=== menghapus nilai nilai list ===")
fruits.remove("pisang")
print(fruits)
print("=== mengubah nilai list value jeruk menjadi mangga ===")
fruits[-1] = "mangga"
print(fruits)
print("=== reset nilai ===")
fruits.remove("mangga")
fruits.remove("jeruk")
print(fruits)
print("=== menambahkan 2 data atau lebih ===")
buah = ["tomat',alpukat"]
fruits = fruits + buah
print(fruits)
print("=== menambah 2 data atau lebih ===")
buah = ["tomat","alpukat"]
# fruits = fruits + buah
fruits += buah
print(fruits)
