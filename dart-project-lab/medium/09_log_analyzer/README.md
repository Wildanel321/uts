# 09. Log Analyzer

Aplikasi penganalisis berkas log (*Log Analyzer*) berbasis Dart murni. Dirancang untuk memproses berkas log berukuran besar melalui pembacaan berbasis aliran data (*streaming*) hemat memori, mendukung ragam format (Common Log Format/CLF dan Standard Application Logs), penyaringan level log, pengelompokan pola galat (*error clustering*), deteksi anomali keamanan (serangan *brute force*, pemindaian *404 Not Found*), serta ekspor laporan analitik ke format JSON dan CSV.

## Fitur Utama
- **Stream Processing**: Dukungan pemrosesan berkas log raksasa tanpa memuat seluruh file ke memori.
- **Ragam Parser**: Parser Common Log Format (Nginx/Apache) dan Standard App Log Format.
- **Filter Fleksibel**: Filter berdasarkan level (DEBUG, INFO, WARN, ERROR, FATAL), IP, status HTTP, dan kata kunci.
- **Error Clustering**: Pengelompokan pesan kesalahan serupa berdasarkan tanda tangan galat (*error signature*).
- **Deteksi Anomali**: Mendeteksi pola serangan brute force (banyak login gagal berulang) dan pemindaian 404.
- **Ekspor Laporan**: Hasilkan ringkasan statistik komprehensif ke format JSON dan CSV.

## Struktur File (22 File Dart)
- `bin/main.dart`: Entry point CLI interaktif.
- `lib/log_analyzer.dart`: Export publik pustaka.
- `lib/src/models/`: LogLevel, LogEntry, AnalysisReport, FilterCriteria, AnomalyDetectionResult.
- `lib/src/exceptions/`: LogAnalyzerException.
- `lib/src/parsers/`: LogParser, StandardLogParser, ClfLogParser.
- `lib/src/services/`: StreamingReader, FilterService, AggregationService, ErrorClusteringService, AnomalyDetector, ReportExporter.
- `lib/src/utils/`: RegexPatterns.
- `lib/src/config/`: AnalyzerConfig.
- `lib/src/application/`: LogAnalyzerApp.
- `test/unit/`: Pengujian parser log, filter level, dan deteksi anomali.
- `test/integration/`: Pengujian streaming data log dan ekspor laporan end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
