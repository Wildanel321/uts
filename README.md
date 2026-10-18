# Kumpulan Program Latihan & Studi Kasus Dart (UTS)

> ⚠️ **Catatan Penting:** *SELALU PAKAI `dart analyze` sebelum commit atau pengujian kode untuk memastikan tidak ada error maupun warning.*

Repositori ini berisi kumpulan program berbasis bahasa pemrograman Dart untuk menyelesaikan berbagai studi kasus logika percabangan, perhitungan tarif, validasi, dan alur kontrol dengan tingkat kesulitan: **Easy**, **Medium**, dan **Advance**.

---

## 📁 Struktur Direktori

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

## 🟢 1. Sub-Folder: Easy (Tingkat Dasar)

Folder ini berisi latihan logika dasar, perbandingan nilai sederhana, dan pengkondisian (`if-else`) satu atau dua cabang.

### 📄 `Easy/batas kecepatan .dart` (Soal 3)
* **Deskripsi:** Memeriksa apakah kecepatan kendaraan masih dalam batas wajar atau melebihi batas aman.
* **Input:** Kecepatan kendaraan (`km/jam`).
* **Aturan Logika:**
  * Kecepatan maksimal: `80 km/jam`.
  * Jika `kecepatan > 80`: Menampilkan status *"Melebihi Batas Kecepatan"* serta peringatan keselamatan.
  * Jika `kecepatan <= 80`: Menampilkan status *Kecepatan Aman*.

### 📄 `Easy/diskon toko.dart` (Soal 1)
* **Deskripsi:** Menghitung potongan harga (diskon) belanja pada kasir toko.
* **Input:** Total nilai belanja (`Rp`).
* **Aturan Logika:**
  * Jika total belanja minimal `Rp 500.000`: Mendapatkan diskon `10%`.
  * Selain itu: Diskon `0%`.
  * Program menghitung nominal diskon dan total akhir yang wajib dibayarkan.

### 📄 `Easy/easy.dart`
* **Deskripsi:** Program dasar penentuan nilai terbesar dari dua buah bilangan integer secara langsung.
* **Input:** Dua buah bilangan integer (`a` dan `b`).
* **Aturan Logika:** Menggunakan perbandingan `a > b` untuk mencetak bilangan mana yang paling besar.

### 📄 `Easy/iseng.dart`
* **Deskripsi:** Program penentu bilangan terbesar dari dua bilangan dengan penanganan validasi input (angka desimal/bulat, sanitasi string kosong, dan pencegahan error input).
* **Input:** Dua buah bilangan (bisa bertipe desimal / integer).
* **Aturan Logika:**
  * Membandingkan kedua angka (`bil1 > bil2`, `bil2 > bil1`, atau sama besar).
  * Dilengkapi fungsi `formatAngka` untuk membuang desimal `.0` jika bernilai bulat.

### 📄 `Easy/penarikan saldo.dart` (Soal 4)
* **Deskripsi:** Simulasi transaksi penarikan saldo rekening tabungan / ATM.
* **Input:** Saldo awal rekening (`Rp`) dan nominal uang yang ingin ditarik (`Rp`).
* **Aturan Logika:**
  * Jika `penarikan <= saldo`: Status *"Transaksi Berhasil"* dan menampilkan sisa saldo.
  * Jika `penarikan > saldo`: Status *"Saldo Tidak Cukup"* dan menghitung kekurangan dana.

### 📄 `Easy/persentase hp.dart` (Soal 5)
* **Deskripsi:** Pengecekan kondisi level daya baterai smartphone.
* **Input:** Persentase baterai (`0 - 100%`).
* **Aturan Logika:**
  * Jika `baterai < 20%`: Menampilkan peringatan *"Segera Isi Daya"* karena daya lemah.
  * Jika `baterai >= 20%`: Menampilkan status baterai aman/cukup.

---

## 🟡 2. Sub-Folder: Medium (Tingkat Menengah)

Folder ini berisi kasus logika yang melibatkan multi-kondisi (kombinasi operator logika `&&`, `||`), perhitungan bertingkat, serta validasi sanitasi input yang lebih kompleks.

### 📄 `Medium/auth login.dart` (Soal 5)
* **Deskripsi:** Simulasi sistem otentikasi login pengguna berbasis konsol.
* **Input:** `Username` dan `Password`.
* **Aturan Logika:**
  * Kredensial valid: `Username == 'admin'` dan `Password == '12345'`.
  * Jika kedua kondisi terpenuhi: Status *"Login Berhasil"*.
  * Selain itu: Status *"Login Gagal"* (kredensial salah).

