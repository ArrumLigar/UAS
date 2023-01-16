class Kendaraan(object):
    
  def __init__(self, nama):
    self.nama = nama
    self.penumpang = []
    
  def tambah_penumpang(self, nama_penumpang):
    self.penumpang.append(nama_penumpang)
    
# membuat class pesawat yang merupakan turunan Kendaraan
class Pesawat(Kendaraan):
  pintu_terbuka = False
  
  def buka_pintu(self):
    self.pintu_terbuka = True
  def tutup_pintu(self):
    self.pintu_terbuka = False
    
pesnas = Pesawat("Garuda")

# pesnas akan memiliki properti dari Kendaraan
pesnas.tambah_penumpang("Alghifary")
print ("Penumpang: " + str(pesnas.penumpang))
# dan memiliki properti pesawat
pesnas.buka_pintu()
print ("Pintu terbuka: " + str(pesnas.pintu_terbuka))
