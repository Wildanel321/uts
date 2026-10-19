import 'dart:io';
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
