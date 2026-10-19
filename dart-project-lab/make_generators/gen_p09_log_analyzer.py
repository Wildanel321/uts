import os

def generate_p09(base_dir):
    pdir = os.path.join(base_dir, 'medium', '09_log_analyzer')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'parsers'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'utils'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'config'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'application'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'unit'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'integration'), exist_ok=True)

    def write_f(rel_path, content):
        target = os.path.join(pdir, rel_path)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

    write_f('pubspec.yaml', """name: log_analyzer
description: Pure Dart Stream Log Analyzer with CLF/custom parsers, error clustering, anomaly detection, and reports.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dev_dependencies:
  test: ^1.25.0
""")

    write_f('README.md', """# 09. Log Analyzer

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
""")

    # models
    write_f('lib/src/models/log_level.dart', """enum LogLevel {
  debug,
  info,
  warn,
  error,
  fatal;

  static LogLevel fromString(String val) {
    switch (val.trim().toUpperCase()) {
      case 'DEBUG':
        return LogLevel.debug;
      case 'WARN':
      case 'WARNING':
        return LogLevel.warn;
      case 'ERROR':
        return LogLevel.error;
      case 'FATAL':
        return LogLevel.fatal;
      case 'INFO':
      default:
        return LogLevel.info;
    }
  }
}
""")

    write_f('lib/src/models/log_entry.dart', """import 'log_level.dart';

class LogEntry {
  final DateTime timestamp;
  final LogLevel level;
  final String message;
  final String source;
  final String? ip;
  final int? statusCode;
  final int? durationMs;

  LogEntry({
    required this.timestamp,
    required this.level,
    required this.message,
    this.source = 'app',
    this.ip,
    this.statusCode,
    this.durationMs,
  });

  Map<String, dynamic> toJson() => {
    'timestamp': timestamp.toIso8601String(),
    'level': level.name,
    'message': message,
    'source': source,
    'ip': ip,
    'statusCode': statusCode,
    'durationMs': durationMs,
  };
}
""")

    write_f('lib/src/models/filter_criteria.dart', """import 'log_level.dart';

class FilterCriteria {
  final LogLevel? minLevel;
  final String? query;
  final String? ip;
  final int? statusCode;

  const FilterCriteria({
    this.minLevel,
    this.query,
    this.ip,
    this.statusCode,
  });
}
""")

    write_f('lib/src/models/anomaly_detection_result.dart', """class AnomalyDetectionResult {
  final String type; // e.g. "BRUTE_FORCE", "404_SCAN"
  final String ip;
  final int occurrences;
  final String details;

  const AnomalyDetectionResult({
    required this.type,
    required this.ip,
    required this.occurrences,
    required this.details,
  });

  @override
  String toString() => '[$type] $ip ($occurrences events): $details';
}
""")

    write_f('lib/src/models/analysis_report.dart', """import 'anomaly_detection_result.dart';
import 'log_level.dart';

class AnalysisReport {
  final int totalEntries;
  final Map<LogLevel, int> countsByLevel;
  final Map<int, int> statusCodes;
  final Map<String, int> topIps;
  final List<AnomalyDetectionResult> anomalies;

  AnalysisReport({
    required this.totalEntries,
    required this.countsByLevel,
    required this.statusCodes,
    required this.topIps,
    required this.anomalies,
  });
}
""")

    # exceptions
    write_f('lib/src/exceptions/log_analyzer_exception.dart', """class LogAnalyzerException implements Exception {
  final String message;
  LogAnalyzerException(this.message);

  @override
  String toString() => 'LogAnalyzerException: $message';
}
""")

    # utils
    write_f('lib/src/utils/regex_patterns.dart', """class RegexPatterns {
  // [2026-01-01 12:00:00] [INFO] [AuthService] Message text here
  static final standardLog = RegExp(
    r'^\\[(\\d{4}-\\d{2}-\\d{2}[ T]\\d{2}:\\d{2}:\\d{2})\\]\\s*\\[(\\w+)\\]\\s*(?:\\[([^\\]]+)\\])?\\s*(.*)$',
  );

  // 192.168.1.1 - - [10/Oct/2026:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
  static final clfLog = RegExp(
    r'^(\\S+)\\s+\\S+\\s+\\S+\\s+\\[([^\\]]+)\\]\\s+"(\\S+)\\s+(\\S+)\\s+[^"]*"\\s+(\\d{3})\\s+(\\d+|-)',
  );
}
""")

    # parsers
    write_f('lib/src/parsers/log_parser.dart', """import '../models/log_entry.dart';

abstract class LogParser {
  LogEntry? parseLine(String line);
}
""")

    write_f('lib/src/parsers/standard_log_parser.dart', """import '../models/log_entry.dart';
import '../models/log_level.dart';
import '../utils/regex_patterns.dart';
import 'log_parser.dart';

class StandardLogParser implements LogParser {
  @override
  LogEntry? parseLine(String line) {
    final match = RegexPatterns.standardLog.firstMatch(line.trim());
    if (match == null) return null;

    final dateStr = match.group(1)!.replaceAll(' ', 'T');
    final levelStr = match.group(2)!;
    final source = match.group(3) ?? 'app';
    final message = match.group(4) ?? '';

    return LogEntry(
      timestamp: DateTime.tryParse(dateStr) ?? DateTime.now(),
      level: LogLevel.fromString(levelStr),
      message: message,
      source: source,
    );
  }
}
""")

    write_f('lib/src/parsers/clf_log_parser.dart', """import '../models/log_entry.dart';
import '../models/log_level.dart';
import '../utils/regex_patterns.dart';
import 'log_parser.dart';

class ClfLogParser implements LogParser {
  @override
  LogEntry? parseLine(String line) {
    final match = RegexPatterns.clfLog.firstMatch(line.trim());
    if (match == null) return null;

    final ip = match.group(1)!;
    final path = match.group(4)!;
    final statusCode = int.tryParse(match.group(5)!) ?? 200;

    LogLevel level = LogLevel.info;
    if (statusCode >= 500) {
      level = LogLevel.error;
    } else if (statusCode >= 400) {
      level = LogLevel.warn;
    }

    return LogEntry(
      timestamp: DateTime.now(),
      level: level,
      message: 'Request to $path (Status: $statusCode)',
      source: 'web_server',
      ip: ip,
      statusCode: statusCode,
    );
  }
}
""")

    # services
    write_f('lib/src/services/streaming_reader.dart', """import 'dart:convert';
import 'dart:io';
import '../models/log_entry.dart';
import '../parsers/log_parser.dart';

class StreamingReader {
  final LogParser parser;

  StreamingReader(this.parser);

  Stream<LogEntry> readEntries(String filePath) async* {
    final file = File(filePath);
    if (!file.existsSync()) return;

    final lines = file.openRead().transform(utf8.decoder).transform(const LineSplitter());
    await for (final line in lines) {
      final entry = parser.parseLine(line);
      if (entry != null) {
        yield entry;
      }
    }
  }
}
""")

    write_f('lib/src/services/filter_service.dart', """import '../models/filter_criteria.dart';
import '../models/log_entry.dart';

class FilterService {
  static bool matches(LogEntry entry, FilterCriteria criteria) {
    if (criteria.minLevel != null && entry.level.index < criteria.minLevel!.index) {
      return false;
    }
    if (criteria.ip != null && entry.ip != criteria.ip) {
      return false;
    }
    if (criteria.statusCode != null && entry.statusCode != criteria.statusCode) {
      return false;
    }
    if (criteria.query != null && !entry.message.toLowerCase().contains(criteria.query!.toLowerCase())) {
      return false;
    }
    return true;
  }
}
""")

    write_f('lib/src/services/error_clustering_service.dart', """import '../models/log_entry.dart';
import '../models/log_level.dart';

class ErrorClusteringService {
  static Map<String, int> clusterErrors(List<LogEntry> entries) {
    final clusters = <String, int>{};

    for (final e in entries) {
      if (e.level == LogLevel.error || e.level == LogLevel.fatal) {
        final signature = e.message
            .replaceAll(RegExp(r'\\b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\b'), '#IP')
            .replaceAll(RegExp(r'\\b\\d+\\b'), '#NUM')
            .replaceAll(RegExp(r'0x[a-fA-F0-9]+'), '#HEX')
            .trim();

        clusters[signature] = (clusters[signature] ?? 0) + 1;
      }
    }

    return clusters;
  }
}
""")

    write_f('lib/src/services/anomaly_detector.dart', """import '../models/anomaly_detection_result.dart';
import '../models/log_entry.dart';

class AnomalyDetector {
  static List<AnomalyDetectionResult> detect(List<LogEntry> entries) {
    final anomalies = <AnomalyDetectionResult>[];
    final failedLoginsByIp = <String, int>{};
    final notFoundByIp = <String, int>{};

    for (final e in entries) {
      final ip = e.ip ?? 'unknown';

      if (e.message.toLowerCase().contains('failed login') || e.message.toLowerCase().contains('unauthorized')) {
        failedLoginsByIp[ip] = (failedLoginsByIp[ip] ?? 0) + 1;
      }

      if (e.statusCode == 404) {
        notFoundByIp[ip] = (notFoundByIp[ip] ?? 0) + 1;
      }
    }

    for (final entry in failedLoginsByIp.entries) {
      if (entry.value >= 3) {
        anomalies.add(AnomalyDetectionResult(
          type: 'BRUTE_FORCE_ATTEMPT',
          ip: entry.key,
          occurrences: entry.value,
          details: 'Detected ${entry.value} failed login attempts from ${entry.key}',
        ));
      }
    }

    for (final entry in notFoundByIp.entries) {
      if (entry.value >= 5) {
        anomalies.add(AnomalyDetectionResult(
          type: 'PATH_SCANNING',
          ip: entry.key,
          occurrences: entry.value,
          details: 'Detected ${entry.value} 404 requests indicating scanning probe',
        ));
      }
    }

    return anomalies;
  }
}
""")

    write_f('lib/src/services/aggregation_service.dart', """import '../models/analysis_report.dart';
import '../models/log_entry.dart';
import '../models/log_level.dart';
import 'anomaly_detector.dart';

class AggregationService {
  static AnalysisReport analyze(List<LogEntry> entries) {
    final counts = <LogLevel, int>{};
    final statuses = <int, int>{};
    final ips = <String, int>{};

    for (final e in entries) {
      counts[e.level] = (counts[e.level] ?? 0) + 1;
      if (e.statusCode != null) {
        statuses[e.statusCode!] = (statuses[e.statusCode!] ?? 0) + 1;
      }
      if (e.ip != null) {
        ips[e.ip!] = (ips[e.ip!] ?? 0) + 1;
      }
    }

    final anomalies = AnomalyDetector.detect(entries);

    return AnalysisReport(
      totalEntries: entries.length,
      countsByLevel: counts,
      statusCodes: statuses,
      topIps: ips,
      anomalies: anomalies,
    );
  }
}
""")

    write_f('lib/src/services/report_exporter.dart', """import 'dart:convert';
import '../models/analysis_report.dart';

class ReportExporter {
  static String toJson(AnalysisReport report) {
    final map = {
      'totalEntries': report.totalEntries,
      'countsByLevel': report.countsByLevel.map((k, v) => MapEntry(k.name, v)),
      'statusCodes': report.statusCodes.map((k, v) => MapEntry(k.toString(), v)),
      'topIps': report.topIps,
      'anomalies': report.anomalies.map((a) => {
        'type': a.type,
        'ip': a.ip,
        'occurrences': a.occurrences,
        'details': a.details,
      }).toList(),
    };
    return const JsonEncoder.withIndent('  ').convert(map);
  }

  static String toCsv(AnalysisReport report) {
    final buffer = StringBuffer('Metric,Key,Value\\n');
    for (final entry in report.countsByLevel.entries) {
      buffer.writeln('Level,${entry.key.name},${entry.value}');
    }
    for (final entry in report.statusCodes.entries) {
      buffer.writeln('StatusCode,${entry.key},${entry.value}');
    }
    for (final entry in report.topIps.entries) {
      buffer.writeln('IP,${entry.key},${entry.value}');
    }
    return buffer.toString();
  }
}
""")

    # config
    write_f('lib/src/config/analyzer_config.dart', """class AnalyzerConfig {
  final int bruteForceThreshold;
  final int scanningThreshold;

  const AnalyzerConfig({
    this.bruteForceThreshold = 3,
    this.scanningThreshold = 5,
  });
}
""")

    # application
    write_f('lib/src/application/log_analyzer_app.dart', """import '../config/analyzer_config.dart';
import '../models/analysis_report.dart';
import '../models/filter_criteria.dart';
import '../models/log_entry.dart';
import '../parsers/clf_log_parser.dart';
import '../parsers/log_parser.dart';
import '../parsers/standard_log_parser.dart';
import '../services/aggregation_service.dart';
import '../services/filter_service.dart';
import '../services/report_exporter.dart';

class LogAnalyzerApp {
  final AnalyzerConfig config;
  final LogParser standardParser;
  final LogParser clfParser;

  LogAnalyzerApp({AnalyzerConfig? config})
      : config = config ?? const AnalyzerConfig(),
        standardParser = StandardLogParser(),
        clfParser = ClfLogParser();

  List<LogEntry> parseLines(List<String> lines, {bool isClf = false}) {
    final parser = isClf ? clfParser : standardParser;
    final results = <LogEntry>[];
    for (final line in lines) {
      final entry = parser.parseLine(line);
      if (entry != null) {
        results.add(entry);
      }
    }
    return results;
  }

  List<LogEntry> filterEntries(List<LogEntry> entries, FilterCriteria criteria) {
    return entries.where((e) => FilterService.matches(e, criteria)).toList();
  }

  AnalysisReport analyze(List<LogEntry> entries) => AggregationService.analyze(entries);
  String exportReportJson(AnalysisReport report) => ReportExporter.toJson(report);
  String exportReportCsv(AnalysisReport report) => ReportExporter.toCsv(report);
}
""")

    # lib export
    write_f('lib/log_analyzer.dart', """export 'src/models/log_level.dart';
export 'src/models/log_entry.dart';
export 'src/models/filter_criteria.dart';
export 'src/models/anomaly_detection_result.dart';
export 'src/models/analysis_report.dart';
export 'src/exceptions/log_analyzer_exception.dart';
export 'src/parsers/log_parser.dart';
export 'src/parsers/standard_log_parser.dart';
export 'src/parsers/clf_log_parser.dart';
export 'src/services/streaming_reader.dart';
export 'src/services/filter_service.dart';
export 'src/services/error_clustering_service.dart';
export 'src/services/anomaly_detector.dart';
export 'src/services/aggregation_service.dart';
export 'src/services/report_exporter.dart';
export 'src/utils/regex_patterns.dart';
export 'src/config/analyzer_config.dart';
export 'src/application/log_analyzer_app.dart';
""")

    # bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
