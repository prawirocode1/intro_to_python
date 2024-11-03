#kasus
# kita di suruh amati hewan

class Hewan: #Hewan itu nama class
    nama_hewan = "" # nama_hewan Object
    jenis_hewan = ""
    umur_hewan = 10 # object property dimana umur_hewan tidak bisa diubah private
    def __init__(self,nama,jenis): #contruktor
        self.nama_hewan = nama
        self.jenis_hewan = jenis

    def makan(self):
        print("Hewan sedang makan !!!")


# cara panggil
kucing = Hewan("tom","anggora")
# variable
print("nama kucing {nama}".format(nama = kucing.nama_hewan))
print("jenis kucing {jenis}".format(jenis = kucing.jenis_hewan))
print("umur hewan {umur}".format(umur = kucing.umur_hewan))
# manggil function atau method
print("Sedang apakah kucing ?")
kucing.makan()
