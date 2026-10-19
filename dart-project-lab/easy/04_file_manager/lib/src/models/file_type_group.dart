class FileTypeGroup {
  final String categoryName;
  final List<String> extensions;
  int fileCount;
  int totalBytes;

  FileTypeGroup({
    required this.categoryName,
    required this.extensions,
    this.fileCount = 0,
    this.totalBytes = 0,
  });

  void addFile(int bytes) {
    fileCount++;
    totalBytes += bytes;
  }
}
