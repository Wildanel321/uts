class HistoryEntry {
  final String expression;
  final double result;
  final DateTime timestamp;

  HistoryEntry({
    required this.expression,
    required this.result,
    DateTime? timestamp,
  }) : timestamp = timestamp ?? DateTime.now();

  @override
  String toString() => '[$timestamp] $expression = $result';
}