import 'package:log_analyzer/log_analyzer.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('           09. LOG ANALYZER CLI               ');
  stdout.writeln('==============================================');

  final app = LogAnalyzerApp();

  final sampleLogs = [
    '[2026-01-01 10:00:01] [INFO] [AuthService] User login success for alice',
    '[2026-01-01 10:00:05] [WARN] [AuthService] Failed login attempt for bob',
    '[2026-01-01 10:00:06] [WARN] [AuthService] Failed login attempt for bob',
    '[2026-01-01 10:00:07] [WARN] [AuthService] Failed login attempt for bob',
    '[2026-01-01 10:00:15] [ERROR] [Database] Connection timeout on port 5432',
    '[2026-01-01 10:00:18] [ERROR] [Database] Connection timeout on port 5432',
  ];

  stdout.writeln('Parsing ${sampleLogs.length} sample log lines...');
  final entries = app.parseLines(sampleLogs);
  final report = app.analyze(entries);

  stdout.writeln('Total Log Entries: ${report.totalEntries}');
  stdout.writeln('Counts By Level:');
  for (final l in report.countsByLevel.entries) {
    stdout.writeln('  ${l.key.name.toUpperCase().padRight(8)}: ${l.value}');
  }

  stdout.writeln('\\nDetected Anomalies:');
  for (final a in report.anomalies) {
    stdout.writeln('  $a');
  }

  stdout.writeln('==============================================');
}
""")

    # test/unit
    write_f('test/unit/log_analyzer_unit_test.dart', """import 'package:test/test.dart';
