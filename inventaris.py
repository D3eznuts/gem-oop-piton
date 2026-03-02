from abc import ABC, abstractmethod

#Kelas Abstrak

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar

    # Getter untuk melihat stok
    def get_stok(self):
        return self.__stok

    # Getter untuk harga dasar (dipakai child class)
    def get_harga_dasar(self):
        return self.__harga_dasar

    # Method untuk menambah stok (dengan validasi)
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")

    # Abstract Method
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

#Inheritance & Polymorphism

class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor
        self.pajak = 0.10

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")

    def hitung_harga_total(self, jumlah):
        harga_dasar = self.get_harga_dasar()
        pajak_nominal = harga_dasar * self.pajak
        subtotal = (harga_dasar + pajak_nominal) * jumlah

        print(f"   Harga Dasar: Rp {harga_dasar:,} | Pajak(10%): Rp {int(pajak_nominal):,}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")

        return subtotal


class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera
        self.pajak = 0.05

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")

    def hitung_harga_total(self, jumlah):
        harga_dasar = self.get_harga_dasar()
        pajak_nominal = harga_dasar * self.pajak
        subtotal = (harga_dasar + pajak_nominal) * jumlah

        print(f"   Harga Dasar: Rp {harga_dasar:,} | Pajak(5%): Rp {int(pajak_nominal):,}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")

        return subtotal


#Fungsi polymorphism untuk proses transaksi

def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0

    for i, (barang, jumlah) in enumerate(daftar_barang, start=1):
        print(f"{i}. ", end="")
        barang.tampilkan_detail()
        total += barang.hitung_harga_total(jumlah)

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")


# Uji Coba 
print("--- SETUP DATA ---")

# Admin membuat produk
laptop1 = Laptop("ACER Nitro Y15", 25000000, "ITEL Core i7")
hp1 = Smartphone("Nokia", 1000000, "1000MP")

# Admin isi stok
laptop1.tambah_stok(67)
hp1.tambah_stok(-5)   # Harus gagal
hp1.tambah_stok(37)   # Berhasil

# User membeli barang
keranjang = [
    (laptop1, 2),
    (hp1, 1)
]
proses_transaksi(keranjang)