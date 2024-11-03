# kasus
# manusia

class Ibu:
    def __init__(self,panggilan,sifat):
        self.panggilan = panggilan
        self.__sifat__ = sifat

    def memanggil(self):
        print("Iya, Ada Apa ?")
    def setSifat(self,sifat):
        self.__Sifat = sifat
    def getSifat(self):
        return self.__sifat

class Anak(Ibu):
    def suruh(self):
        print("nanti dulu deh")
        

sekolah = Anak("Ucok","Malas")

print("Siapa nama anak ini ? {nama_anak}".format(nama_anak = sekolah.panggilan))
sekolah.memanggil()