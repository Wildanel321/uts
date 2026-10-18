# Kumpulan Program Latihan Dart (UTS)

> *SELALU PAKAI `dart analyze`*

Repositori ini berisi latihan program bahasa pemrograman Dart untuk berbagai studi kasus alur kontrol dan percabangan (`if-else`), dibagi menjadi tiga tingkatan: **Easy**, **Medium**, dan **Advance**.

---

## 📁 Struktur Folder

```text
uts/
├── Easy/
│   ├── batas kecepatan .dart
│   ├── diskon toko.dart
│   ├── easy.dart
│   ├── iseng.dart
│   ├── penarikan saldo.dart
│   └── persentase hp.dart
├── Medium/
│   ├── auth login.dart
│   ├── iseng.dart
│   ├── medium.dart
│   ├── parkir mobil.dart
│   ├── penghitung massa.dart
│   └── tarif wisata.dart
├── Advance/
│   ├── Advance.dart
│   ├── jenis segitiga.dart
│   ├── penentu kelulusan.dart
│   ├── seleksi penerimaan karyawan.dart
│   └── tarif hotel.dart
└── README.md
```

---

## 🟢 1. Folder Easy (Tingkat Dasar)

Program pada folder ini berfokus pada logika dasar perbandingan dan pengkondisian sederhana:

* **`batas kecepatan .dart`**: Mengecek kecepatan kendaraan. Jika `kecepatan > 80`, tampilkan *"Melebihi Batas Kecepatan"*, selain itu *"Kecepatan Aman"*.
* **`diskon toko.dart`**: Menghitung diskon 10% jika total belanja $\ge$ Rp 500.000.
* **`easy.dart`**: Membandingkan dua bilangan bulat untuk menentukan bilangan mana yang lebih besar.
* **`iseng.dart`**: Membandingkan dua bilangan bulat dengan penanganan kondisi jika kedua bilangan bernilai sama.
* **`penarikan saldo.dart`**: Memeriksa penarikan saldo rekening. Jika nominal tarik $\le$ saldo, transaksi berhasil; jika melebihi, saldo tidak cukup.
* **`persentase hp.dart`**: Mengecek persentase baterai HP. Jika `< 20%`, tampilkan peringatan *"Segera Isi Daya"*.

---

## 🟡 2. Folder Medium (Tingkat Menengah)

Program pada folder ini menggunakan kombinasi operator logika (`&&`, `||`) dan perhitungan berjenjang:

* **`auth login.dart`**: Autentikasi login sederhana dengan mencocokkan `username == 'admin'` dan `password == '12345'`.
* **`iseng.dart`**: Seleksi kelayakan beasiswa mahasiswa dengan syarat `IPK >= 3.50` dan `penghasilan orang tua <= Rp 4.000.000`.
* **`medium.dart`**: Versi ringkas seleksi beasiswa dengan syarat IPK dan batas penghasilan orang tua.
* **`parkir mobil.dart`**: Menghitung biaya parkir mobil (2 jam pertama Rp 5.000, jam berikutnya Rp 2.000/jam, maksimal Rp 20.000 jika lebih dari 8 jam).
* **`penghitung massa.dart`**: Menghitung Indeks Massa Tubuh (BMI) dengan rumus $\text{berat} / (\text{tinggi}^2)$ dan menentukan kategori (Kurus, Normal, Kelebihan Berat Badan, Obesitas).
* **`tarif wisata.dart`**: Menentukan tarif tiket masuk berdasarkan kategori usia (< 5 tahun: gratis, 5-12 tahun: Rp 15.000, 13-59 tahun: Rp 30.000, $\ge 60$ tahun: Rp 20.000).

---

## 🔴 3. Folder Advance (Tingkat Lanjutan)

Program pada folder ini mencakup studi kasus bertingkat dan perhitungan kompleks:

* **`Advance.dart`**: Menghitung tarif listrik progresif per tier (Tier 1: 0-100 kWh @ Rp 1.500, Tier 2: 101-300 kWh @ Rp 2.000, Tier 3: > 300 kWh @ Rp 2.500).
  > **Catatan Penggunaan Library:** Menggunakan `dart:io` untuk input-output konsol (`stdin` dan `stdout`). Tidak menggunakan `dart:math` karena perhitungan hanya membutuhkan operasi aritmatika dasar (`+`, `-`, `*`) yang sudah tersedia bawaan di Dart core.
* **`jenis segitiga.dart`**: Memeriksa syarat segitiga ($a+b>c, a+c>b, b+c>a$), lalu mengelompokkan jenisnya (Sama Sisi, Sama Kaki, atau Sembarang).
* **`penentu kelulusan.dart`**: Menghitung nilai akhir dengan bobot (30% Tugas + 30% UTS + 40% UAS). Syarat lulus: nilai akhir $\ge 60$ dan kehadiran $\ge 75\%$, serta otomatis tidak lulus jika nilai UAS $< 40$.
* **`seleksi penerimaan karyawan.dart`**: Menyeleksi calon karyawan berdasarkan kriteria usia (21-35 tahun), pendidikan (D3/S1), dan nilai tes.
* **`tarif hotel.dart`**: Menghitung tarif kamar hotel berdasarkan lama inap, diskon berjenjang member/non-member, dan potongan ekstra Rp 200.000 jika total setelah diskon $> \text{Rp } 3.000.000$.

---

## 🚀 Cara Menjalankan

1. **Analisis Kode:**
   ```bash
   dart analyze
   ```
2. **Jalankan File Program:**
   ```bash
   dart run "Easy/batas kecepatan .dart"
   dart run "Medium/tarif wisata.dart"
   dart run "Advance/Advance.dart"
   ```
