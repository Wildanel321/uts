import 'dart:io';
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

  stdout.writeln('\nDetected Anomalies:');
  for (final a in report.anomalies) {
    stdout.writeln('  $a');
  }

  stdout.writeln('==============================================');
}
