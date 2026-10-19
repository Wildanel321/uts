import '../models/log_entry.dart';
import '../models/log_level.dart';

class ErrorClusteringService {
  static Map<String, int> clusterErrors(List<LogEntry> entries) {
    final clusters = <String, int>{};

    for (final e in entries) {
      if (e.level == LogLevel.error || e.level == LogLevel.fatal) {
        final signature = e.message
            .replaceAll(
                RegExp(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'), '#IP')
            .replaceAll(RegExp(r'\b\d+\b'), '#NUM')
            .replaceAll(RegExp(r'0x[a-fA-F0-9]+'), '#HEX')
            .trim();

        clusters[signature] = (clusters[signature] ?? 0) + 1;
      }
    }

    return clusters;
  }
}
