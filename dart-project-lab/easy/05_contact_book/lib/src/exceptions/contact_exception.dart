class ContactException implements Exception {
  final String message;
  ContactException(this.message);

  @override
  String toString() => 'ContactException: $message';
}
