import '../models/anomaly_detection_result.dart';
import '../models/log_entry.dart';

class AnomalyDetector {
  static List<AnomalyDetectionResult> detect(List<LogEntry> entries) {
    final anomalies = <AnomalyDetectionResult>[];
    final failedLoginsByIp = <String, int>{};
    final notFoundByIp = <String, int>{};

    for (final e in entries) {
      final ip = e.ip ?? 'unknown';

      if (e.message.toLowerCase().contains('failed login') ||
          e.message.toLowerCase().contains('unauthorized')) {
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
          details:
              'Detected ${entry.value} failed login attempts from ${entry.key}',
        ));
      }
    }

    for (final entry in notFoundByIp.entries) {
      if (entry.value >= 5) {
        anomalies.add(AnomalyDetectionResult(
          type: 'PATH_SCANNING',
          ip: entry.key,
          occurrences: entry.value,
          details:
              'Detected ${entry.value} 404 requests indicating scanning probe',
        ));
      }
    }

    return anomalies;
  }
}
