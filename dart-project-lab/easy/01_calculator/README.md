# 01. Calculator CLI

Aplikasi kalkulator baris perintah (*CLI*) berbasis Dart murni yang dilengkapi mesin evaluasi ekspresi matematika Shunting-yard, perhitungan fungsi ilmiah, riwayat kalkulasi, dan penanganan kesalahan aritmetika yang tangguh.

## Fitur Utama
- **Operasi Aritmetika**: Penjumlahan (+), Pengurangan (-), Perkalian (*), Pembagian (/), Modulo (%), dan Pangkat (^).
- **Fungsi Ilmiah**: Sin, Cos, Tan, Log10, Ln, Sqrt, dan Faktorial (!).
- **Mode Sudut**: Derajat (*Degree*) dan Radian (*Radian*).
- **Evaluasi Ekspresi**: Tokenizer (Lexer) dan algoritma Shunting-yard untuk konversi Infix ke Postfix (RPN).
- **Riwayat Perhitungan**: Pencatatan log ekspresi dan hasil dengan fitur *Undo* dan *Clear*.
- **Validasi Input**: Pengecekan keseimbangan tanda kurung dan karakter ilegal.

## Struktur File (22 File Dart)
- `bin/main.dart`: Entry point aplikasi CLI.
- `lib/calculator_cli.dart`: Library export publik.
- `lib/src/models/`: Token, TokenType, AngleMode, CalculationHistory.
- `lib/src/exceptions/`: CalculatorException, SyntaxException, MathDomainException.
- `lib/src/parsers/`: Lexer, ShuntingYard, ExpressionParser.
- `lib/src/services/`: ArithmeticService, ScientificService, EvaluatorService, HistoryService.
- `lib/src/validators/`: InputValidator.
- `lib/src/utils/`: NumberFormatter.
- `lib/src/config/`: CalculatorConfig.
- `lib/src/application/`: CalculatorApp.
- `test/unit/`: Pengujian unit fungsi aritmetika dan parser.
- `test/integration/`: Pengujian alur kalkulasi end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
