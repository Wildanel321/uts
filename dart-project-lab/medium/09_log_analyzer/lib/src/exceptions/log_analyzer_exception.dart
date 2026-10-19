class LogAnalyzerException implements Exception {
  final String message;
  LogAnalyzerException(this.message);

  @override
  String toString() => 'LogAnalyzerException: $message';
}
