class ToolkitException implements Exception {
  final String message;
  ToolkitException(this.message);

  @override
  String toString() => 'ToolkitException: $message';
}
