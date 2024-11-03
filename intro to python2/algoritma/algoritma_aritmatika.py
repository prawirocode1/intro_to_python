x = 10
y = 5

# penjumlahan
hasil = x + y 
print("hasil tambah dari {a} + {b} = {hasil} ".format(a=x,b=y,hasil=hasil))
# pengurangan
hasil = x - y 
print("hasil kurang dari {0} - {1} = {2} ".format(x,y,hasil))
# perkalian
hasil = x * y 
print("hasil kali dari {a} * {b} = {hasil} ".format(hasil=hasil,a=x,b=y))
# pembagian
hasil = x / y
print("hasil bagi dari {a} / {b} = {hasil} ".format(hasil=hasil,a=x,b=y))

# modulus
hasil = x % y 
print("hasil sisa bagi dari {a} % {b} = {hasil}".format(a=x,b=y,hasil=hasil))
# perpangkatan
hasil = x ** y
print("hasil dari pangkat {a} ^ {b} = {hasil}".format(a=x,b=y,hasil=hasil))
nilai = 0
# nilai= nilai + 1
nilai += 1
print("hasil dari nilai increment 0 = 0(old) + 1 : {nilai}".format(nilai=nilai))
nilai -= 1
print("hasil dari nilai increment 1 = 1(old) - 1 : {nilai}".format(nilai=nilai))
