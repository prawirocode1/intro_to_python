#int
# (pagar) komentar
x = 1; # integer
print("ini contoh integer : {0}".format(x))
f = 10.5 # float
print("ini contoh nilai desimal : {0} ".format(f))
z = 2 + 3j # complex
print("ini contoh tipe data kompleks : {0} ".format(z))

# sequence type
a = [1,2,3] # list : nilainya harus sama dan boleh di ubah
print(a)
b = (4,5,6) # truple : nilainya tidak bisa diubah
print(b)
c = range(0,5) # range
print(c)

# type text
d = "hello , world!" # string (str)

# maping type
e = {"nama" : "alfadjri" , "age" : 24} # dict (dictionary)

# set type
f = {1,2,3} # set
g = frozenset ({4,5,6}) # frozenset

# boolean type (kondisi)
h = True; # bool (true(1), false(0)) ;
# binary type
i = b"hello" # bytes
print(i)
j = bytearray(5) # bytearray
print(j)
k = memoryview(bytes(5)) # memoryview
print(k)
