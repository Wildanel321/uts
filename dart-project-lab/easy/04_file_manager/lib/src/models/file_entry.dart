class FileEntry {
  final String path;
  final String name;
  final int sizeBytes;
  final bool isDirectory;
  final DateTime modifiedAt;
  final String extension;

  FileEntry({
    required this.path,
    required this.name,
    required this.sizeBytes,
    required this.isDirectory,
    required this.modifiedAt,
    required this.extension,
  });

  @override
  String toString() => '$name [${isDirectory ? "DIR" : "$sizeBytes B"}]';
}
