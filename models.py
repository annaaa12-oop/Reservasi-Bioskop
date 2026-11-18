from abc import ABC, abstractmethod


class Studio(ABC):
    jumlah_studio = 0  # class variable

    def __init__(self, nama, jumlah_kursi):
        self.nama = nama
        self.__kursi = {f"K{i}": False for i in range(1, jumlah_kursi + 1)}  # encapsulation
        Studio.jumlah_studio += 1

    @property
    def kursi_kosong(self):
        return [k for k, terisi in self.__kursi.items() if not terisi]

    def pesan_kursi(self, nomor):
        if nomor not in self.__kursi:
            print(f"Kursi {nomor} tidak ada")
            return False
        if self.__kursi[nomor]:
            print(f"Kursi {nomor} sudah dipesan")
            return False
        self.__kursi[nomor] = True
        return True

    def batal_kursi(self, nomor):
        if nomor in self.__kursi:
            self.__kursi[nomor] = False

    @classmethod
    def total_studio(cls):
        return cls.jumlah_studio

    @staticmethod
    def format_rupiah(angka):
        return f"Rp{angka:,}"

    @abstractmethod  # abstraction
    def harga_tiket(self):
        pass


class Reguler(Studio):  # inheritance
    def harga_tiket(self):  # polymorphism
        return 25000


class Premier(Studio):
    def harga_tiket(self):
        return 70000


class IMAX(Studio):
    def harga_tiket(self):
        return 100000


class Film:
    def __init__(self, judul, durasi, studio):
        self.judul = judul
        self.durasi = durasi
        self.studio = studio


class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.tiket = []

    def reservasi(self, film, nomor_kursi):
        if film.studio.pesan_kursi(nomor_kursi):
            harga = film.studio.harga_tiket()
            self.tiket.append((film.judul, nomor_kursi, harga))
            print(f"{self.nama} memesan kursi {nomor_kursi} untuk '{film.judul}' "
                  f"di {film.studio.nama} ({Studio.format_rupiah(harga)})")

    def total_bayar(self):
        return sum(t[2] for t in self.tiket)
