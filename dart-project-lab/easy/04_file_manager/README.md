# 04. File Manager CLI

Aplikasi pengelola berkas baris perintah (*File Manager CLI*) berbasis Dart murni. Menyediakan navigasi direktori (*tree view*), pencarian file rekursif, pengelompokan berdasarkan ekstensi/tipe, penghitungan *checksum* SHA-256 integritas file, dan operasi berkas aman (*safe copy/move/delete* dengan konfirmasi pelindung).

## Fitur Utama
- **Eksplorasi Direktori**: Tampilan pohon (*tree*) dan daftar detail (ukuran, tanggal modifikasi).
- **Pencarian Rekursif**: Pencarian berdasarkan substring nama, ekstensi, dan rentang ukuran.
- **Pengelompokan Ekstensi**: Statistik jumlah file dan total ukuran per kategori (Kode, Dokumen, Gambar, Audio, Arsip).
- **Integritas Checksum**: Komputasi hash kriptografis SHA-256 untuk mendeteksi integritas file.
- **Operasi Berkas Aman**: Proteksi penimpaan file (*overwrite guard*) dan validasi pencegahan *directory traversal*.

## Struktur File (21 File Dart)
- `bin/main.dart`: CLI interactive runner.
- `lib/file_manager.dart`: Export publik pustaka.
- `lib/src/models/`: FileEntry, FileTypeGroup, SearchCriteria, HashResult.
- `lib/src/exceptions/`: FileManagerException, PermissionException.
- `lib/src/services/`: DirectoryService, FileSearchService, FileOperationService, HashService, MetadataService.
- `lib/src/validators/`: PathValidator, OperationValidator.
- `lib/src/utils/`: SizeFormatter, PathHelper.
- `lib/src/config/`: ManagerConfig.
- `lib/src/application/`: FileManagerApp.
- `test/unit/`: Pengujian pencarian, pengelompokan ekstensi, dan formatting ukuran.
- `test/integration/`: Pengujian alur pembuatan direktori, penyalinan, hashing, dan penghapusan.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