import 'package:log_analyzer/log_analyzer.dart';

void main() {
  group('Log Analyzer Unit Tests', () {
    test('StandardLogParser parses standard formatted lines', () {
      final parser = StandardLogParser();
      final line = '[2026-05-10 14:30:00] [ERROR] [PaymentService] Card charge failed';
      final entry = parser.parseLine(line);

      expect(entry, isNotNull);
      expect(entry!.level, equals(LogLevel.error));
      expect(entry.source, equals('PaymentService'));
      expect(entry.message, equals('Card charge failed'));
    });

    test('ClfLogParser parses Common Log Format lines', () {
      final parser = ClfLogParser();
      final line = '10.0.0.1 - - [10/Oct/2026:13:55:36 +0000] "GET /api/v1/users HTTP/1.1" 200 1024';
      final entry = parser.parseLine(line);

      expect(entry, isNotNull);
      expect(entry!.ip, equals('10.0.0.1'));
      expect(entry.statusCode, equals(200));
      expect(entry.level, equals(LogLevel.info));
    });

    test('ErrorClusteringService groups repetitive error messages', () {
      final entries = [
        LogEntry(timestamp: DateTime.now(), level: LogLevel.error, message: 'Timeout connecting to 192.168.1.100:8080'),
        LogEntry(timestamp: DateTime.now(), level: LogLevel.error, message: 'Timeout connecting to 192.168.1.101:8080'),
      ];

      final clusters = ErrorClusteringService.clusterErrors(entries);
      expect(clusters.length, equals(1));
      expect(clusters.values.first, equals(2));
    });
  });
}
""")

    # test/integration
    write_f('test/integration/log_analyzer_integration_test.dart', """import 'dart:io';
