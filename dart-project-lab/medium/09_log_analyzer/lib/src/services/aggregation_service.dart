import '../models/analysis_report.dart';
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
