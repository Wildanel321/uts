class FileManagerException implements Exception {
  final String message;
  FileManagerException(this.message);

  @override
  String toString() => 'FileManagerException: $message';
}
