class Wahana:
    def __init__(self, nama, harga, kategori):       #encapsulation
        self.__nama = nama
        self.__harga = harga
        self.__kategori = kategori

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_kategori(self):
        return self.__kategori

    def hitung_harga(self, jumlah):                 #abstract
        return self.__harga * jumlah

    def __str__(self):
        return f"{self.__nama} - Rp{self.__harga:,}"


# INHERITANCE
class RollerCoaster(Wahana):                          #polymorphism

    # POLYMORPHISM
    def hitung_harga(self, jumlah):
        return self.get_harga() * jumlah


class WaterBoom(Wahana):

    # POLYMORPHISM
    def hitung_harga(self, jumlah):
        return self.get_harga() * jumlah


class Bianglala(Wahana):

    # POLYMORPHISM
    def hitung_harga(self, jumlah):
        return self.get_harga() * jumlah


class Pengunjung:

    def __init__(self, nama, gender):
        self.nama = nama
        self.gender = gender

    def __str__(self):
        return f"{self.nama} ({self.gender})"


class Tiket:

    def __init__(self, pengunjung, wahana, jumlah):
        self.pengunjung = pengunjung
        self.wahana = wahana
        self.jumlah = jumlah

    # INSTANCE METHOD
    def beli_tiket(self):
        return self.wahana.hitung_harga(self.jumlah)

    # INSTANCE METHOD
    def tampilkan_tiket(self):
        total = self.beli_tiket()

        return {
            "nama": self.pengunjung.nama,
            "gender": self.pengunjung.gender,
            "wahana": self.wahana.get_nama(),
            "jumlah": self.jumlah,
            "harga": self.wahana.get_harga(),
            "total": total
        }

    # STATIC METHOD
    @staticmethod
    def validasi_jumlah(jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah tiket harus lebih dari 0")

        if jumlah > 10:
            raise ValueError("Maksimal pembelian adalah 10 tiket")

        return True