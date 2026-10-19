class ImportExportResult {
  final int successCount;
  final int failureCount;
  final List<String> errors;

  ImportExportResult({
    required this.successCount,
    required this.failureCount,
    required this.errors,
  });

  bool get hasErrors => errors.isNotEmpty;
}
