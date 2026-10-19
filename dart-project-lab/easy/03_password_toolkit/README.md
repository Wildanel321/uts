# 03. Password Toolkit

Aplikasi keamanan kata sandi serbaguna (*Password Toolkit*) berbasis Dart murni. Menyediakan generator kata sandi acak berbasis kebijakan, pembuat *passphrase* ala Diceware, kalkulator entropi Shannon, pendeteksi pola sandi lemah (urutan keyboard, angka berulang, kamus kata umum), dan brankas kredensial lokal terenkripsi (*Encrypted Vault*).

## Fitur Utama
- **Password Generator**: Pengaturan panjang, huruf besar/kecil, angka, simbol, dan pengecualian karakter ambigu.
- **Passphrase Generator**: Pembuat kata sandi berbasis frasa kata dengan pemisah dan kapitalisasi acak.
- **Strength Checker & Entropy**: Menghitung skor kekuatan (0-100) dan entropi informasi Shannon (bit).
- **Pattern Detector**: Deteksi pola lemah (qwerty, 123456, perulangan huruf aaa, kata umum 'password').
- **Encrypted Local Vault**: Penyimpanan kredensial lokal dengan enkripsi stream XOR/HMAC SHA-256 menggunakan Master Key.

## Struktur File (22 File Dart)
- `bin/main.dart`: CLI interactive & batch toolkit runner.
- `lib/password_toolkit.dart`: Export publik pustaka.
- `lib/src/models/`: PasswordPolicy, StrengthResult, PassphraseConfig, VaultEntry.
- `lib/src/exceptions/`: ToolkitException, VaultException.
- `lib/src/services/`: PasswordGenerator, PassphraseGenerator, EntropyCalculator, StrengthChecker, PatternDetector, CryptoService.
- `lib/src/repositories/`: VaultRepository.
- `lib/src/validators/`: PolicyValidator.
- `lib/src/utils/`: WordList, CharSets.
- `lib/src/config/`: ToolkitConfig.
- `lib/src/application/`: ToolkitApp.
- `test/unit/`: Pengujian pembuatan sandi, entropi, dan pendeteksi pola.
- `test/integration/`: Pengujian alur brankas terenkripsi end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
