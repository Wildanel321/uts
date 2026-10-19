# Dart Project Lab (16 Projects • 320+ Pure Dart Files)

Selamat datang di **Dart Project Lab** — kumpulan 16 aplikasi *Pure Dart* (tanpa dependensi Flutter) yang dibangun secara modular, teruji, dan siap dijalankan dengan Dart SDK murni.

Repositori ini dirancang dengan standar arsitektur perangkat lunak yang ketat: setiap proyek memiliki minimal **20 file Dart** mandiri dengan fungsionalitas nyata, pemisahan tanggung jawab (Separation of Concerns), penanganan error komprehensif, null safety penuh, serta rangkaian pengujian unit dan integrasi.

---

## 🗂️ Katalog 16 Proyek

| Tingkat | No | Folder Proyek | Deskripsi Singkat | Fitur Utama | File Dart |
|:---|:---:|:---|:---|:---|:---:|
| **Easy** | 01 | [`easy/01_calculator`](easy/01_calculator) | Calculator CLI & Evaluator | Operasi aritmetika, fungsi ilmiah, tokenisasi Shunting-yard RPN, riwayat & undo | 21+ |
| **Easy** | 02 | [`easy/02_expense_tracker`](easy/02_expense_tracker) | Expense & Budget Tracker | Pencatatan pemasukan/pengeluaran, kategori, batas anggaran, analitik & ekspor CSV/JSON | 21+ |
| **Easy** | 03 | [`easy/03_password_toolkit`](easy/03_password_toolkit) | Password & Vault Toolkit | Generator acak, Diceware passphrase, Shannon entropy, deteksi pola lemah, vault terenkripsi | 21+ |
| **Easy** | 04 | [`easy/04_file_manager`](easy/04_file_manager) | File Manager CLI | Eksplorasi direktori, pencarian rekursif, pengelompokan ekstensi, checksum SHA-256 | 21+ |
| **Easy** | 05 | [`easy/05_contact_book`](easy/05_contact_book) | Contact Book | CRUD kontak, pencarian fuzzy Levenshtein, grup, normalisasi nomor telepon, serialisasi JSON | 21+ |
| **Easy** | 06 | [`easy/06_quiz_engine`](easy/06_quiz_engine) | Interactive Quiz Engine | Bank soal, ragam jenis kuis, timer per soal, shuffle Fisher-Yates, leaderboard | 21+ |
| **Medium** | 07 | [`medium/07_inventory_system`](medium/07_inventory_system) | Inventory Management | Pengelolaan stok, SKU generator, transaksi masuk/keluar, audit log kekal, CSV import/export | 21+ |
| **Medium** | 08 | [`medium/08_task_scheduler`](medium/08_task_scheduler) | Task Scheduler & Worker | Antrean tugas prioritas, interval berulang, parser ekspresi cron, worker pool, retry backoff | 21+ |
| **Medium** | 09 | [`medium/09_log_analyzer`](medium/09_log_analyzer) | Stream Log Analyzer | Parser CLF/Custom, streaming hemat memori, klasterisasi error, deteksi serangan brute-force | 21+ |
| **Medium** | 10 | [`medium/10_rest_api_client`](medium/10_rest_api_client) | Robust REST API Client | HTTP adapter (Real & Mock), exponential backoff & jitter, cache memory ber-TTL, JSON encoder | 21+ |
| **Medium** | 11 | [`medium/11_chat_server`](medium/11_chat_server) | TCP Multi-Client Chat | Server soket TCP, protokol framing berbasis paket, broadcast & private whisper, heartbeat keepalive | 21+ |
| **Medium** | 12 | [`medium/12_web_scraper`](medium/12_web_scraper) | Polite Web Scraper & Crawler | Parser robots.txt, rate limiter per domain, crawler antrean BFS, ekstraksi elemen HTML | 21+ |
| **Advance** | 13 | [`advance/13_mini_database`](advance/13_mini_database) | Mini SQL Database Engine | Parser SQL subset, B-Tree index memory, Write-Ahead Logging (WAL), transaksi ACID rollback | 21+ |
| **Advance** | 14 | [`advance/14_http_framework`](advance/14_http_framework) | Modular HTTP Framework | Radix Tree / Trie router (:param & *), pipeline middleware (Logger, CORS, Auth), JSON helpers | 21+ |
| **Advance** | 15 | [`advance/15_static_code_analyzer`](advance/15_static_code_analyzer) | Static Dart Code Linter | Lexer kode Dart, deteksi konvensi penamaan, unused imports, empty blocks, code duplication detector | 21+ |
| **Advance** | 16 | [`advance/16_job_queue_engine`](advance/16_job_queue_engine) | Background Job Queue | Prioritas antrean multi-level, worker pool berkonkurensi terbatas, Dead-Letter Queue (DLQ), graceful drain | 21+ |

---

## 💻 Panduan Instalasi Dart SDK

### Windows:
Menggunakan Chocolatey atau Winget:
```powershell
# Menggunakan winget
winget install Dart.Dart-SDK

# Atau menggunakan Chocolatey
choco install dart-sdk
```

### Linux (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install apt-transport-https
wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/dart.gpg
echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | sudo tee /etc/apt/sources.list.d/dart_stable.list
sudo apt-get update
sudo apt-get install dart
```

Verifikasi versi Dart:
```bash
dart --version
# Output minimal: Dart SDK version: 3.0.0+
```

---

## 🚀 Cara Menjalankan Proyek

Setiap proyek bersifat mandiri. Pindah ke direktori proyek yang diinginkan, unduh dependensi, lalu jalankan entry point:

```bash
# Contoh 1: Menjalankan Calculator CLI
cd easy/01_calculator
dart pub get
dart run bin/main.dart

# Contoh 2: Menjalankan Task Scheduler
cd ../../medium/08_task_scheduler
dart pub get
dart run bin/main.dart

# Contoh 3: Menjalankan Mini Database Engine
cd ../../advance/13_mini_database
dart pub get
dart run bin/main.dart
```

---

## 🧪 Menjalankan Pengujian Otomatis

Seluruh proyek dilengkapi dengan skrip verifikasi otomatis yang memvalidasi ketersediaan SDK, memeriksa jumlah file (>=20 file per proyek), menjalankan `dart pub get`, `dart format`, `dart analyze`, dan `dart test`.

### Menggunakan Dart Script (Lintas Platform):
```bash
dart run tool/verify_all.dart
```

### Menggunakan PowerShell (Windows):
```powershell
.\scriptserify_all.ps1
```

### Menggunakan Bash (Linux / macOS):
```bash
bash scripts/verify_all.sh
```
