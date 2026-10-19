import 'anomaly_detection_result.dart';
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
