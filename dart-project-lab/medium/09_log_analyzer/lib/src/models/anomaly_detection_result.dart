class AnomalyDetectionResult {
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
