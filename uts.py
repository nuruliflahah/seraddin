class Santri:
    def __init__(self,nama,nisn,jurusan,tingkat,jenis_kelamin):
        self.nama = nama
        self.nisn = nisn
        self.jurusan = jurusan
        self.tingkat = tingkat
        self.jenis_kelamin = jenis_kelamin


    def keterangan(self):
        ket =""
        if jenis_kelamin == "L" or jenis_kelamin == "l":
            ket = "laki_laki"
        elif jenis_kelamin == "P" or jenis_kelamin == "p":
            ket = "perempuan"

        print("santri dengan\n nama : {}\n nisn :{}\n jurusan : {}\n tingkat : {}\n ".format(self.nama,self.nisn,self.jurusan,self.tingkat))
        
#program pendaftaran santri baru
nama = input("masukkan nama :")
    
#jika menggunakan int maka
nisn = int(input("masukkan nisn :")) 

#menentukan jurusan
jurusan = input("masukkan jurusan :")

#menetukan tingkat
tingkat = input("masukkan tingkat :")

# L = laki_laki
# P = perempuan


jenis_kelamin = input("pilih jenis_kelamin[L/P]: ")


santri = Santri(nama, nisn, jurusan, tingkat,jenis_kelamin)
santri.keterangan()



            


        