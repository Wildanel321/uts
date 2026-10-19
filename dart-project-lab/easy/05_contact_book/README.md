# 05. Contact Book

Aplikasi buku kontak (*Contact Book*) berbasis Dart murni. Menyediakan pengelolaan kontak penuh (CRUD), pencarian cerdas berbasis kemiripan string (*Levenshtein distance*), normalisasi nomor telepon internasional, pengelompokan kontak (*Family, Work, Friends*), dan impor/ekspor data JSON.

## Fitur Utama
- **CRUD Kontak**: Tambah, perbarui, hapus, dan tandai kontak favorit.
- **Pencarian Cerdas**: Pencarian fuzzy berbasis Levenshtein distance dan kecocokan substring nomor telepon yang dinormalisasi.
- **Validasi Data**: Memvalidasi format email dan pola nomor telepon yang valid.
- **Pengelompokan (Group Tagging)**: Mengorganisir kontak ke dalam grup khusus.
- **Impor & Ekspor JSON**: Serialisasi dan deserialisasi data buku kontak untuk pencadangan.

## Struktur File (22 File Dart)
- `bin/main.dart`: CLI entry point interaktif.
- `lib/contact_book.dart`: Export publik modul.
- `lib/src/models/`: Contact, ContactGroup, SearchFilter, ImportExportResult.
- `lib/src/exceptions/`: ContactException, ValidationException.
- `lib/src/repositories/`: ContactRepository.
- `lib/src/services/`: ContactService, SearchService, GroupService, SerializationService.
- `lib/src/validators/`: ContactValidator.
- `lib/src/utils/`: PhoneNormalizer, StringSimilarity.
- `lib/src/config/`: BookConfig.
- `lib/src/application/`: ContactApp.
- `test/unit/`: Pengujian validasi kontak, normalisasi telepon, dan fuzzy similarity.
- `test/integration/`: Pengujian alur CRUD dan impor/ekspor JSON.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
