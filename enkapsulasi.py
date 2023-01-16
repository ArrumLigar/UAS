class mahasiswi:
    def __init__ (self, nim,nama):
        self.nim = nim
        self.nama = nama
 
    def infoMahasiswi(self):
        print ('Identitas Mahasiswa:')
        print ('Nim =', self.nim)
        print ('Nama =', self.nama)
        
mhs = mahasiswi('20220801389','Arrum Ligar')
mhs.infoMahasiswi()