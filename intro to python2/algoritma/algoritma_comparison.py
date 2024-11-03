a = 10
b = 5
hasil = a > b # true
print("apakah {a} lebih besar dari (>) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
hasil = a < b # false
print("apakah {a} lebih kecil dari (<) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
a = 15
b = 2
hasil = a >= b # true
print("apakah {a} lebih besar sama dengan dari (>=) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
hasil = a <= b # false
print("apakah {a} lebih kecil sama dengan dari (<=) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
hasil = a == b
print("apakah {a} sama dengan (==) {b} adalah {hasil}".format(a=a,b=b,hasil=hasil))
# tidak sama dengan (!)
a = False 
hasil = a != True
print("apakah {a} tidak sama dengan (!=) True adalah {hasil}".format(a=a,hasil=hasil))