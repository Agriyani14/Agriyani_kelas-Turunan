class minuman(object):
   def __init__(self, i):
      self.minuman = i
   def cetakA(self):
      print("minuman yang saya suka= ", self.minuman)

# mendefinisikan kelas induk kedua
class makanan(object):
   def __init__(self, b):
      self.makanan = b
   def cetakB(self):
      print("makanan yang saya suka = ", self.makanan)

# mendefinisikan kelas turunan
class cemilan(minuman, makanan):
   def __init__(self, i, b, n):
      # memanggil minuman.__init__()
      minuman.__init__(self, i)
      # memanggil makanan.__init__()
      makanan.__init__(self, b)
      self.cemilan = n
   def cetakC(self):
      print("cemilan yang saya suka = ", self.cemilan)

def main():
   # membuat objek dari kelas cemilan
   obj = cemilan("susu", "mie", "eskrim")

   # memanggil metode kelas minuman dari obj
   obj.cetakA()

   # memanggil metode kelas makanan dari obj
   obj.cetakB()

   # memanggil metode kelas cemilan
   obj.cetakC()

if __name__ == "__main__":
   main()
