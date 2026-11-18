from models import Studio, Reguler, IMAX, Film, Pelanggan

# Program utama
studio1 = Reguler("Cgv Studio 1", 5)
studio2 = IMAX("Studio IMAX", 5)

film1 = Film("The Married Empress", 120, studio1)
film2 = Film("The Autopsy", 150, studio2)

Anna = Pelanggan("Anna")
Ayra = Pelanggan("Ayra")

Anna.reservasi(film1, "K1")
Ayra.reservasi(film2, "K3")
Anna.reservasi(film1, "K1")     # gagal, sudah dipesan
Anna.reservasi(film1, "K9")     # gagal, kursi tidak ada
Ayra.reservasi(film2, "K4")

print("Kursi kosong Cgv Studio 1:", studio1.kursi_kosong)
print(f"Total bayar Anna: {Studio.format_rupiah(Anna.total_bayar())}")
print("Total studio:", Studio.total_studio())