### 📄 `Medium/iseng.dart`
* **Deskripsi:** Seleksi kelayakan beasiswa mahasiswa dengan validasi ketat terhadap input IPK dan format nominal gaji orang tua (membersihkan pemisah ribuan titik/koma/simbol Rp).
* **Input:** Nilai IPK (`0.00 - 4.00`) dan Penghasilan orang tua per bulan (`Rp`).
* **Aturan Logika:**
  * Syarat lolos: `IPK >= 3.50` DAN `Penghasilan <= Rp 4.000.000`.
  * Menampilkan catatan spesifik jika salah satu atau kedua syarat tidak terpenuhi.

### 📄 `Medium/medium.dart`
* **Deskripsi:** Versi implementasi ringkas untuk penentuan beasiswa mahasiswa Poliwangi.
* **Input:** IPK dan penghasilan orang tua per bulan.
* **Aturan Logika:** Pengecekan kondisi `ipk >= 3.50 && penghasilan <= 4000000` dengan luaran *"Berhak Menerima Beasiswa"* atau *"Tidak Berhak"*.

### 📄 `Medium/parkir mobil.dart` (Soal 4)
* **Deskripsi:** Menghitung total biaya parkir mobil berdasarkan durasi parkir (dibulatkan ke atas / `ceil`).
* **Input:** Durasi parkir dalam satuan jam.
* **Aturan Logika:**
  * 2 jam pertama: Dikenakan tarif `Rp 5.000`.
  * Setiap jam berikutnya: Tambahan `Rp 2.000 / jam`.
  * Tarif maksimal (durasi > 8 jam): Flat maksimal `Rp 20.000`.

### 📄 `Medium/penghitung massa.dart` (Soal 3)
* **Deskripsi:** Menghitung Indeks Massa Tubuh (*Body Mass Index* / BMI) serta mengelompokkan ke dalam kategori berat badan.
* **Input:** Berat badan (`kg`) dan tinggi badan (`meter` atau otomatis dikonversi jika diinput dalam `cm`).
* **Rumus & Kategori:**
  * $\text{BMI} = \frac{\text{berat}}{\text{tinggi}^2}$
  * $\text{BMI} < 18.5$: Kurus
  * $18.5 \le \text{BMI} \le 24.9$: Normal
  * $25.0 \le \text{BMI} \le 29.9$: Kelebihan Berat Badan
  * $\text{BMI} \ge 30.0$: Obesitas

### 📄 `Medium/tarif wisata.dart` (Soal 1)
* **Deskripsi:** Menentukan harga tiket masuk tempat wisata sesuai dengan kategori umur pengunjung.
* **Input:** Usia pengunjung (tahun).
* **Aturan Logika:**
  * Usia `< 5 tahun`: Kategori Balita $\rightarrow$ **Gratis (Rp 0)**
  * Usia `5 - 12 tahun`: Kategori Anak-anak $\rightarrow$ **Rp 15.000**
  * Usia `13 - 59 tahun`: Kategori Dewasa $\rightarrow$ **Rp 30.000**
  * Usia $\ge 60 \text{ tahun}$: Kategori Lansia $\rightarrow$ **Rp 20.000**

---

## 🔴 3. Sub-Folder: Advance (Tingkat Lanjutan)

Folder ini mencakup studi kasus kompleks dengan perhitungan tarif progresif bertingkat (*multi-tier*), validasi geometri segitiga, evaluasi nilai berbobot persentase, dan penggabungan kriteria seleksi berlapis.

### 📄 `Advance/Advance.dart`
* **Deskripsi:** Program penghitung tagihan tarif listrik progresif per *tier* pemakaian.
* **Input:** Total pemakaian listrik (`kWh`).
* **Aturan Tarif Bertingkat (Tier):**
  * **Tier 1 (0 - 100 kWh):** Rp 1.500 / kWh
  * **Tier 2 (101 - 300 kWh):** Rp 2.000 / kWh (dihitung untuk pemakaian di atas 100 s.d. 300)
  * **Tier 3 (> 300 kWh):** Rp 2.500 / kWh (dihitung untuk kelebihan pemakaian di atas 300)
