class ExpenseException implements Exception {
  final String message;
  ExpenseException(this.message);

  @override
  String toString() => 'ExpenseException: $message';
}
