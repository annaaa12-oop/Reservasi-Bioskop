# Tugas UTS Pemrograman Berorientasi Objek (OOP)

- Nama : Destryana Damayanti Sumarna
- NIM : 14012500116
- Kelas : 3A-KOM
- Mata Kuliah : Pemrogramman Berorientasi Objek

---
# Reservasi Bioskop

Project OOP Python sederhana untuk reservasi tiket bioskop.

## Fitur
- Pemesanan kursi berdasarkan film dan studio
- Validasi kursi yang sudah dipesan atau tidak tersedia
- Harga tiket berbeda untuk tiap tipe studio (Reguler, IMAX)
- Perhitungan total pembayaran pelanggan

## Penerapan Konsep OOP

| Konsep | Lokasi |
|---|---|
| Class & Object | semua file |
| Atribut instance & class attribute | `models.py` (`jumlah_studio`) |
| Instance method | `pesan_kursi()`, `batal_kursi()`, `reservasi()` |
| Class method | `Studio.total_studio()` |
| Static method | `Studio.format_rupiah()` |
| Property | `Studio.kursi_kosong` |
| Encapsulation | atribut `__kursi` |
| Abstract class & method | `Studio`, `harga_tiket()` |
| Inheritance | `Reguler`, `Premier`, `IMAX` |
| Polymorphism | `harga_tiket()` berbeda di tiap class |
| Composition | `Film` memiliki `Studio` |

## Struktur File
- `models.py` : berisi semua class
- `main.py` : program utama

## Cara Menjalankan
python main.py
