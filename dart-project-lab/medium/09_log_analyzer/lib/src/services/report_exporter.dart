import 'dart:convert';
import '../models/analysis_report.dart';

class ReportExporter {
  static String toJson(AnalysisReport report) {
    final map = {
      'totalEntries': report.totalEntries,
      'countsByLevel': report.countsByLevel.map((k, v) => MapEntry(k.name, v)),
      'statusCodes':
          report.statusCodes.map((k, v) => MapEntry(k.toString(), v)),
      'topIps': report.topIps,
      'anomalies': report.anomalies
          .map((a) => {
                'type': a.type,
                'ip': a.ip,
                'occurrences': a.occurrences,
                'details': a.details,
              })
          .toList(),
    };
    return const JsonEncoder.withIndent('  ').convert(map);
  }

  static String toCsv(AnalysisReport report) {
    final buffer = StringBuffer('Metric,Key,Value\n');
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
