# Pertemuan-02-dasar-python-2225250203
## Identitas
**Nama** : Siti Rohmah
**NIM** : 2225250203
**Kelas** : 3A
## Tujuan Repositori
repositori ini adalah tempat untuk mengumpulkan tugas pertemuan 02 Algoritma dan pemrograman. 
pada pertemuan 02 ini materi yang di praktikkan antara lain variabel,konstanta, tipe data,serta 
input dan output
## Daftar dan fungsi berkas
### 01_biodata.py
* Menerima input data diri (nama, NIM, kelas, tahun lahir) dan menghitung perkiraan umur berdasarkan tahun saat ini.
### 02_persegi_panjang.py
* Menerima input panjang dan lebar sebagai `float` untuk menghitung luas dan keliling persegi panjang dengan format dua angka desimal.
### 03_konversi_suhu.py
* Mengonversi suhu dari Celsius ke Fahrenheit dan Kelvin menggunakan konstanta `KELVIN_OFFSET = 273.15`.
### 04_nilai_akhir.py
* Menghitung nilai akhir mahasiswa berdasarkan komponen bobot tugas (20%), UTS (30%), dan UAS (50%).
### kalkulator_koordinat.py
* Menghitung perubahan koordinat ($dx$ dan $dy$), jarak Euclidean, serta titik tengah (*midpoint*) dari dua titik koordinat pada bidang kartesius.
## Cara menjalankan program dari terminal
### 1. python 01_biodata.py
Masukkan Nama Anda: Siti Rohmah
Masukkan NIM Anda: 2225250203
Masukkan Kelas Anda: 3A
Masukkan Tahun Lahir: 2007

--- OUTPUT BIODATA ---
Nama   : Siti Rohmah
NIM    : 2225250203
Kelas  : 3A
Umur   : 19 Tahun
### 2. python 02_persegi_panjang.py
Masukkan panjang: 8
Masukkan lebar: 5

Luas Persegi Panjang     : 40.00
Keliling Persegi Panjang : 26.00
### 3. python 03_konversi_suhu.py
Masukkan suhu dalam Celsius: 0°
Suhu dalam Fahrenheit: 32.00 °F
Suhu dalam Kelvin    : 273.15 K
### 4. python 04_nilai_akhir.py
Masukkan nilai Tugas: 80
Masukkan nilai UTS: 80
Masukkan nilai UAS: 80
Nilai Akhir: 80.00
### 5. Kalkulator_Koordinat.py 
Menggunakan Test Case 1
python kalkulator_koordinat.py
x titik A: 0
y titik A: 0
x titik B: 3
y titik B: 4
Perubahan : dx = 3.00, dy = 4.00
Jarak A ke B : 5.00
Titik tengah : (1.50, 2.00)
## Tabel Hasil Uji Coba (Test Cases) Kalkulator Koordinat

| No | Titik A $(x_1, y_1)$ | Titik B $(x_2, y_2)$ | Perubahan ($dx, dy$) | Jarak Euclidean | Titik Tengah ($(x_1+x_2)/2, (y_1+y_2)/2$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | (0, 0) | (3, 4) | $dx = 3.00, dy = 4.00$ | $5.00$ | (1.50, 2.00) |
| 2 | (2, 1) | (4, 1) | $dx = 2.00, dy = 0.00$ | $2.00$ | (3.00, 1.00) |
| 3 | (2.5, -1) | (2.5, 3) | $dx = 0.00, dy = 4.00$ | $4.00$ | (2.50, 1.00) |
## 5. Refleksi Singkat
Praktikum Pertemuan 2 ini memberikan pemahaman mengenai pentingnya tipe data (`float`, `int`), penanganan input pengguna secara interaktif, serta pemanfaatan operator aritmatika dan *f-string* untuk menghasilkan format keluaran yang presisi. Kendala teknis seperti pengelolaan *version control* menggunakan Git dan sinkronisasi dengan GitHub juga berhasil diatasi, sehingga melatih kedisiplinan dalam mendokumentasikan kode program secara profesional.
## 6. Sumber / Referensi
*Modul Praktikum Algoritma dan Pemrograman: Dasar Pemrograman Python & Git/GitHub*.
*Dokumentasi Resmi Python Software Foundation. (https://docs.python.org/)
*Panduan Penggunaan Git dan GitHub Dokumentasi Resmi. (https://git-scm.com/doc)
