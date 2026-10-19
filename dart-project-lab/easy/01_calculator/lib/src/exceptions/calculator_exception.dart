class CalculatorException implements Exception {
  final String message;
  CalculatorException(this.message);

  @override
  String toString() => 'CalculatorException: $message';
}
