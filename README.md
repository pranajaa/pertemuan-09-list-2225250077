# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Hitana Rifa Pranaja

NIM: 2225250077

Kelas: 3A

## Tujuan
Mengolah kumpulan data numerik menggunakan list Python untuk menghitung statistik nilai dan menentukan kelulusan mahasiswa.

## Struktur Program
- `praktik/analisis_nilai_mahasiswa.py`: Program untuk mengolah data nilai mahasiswa, menghitung total, rata-rata, nilai minimum, nilai maksimum, serta jumlah mahasiswa yang lulus dan belum lulus.

## Cara Menjalankan
Jalankan perintah berikut melalui terminal:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

## Test Case

| Data | Yang Diperiksa | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| `[60, 70, 80]` | Rata-rata | 70.00 | 70.00 | Berhasil |
| `[60, 70, 80]` | Minimum / maksimum | 60 / 80 | 60 / 80 | Berhasil |
| `[60, 70, 80]` | Jumlah lulus | 3 | 3 | Berhasil |
| `[59, 60, 61]` | Batas kelulusan | 2 lulus | 2 lulus | Berhasil |
| `[]` | Penanganan list kosong pada fungsi rata-rata | Tidak error | Tidak error | Berhasil |

## Refleksi
Saya memahami bahwa list dapat digunakan untuk menyimpan dan mengolah banyak data dalam satu variabel. Saya juga memahami cara menggunakan fungsi untuk menghitung rata-rata dan menentukan nilai mahasiswa yang lulus. Kesalahan pembagian dengan nol pada list kosong dapat diatasi dengan memeriksa jumlah data terlebih dahulu.
