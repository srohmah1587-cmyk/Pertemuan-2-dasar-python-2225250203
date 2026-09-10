# Judul Utama (Pertemuan-02-dasar-python-2225250203)
## Identitas
**Nama** : Siti Rohmah
**NIM** : 2225250203
**Kelas** : 3A
## Tujuan Repositori
repositori ini adalah tempat untuk mengumpulkan tugas pertemuan 02 Algoritma dan pemrograman 
pada pertemuan 02 ini materi yang di praktikkan antara lain variabel,konstanta, tipe data,serta 
input dan output
## Daftar dan Fungsi Berkas
**`01_biodata.py`** - Program untuk menampilkan biodata terformat dan menghitung perkiraan umur.
**`02_persegi_panjang.py`** - Program untuk menghitung luas dan keliling persegi panjang.
**`03_konversi_suhu.py`** - Program konversi suhu dari Celsius ke Fahrenheit dan Kelvin.
**`04_nilai_akhir.py`** - Program menghitung nilai akhir berdasarkan bobot tugas, UTS, dan UAS.
**`kalkulator_koordinat.py`** - Program untuk menghitung koordinat, perubahan $dx$ dan $dy$, jarak Euclidean, serta titik tengah dari dua titik koordinat.
## Daftar dan fungsi berkas
**`01_biodata.py`**
   * **Fungsi:** Menerima input data diri (nama, NIM, kelas, tahun lahir) dan menghitung perkiraan umur berdasarkan tahun saat ini.
**`02_persegi_panjang.py`**
   * **Fungsi:** Menerima input panjang dan lebar sebagai `float` untuk menghitung luas dan keliling persegi panjang dengan format dua angka desimal.
**`03_konversi_suhu.py`**
   * **Fungsi:** Mengonversi suhu dari Celsius ke Fahrenheit dan Kelvin menggunakan konstanta `KELVIN_OFFSET = 273.15`.
**`04_nilai_akhir.py`**
   * **Fungsi:** Menghitung nilai akhir mahasiswa berdasarkan komponen bobot tugas (20%), UTS (30%), dan UAS (50%).
**`kalkulator_koordinat.py`**
   * **Fungsi:** Menghitung perubahan koordinat ($dx$ dan $dy$), jarak Euclidean, serta titik tengah (*midpoint*) dari dua titik koordinat pada bidang kartesius.
## Cara menjalankan program dari terminal
### 1. Kalkulator Koordinat (`kalkulator_koordinat.py`) — Menggunakan Test Case 1
```text
$ python kalkulator_koordinat.py
x titik A: 0
y titik A: 0
x titik B: 3
y titik B: 4
Perubahan : dx = 3.00, dy = 4.00
Jarak A ke B : 5.00
Titik tengah : (1.50, 2.00)

## Test Case Wajib Kalkulator Koordinat
| Kasus | Titik A $(x_1, y_1)$ | Titik B $(x_2, y_2)$ | Jarak | Titik Tengah |
| :---: | :---: | :---: | :---: | :---: |
| 1 | (0, 0) | (3, 4) | 5.00 | (1.50, 2.00) |
| 2 | (2, 1) | (4, 1) | 2.00 | (3.00, 1.00) |
| 3 | (2.5, -1) | (2.5, 3) | 4.00 | (2.50, 1.00) |
