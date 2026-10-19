# 07. Inventory Management System

Aplikasi sistem pengelolaan inventaris (*Inventory Management System*) tingkat menengah berbasis Dart murni. Menyediakan pengelolaan stok barang komprehensif, generator & validator SKU produk, mutasi transaksi barang masuk/keluar/penyesuaian, deteksi dini stok menipis (*low stock alert*), kalkulasi valuasi aset, jejak audit (*audit trail*) kekal, dan impor/ekspor format CSV.

## Fitur Utama
- **Katalog Produk & SKU**: Pembuatan dan verifikasi SKU unik terstruktur.
- **Mutasi Stok (Transactions)**: Stock In, Stock Out, dan Stock Adjustment dengan alasan mutasi.
- **Peringatan Stok Rendah**: Deteksi otomatis produk yang berada di bawah ambang batas minimum.
- **Valuasi Inventaris**: Perhitungan nilai total aset inventaris berdasarkan harga pokok pembelian.
- **Audit Logging**: Pencatatan riwayat setiap aksi dan perubahan data untuk keperluan kepatuhan (*compliance*).
- **Impor & Ekspor CSV**: Pertukaran data dengan spreadsheet secara langsung.

## Struktur File (23 File Dart)
- `bin/main.dart`: CLI entry point interaktif.
- `lib/inventory_system.dart`: Export publik modul.
- `lib/src/models/`: Product, TransactionType, InventoryTransaction, StockLevel, AuditEntry, InventorySummary.
- `lib/src/exceptions/`: InventoryException, StockException.
- `lib/src/repositories/`: ProductRepository, TransactionRepository, AuditRepository.
- `lib/src/services/`: InventoryService, SkuService, AlertService, ValuationService, CsvService.
- `lib/src/validators/`: ProductValidator.
- `lib/src/utils/`: SkuGenerator.
- `lib/src/config/`: InventoryConfig.
- `lib/src/application/`: InventoryApp.
- `test/unit/`: Pengujian mutasi stok, validasi SKU, dan valuasi aset.
- `test/integration/`: Pengujian alur transaksi inventaris dan ekspor CSV end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