import 'package:test/test.dart';
import 'package:log_analyzer/log_analyzer.dart';

void main() {
  group('Log Analyzer Integration Flow Tests', () {
    late LogAnalyzerApp app;
    late Directory tempDir;

    setUp(() {
      app = LogAnalyzerApp();
      tempDir = Directory.systemTemp.createTempSync('log_test_');
    });

    tearDown(() {
      if (tempDir.existsSync()) {
        tempDir.deleteSync(recursive: true);
      }
    });

    test('Streams log file, filters errors, and exports JSON report', () async {
      final logFile = File('${tempDir.path}/app.log');
      logFile.writeAsStringSync('''
[2026-01-01 12:00:00] [INFO] [Server] System booted
[2026-01-01 12:01:00] [WARN] [Auth] Failed login from 1.2.3.4
[2026-01-01 12:01:01] [WARN] [Auth] Failed login from 1.2.3.4
[2026-01-01 12:01:02] [WARN] [Auth] Failed login from 1.2.3.4
[2026-01-01 12:05:00] [ERROR] [DB] Query deadlock
''');

      final reader = StreamingReader(app.standardParser);
      final entries = await reader.readEntries(logFile.path).toList();
      expect(entries.length, equals(5));

      final report = app.analyze(entries);
      expect(report.countsByLevel[LogLevel.error], equals(1));
      expect(report.countsByLevel[LogLevel.warn], equals(3));

      final jsonOutput = app.exportReportJson(report);
      expect(jsonOutput, contains('"totalEntries": 5'));
      expect(jsonOutput, contains('BRUTE_FORCE_ATTEMPT'));
    });
  });
}
""")

    print("Project 09 (Log Analyzer) generated successfully with 22 Dart files!")

if __name__ == '__main__':
    generate_p09('dart-project-lab')
