# 02. Expense Tracker

Aplikasi pelacak keuangan dan anggaran pribadi (*Expense & Budget Tracker*) berbasis Dart murni. Menyediakan pencatatan transaksi masuk dan keluar, pengelompokan kategori, batas anggaran bulanan, analitik statistik, serta impor/ekspor data CSV dan JSON.

## Fitur Utama
- **Pencatatan Transaksi**: Pemasukan (*Income*) dan Pengeluaran (*Expense*) dengan metadata lengkap.
- **Kategori Fleksibel**: Makanan, Transportasi, Gaji, Belanja, Tagihan, dan kategori kustom.
- **Anggaran Bulanan**: Peringatan jika pengeluaran melebihi batas anggaran yang ditentukan.
- **Laporan & Statistik**: Laporan harian, rekapitulasi bulanan, rasio persentase per kategori, dan transaksi tertinggi.
- **Serialisasi Data**: Impor dan ekspor data dalam format JSON dan CSV.

## Struktur File (24 File Dart)
- `bin/main.dart`: Entry point CLI.
- `lib/expense_tracker.dart`: Export publik modul.
- `lib/src/models/`: Transaction, TransactionType, Category, Budget, ExpenseSummary.
- `lib/src/exceptions/`: ExpenseException, ValidationException.
- `lib/src/repositories/`: TransactionRepository, BudgetRepository.
- `lib/src/services/`: ExpenseService, BudgetService, ReportService, AnalyticsService.
- `lib/src/parsers/`: CsvParser, JsonParser.
- `lib/src/validators/`: TransactionValidator.
- `lib/src/utils/`: CurrencyFormatter, DateHelper.
- `lib/src/config/`: TrackerConfig.
- `lib/src/application/`: TrackerApp.
- `test/unit/`: Pengujian transaksi, kalkulasi anggaran, dan analitik.
- `test/integration/`: Pengujian alur transaksi dan ekspor data.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