* 💡 **Catatan Teknis Arsitektur (Kenapa `dart:io` dan bukan `dart:math`?):**
  * Program mengimpor **`dart:io`** karena membutuhkan fungsionalitas konsol berupa `stdout.write()` untuk mencetak prompt dan `stdin.readLineSync()` untuk membaca input dari keyboard secara interaktif.
  * Program **tidak** mengimpor **`dart:math`** karena perhitungan pada tarif listrik hanyalah operasi aritmatika dasar (perkalian `*`, pengurangan `-`, penjumlahan `+`) yang sudah disediakan oleh inti bahasa Dart (`dart:core`). Library `dart:math` hanya dibutuhkan untuk fungsi tingkat lanjut seperti akar (`sqrt`), eksponen (`pow`), trigonometri, atau bilangan acak (`Random`).

### 📄 `Advance/jenis segitiga.dart` (Soal 4)
* **Deskripsi:** Menentukan validitas pembentukan segitiga dan mengklasifikasikan jenisnya berdasarkan panjang ketiga sisinya ($a, b, c$).
* **Input:** Panjang sisi $a$, sisi $b$, dan sisi $c$.
* **Aturan Logika:**
  * **Pertidaksamaan Segitiga:** Ketiga sisi harus $> 0$, serta memenuhi $a + b > c$, $a + c > b$, dan $b + c > a$. Jika tidak memenuhi, maka *"Bukan Segitiga"*.
  * Jika valid:
    * Ketiga sisi sama ($a = b = c$): *"Sama Sisi"*
    * Dua sisi sama ($a = b$ atau $a = c$ atau $b = c$): *"Sama Kaki"*
    * Ketiga sisi berbeda: *"Sembarang"*

### 📄 `Advance/penentu kelulusan.dart` (Soal 3)
* **Deskripsi:** Evaluasi kelulusan mata kuliah mahasiswa berdasarkan gabungan nilai tugas, UTS, UAS, dan persentase kehadiran.
* **Input:** Nilai Tugas (0-100), Nilai UTS (0-100), Nilai UAS (0-100), dan Kehadiran (0-100%).
* **Aturan Bobot & Syarat Lulus:**
  * Bobot: $\text{Nilai Akhir} = (30\% \times \text{Tugas}) + (30\% \times \text{UTS}) + (40\% \times \text{UAS})$.
  * **Syarat Lulus:** Nilai Akhir $\ge 60$ DAN Kehadiran $\ge 75\%$.
  * **Pengecualian:** Jika nilai **UAS < 40**, mahasiswa dinyatakan otomatis *"Tidak Lulus"* tanpa memandang total nilai akhir.

### 📄 `Advance/seleksi penerimaan karyawan.dart` (Soal 1)
* **Deskripsi:** Program evaluasi kelayakan berkas dan tes calon karyawan perusahaan.
* **Input:** Usia, Pendidikan terakhir (D3/S1/S2/S3/dll), dan Nilai tes (0-100).
* **Aturan Logika:**
  1. *"Lolos Seleksi"*: Usia 21-35 tahun, Pendidikan minimal S1 (S1/S2/S3), dan Nilai Tes $\ge 70$.
  2. *"Dipertimbangkan"*: Usia 21-35 tahun, Pendidikan D3, dan Nilai Tes istimewa $\ge 85$.
  3. *"Tidak Lolos"*: Di luar kriteria di atas (dilengkapi alasan detail mengapa tidak lolos).

### 📄 `Advance/tarif hotel.dart` (Soal 5)
* **Deskripsi:** Program penghitungan biaya reservasi kamar hotel dengan diskon member/non-member berjenjang dan potongan transaksi nominal besar.
* **Input:** Harga kamar per malam (`Rp`), Lama menginap (malam), dan Status Member (`Y/N`).
* **Aturan Perhitungan:**
  * **Member:**
    * 1 - 2 malam: Diskon 10%
    * 3 - 5 malam: Diskon 15%
    * \> 5 malam: Diskon 25%
  * **Non-Member:**
    * \> 5 malam: Diskon 10%
    * $\le$ 5 malam: Diskon 0%
  * **Potongan Tambahan:** Potongan ekstra senilai `Rp 200.000` jika total harga setelah diskon melebihi `Rp 3.000.000`.

---

## 🚀 Cara Menjalankan Program

Pastikan Dart SDK sudah terinstal di sistem Anda.

1. **Jalankan Pengecekan Analisis Kode:**
   ```bash
   dart analyze
   ```
2. **Jalankan File Dart yang Diinginkan:**
   ```bash
   # Contoh menjalankan file di folder Easy
   dart run "Easy/diskon toko.dart"

   # Contoh menjalankan file di folder Medium
   dart run "Medium/tarif wisata.dart"

   # Contoh menjalankan file di folder Advance
   dart run "Advance/Advance.dart"
   ```
