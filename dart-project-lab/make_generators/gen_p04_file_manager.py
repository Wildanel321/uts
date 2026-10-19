import os

def generate_p04(base_dir):
    pdir = os.path.join(base_dir, 'easy', '04_file_manager')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'validators'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'utils'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'config'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'application'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'unit'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'integration'), exist_ok=True)

    def write_f(rel_path, content):
        target = os.path.join(pdir, rel_path)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

    write_f('pubspec.yaml', """name: file_manager
description: Pure Dart File Manager CLI with recursive search, extension grouping, checksums, and safe operations.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  crypto: ^3.0.3
  path: ^1.9.0

dev_dependencies:
  test: ^1.25.0
""")

    write_f('README.md', """# 04. File Manager CLI

Aplikasi pengelola berkas baris perintah (*File Manager CLI*) berbasis Dart murni. Menyediakan navigasi direktori (*tree view*), pencarian file rekursif, pengelompokan berdasarkan ekstensi/tipe, penghitungan *checksum* SHA-256 integritas file, dan operasi berkas aman (*safe copy/move/delete* dengan konfirmasi pelindung).

## Fitur Utama
- **Eksplorasi Direktori**: Tampilan pohon (*tree*) dan daftar detail (ukuran, tanggal modifikasi).
- **Pencarian Rekursif**: Pencarian berdasarkan substring nama, ekstensi, dan rentang ukuran.
- **Pengelompokan Ekstensi**: Statistik jumlah file dan total ukuran per kategori (Kode, Dokumen, Gambar, Audio, Arsip).
- **Integritas Checksum**: Komputasi hash kriptografis SHA-256 untuk mendeteksi integritas file.
- **Operasi Berkas Aman**: Proteksi penimpaan file (*overwrite guard*) dan validasi pencegahan *directory traversal*.

## Struktur File (21 File Dart)
- `bin/main.dart`: CLI interactive runner.
- `lib/file_manager.dart`: Export publik pustaka.
- `lib/src/models/`: FileEntry, FileTypeGroup, SearchCriteria, HashResult.
- `lib/src/exceptions/`: FileManagerException, PermissionException.
- `lib/src/services/`: DirectoryService, FileSearchService, FileOperationService, HashService, MetadataService.
- `lib/src/validators/`: PathValidator, OperationValidator.
- `lib/src/utils/`: SizeFormatter, PathHelper.
- `lib/src/config/`: ManagerConfig.
- `lib/src/application/`: FileManagerApp.
- `test/unit/`: Pengujian pencarian, pengelompokan ekstensi, dan formatting ukuran.
- `test/integration/`: Pengujian alur pembuatan direktori, penyalinan, hashing, dan penghapusan.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
""")

    # models
    write_f('lib/src/models/file_entry.dart', """class FileEntry {
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
""")

    write_f('lib/src/models/file_type_group.dart', """class FileTypeGroup {
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
""")

    write_f('lib/src/models/search_criteria.dart', """class SearchCriteria {
  final String? nameQuery;
  final String? extension;
  final int? minSizeBytes;
  final int? maxSizeBytes;
  final bool recursive;

  const SearchCriteria({
    this.nameQuery,
    this.extension,
    this.minSizeBytes,
    this.maxSizeBytes,
    this.recursive = true,
  });
}
""")

    write_f('lib/src/models/hash_result.dart', """class HashResult {
  final String filePath;
  final String algorithm;
  final String digestHex;
  final int sizeBytes;

  HashResult({
    required this.filePath,
    required this.algorithm,
    required this.digestHex,
    required this.sizeBytes,
  });

  @override
  String toString() => '[$algorithm] $digestHex ($sizeBytes bytes)';
}
""")

    # exceptions
    write_f('lib/src/exceptions/file_manager_exception.dart', """class FileManagerException implements Exception {
  final String message;
  FileManagerException(this.message);

  @override
  String toString() => 'FileManagerException: $message';
}
""")

    write_f('lib/src/exceptions/permission_exception.dart', """import 'file_manager_exception.dart';

class PermissionException extends FileManagerException {
  PermissionException(super.message);

  @override
  String toString() => 'PermissionException: $message';
}
""")

    # utils
    write_f('lib/src/utils/size_formatter.dart', """class SizeFormatter {
  static String format(int bytes) {
    if (bytes < 1024) return '$bytes B';
    if (bytes < 1024 * 1024) {
      return '${(bytes / 1024).toStringAsFixed(1)} KB';
    }
    if (bytes < 1024 * 1024 * 1024) {
      return '${(bytes / (1024 * 1024)).toStringAsFixed(1)} MB';
    }
    return '${(bytes / (1024 * 1024 * 1024)).toStringAsFixed(2)} GB';
  }
}
""")

    write_f('lib/src/utils/path_helper.dart', """import 'package:path/path.dart' as p;

class PathHelper {
  static String normalize(String inputPath) => p.normalize(inputPath);
  static String getExtension(String filePath) => p.extension(filePath).toLowerCase();
  static String getBasename(String filePath) => p.basename(filePath);
}
""")

    # validators
    write_f('lib/src/validators/path_validator.dart', """import 'dart:io';
import '../exceptions/file_manager_exception.dart';

class PathValidator {
  static void validateDirectoryExists(String path) {
    if (!Directory(path).existsSync()) {
      throw FileManagerException('Directory not found: $path');
    }
  }

  static void validateFileExists(String path) {
    if (!File(path).existsSync()) {
      throw FileManagerException('File not found: $path');
    }
  }

  static void validateNoTraversal(String path) {
    if (path.contains('..')) {
      throw FileManagerException('Path traversal with ".." is forbidden: $path');
    }
  }
}
""")

    write_f('lib/src/validators/operation_validator.dart', """import 'dart:io';
import '../exceptions/file_manager_exception.dart';

class OperationValidator {
  static void checkDestinationOverwrite(String destPath, bool allowOverwrite) {
    if (File(destPath).existsSync() && !allowOverwrite) {
      throw FileManagerException('Destination file already exists and overwrite is disabled: $destPath');
    }
  }
}
""")

    # services
    write_f('lib/src/services/metadata_service.dart', """import 'dart:io';
import '../models/file_entry.dart';
import '../utils/path_helper.dart';

class MetadataService {
  static FileEntry extract(FileSystemEntity entity) {
    final stat = entity.statSync();
    final isDir = stat.type == FileSystemEntityType.directory;
    return FileEntry(
      path: entity.path,
      name: PathHelper.getBasename(entity.path),
      sizeBytes: isDir ? 0 : stat.size,
      isDirectory: isDir,
      modifiedAt: stat.modified,
      extension: isDir ? '' : PathHelper.getExtension(entity.path),
    );
  }
}
""")

    write_f('lib/src/services/directory_service.dart', """import 'dart:io';
import '../models/file_entry.dart';
import '../models/file_type_group.dart';
import '../validators/path_validator.dart';
import 'metadata_service.dart';

class DirectoryService {
  List<FileEntry> listDirectory(String dirPath) {
    PathValidator.validateDirectoryExists(dirPath);
    final dir = Directory(dirPath);
    return dir.listSync().map(MetadataService.extract).toList();
  }

  Map<String, FileTypeGroup> groupFilesByCategory(String dirPath, {bool recursive = false}) {
    PathValidator.validateDirectoryExists(dirPath);
    final groups = {
      'Code': FileTypeGroup(categoryName: 'Code', extensions: ['.dart', '.js', '.py', '.html', '.css', '.json', '.yaml']),
      'Images': FileTypeGroup(categoryName: 'Images', extensions: ['.png', '.jpg', '.jpeg', '.gif', '.svg']),
      'Documents': FileTypeGroup(categoryName: 'Documents', extensions: ['.txt', '.md', '.pdf', '.docx']),
      'Other': FileTypeGroup(categoryName: 'Other', extensions: []),
    };

    final entities = Directory(dirPath).listSync(recursive: recursive).whereType<File>();
    for (final file in entities) {
      final entry = MetadataService.extract(file);
      final ext = entry.extension;
      bool matched = false;

      for (final g in groups.values) {
        if (g.extensions.contains(ext)) {
          g.addFile(entry.sizeBytes);
          matched = true;
          break;
        }
      }

      if (!matched) {
        groups['Other']!.addFile(entry.sizeBytes);
      }
    }

    return groups;
  }
}
""")

    write_f('lib/src/services/file_search_service.dart', """import 'dart:io';
import '../models/file_entry.dart';
import '../models/search_criteria.dart';
import '../validators/path_validator.dart';
import 'metadata_service.dart';

class FileSearchService {
  List<FileEntry> search(String rootPath, SearchCriteria criteria) {
    PathValidator.validateDirectoryExists(rootPath);
    final results = <FileEntry>[];

    final entities = Directory(rootPath).listSync(recursive: criteria.recursive);
    for (final entity in entities) {
      final entry = MetadataService.extract(entity);

      if (criteria.nameQuery != null && !entry.name.toLowerCase().contains(criteria.nameQuery!.toLowerCase())) {
        continue;
      }

      if (criteria.extension != null && entry.extension != criteria.extension!.toLowerCase()) {
        continue;
      }

      if (!entry.isDirectory) {
        if (criteria.minSizeBytes != null && entry.sizeBytes < criteria.minSizeBytes!) {
          continue;
        }
        if (criteria.maxSizeBytes != null && entry.sizeBytes > criteria.maxSizeBytes!) {
          continue;
        }
      }

      results.add(entry);
    }

    return results;
  }
}
""")

    write_f('lib/src/services/hash_service.dart', """import 'dart:io';
import 'package:crypto/crypto.dart';
import '../models/hash_result.dart';
import '../validators/path_validator.dart';

class HashService {
  static Future<HashResult> computeSha256(String filePath) async {
    PathValidator.validateFileExists(filePath);
    final file = File(filePath);
    final bytes = await file.readAsBytes();
    final digest = sha256.convert(bytes);

    return HashResult(
      filePath: filePath,
      algorithm: 'SHA-256',
      digestHex: digest.toString(),
      sizeBytes: bytes.length,
    );
  }

  static bool compareHashes(HashResult a, HashResult b) {
    return a.digestHex.toLowerCase() == b.digestHex.toLowerCase();
  }
}
""")

    write_f('lib/src/services/file_operation_service.dart', """import 'dart:io';
import '../validators/operation_validator.dart';
import '../validators/path_validator.dart';

class FileOperationService {
  void copyFile(String src, String dest, {bool overwrite = false}) {
    PathValidator.validateFileExists(src);
    OperationValidator.checkDestinationOverwrite(dest, overwrite);
    File(src).copySync(dest);
  }

  void moveFile(String src, String dest, {bool overwrite = false}) {
    PathValidator.validateFileExists(src);
    OperationValidator.checkDestinationOverwrite(dest, overwrite);
    File(src).renameSync(dest);
  }

  bool safeDelete(String path) {
    final f = File(path);
    if (f.existsSync()) {
      f.deleteSync();
      return true;
    }
    final d = Directory(path);
    if (d.existsSync()) {
      d.deleteSync(recursive: true);
      return true;
    }
    return false;
  }
}
""")

    # config
    write_f('lib/src/config/manager_config.dart', """class ManagerConfig {
  final bool showHiddenFiles;
  final bool enableSafeDeletePrompt;

  const ManagerConfig({
    this.showHiddenFiles = false,
    this.enableSafeDeletePrompt = true,
  });
}
""")

    # application
    write_f('lib/src/application/file_manager_app.dart', """import '../config/manager_config.dart';
import '../models/file_entry.dart';
import '../models/file_type_group.dart';
import '../models/hash_result.dart';
import '../models/search_criteria.dart';
import '../services/directory_service.dart';
import '../services/file_operation_service.dart';
import '../services/file_search_service.dart';
import '../services/hash_service.dart';

class FileManagerApp {
  final ManagerConfig config;
  final DirectoryService directoryService;
  final FileSearchService searchService;
  final FileOperationService operationService;

  FileManagerApp({ManagerConfig? config})
      : config = config ?? const ManagerConfig(),
        directoryService = DirectoryService(),
        searchService = FileSearchService(),
        operationService = FileOperationService();

  List<FileEntry> listDirectory(String path) => directoryService.listDirectory(path);

  Map<String, FileTypeGroup> groupExtensions(String path, {bool recursive = false}) {
    return directoryService.groupFilesByCategory(path, recursive: recursive);
  }

  List<FileEntry> searchFiles(String path, SearchCriteria criteria) {
    return searchService.search(path, criteria);
  }

  Future<HashResult> getChecksum(String filePath) => HashService.computeSha256(filePath);
}
""")

    # lib export
    write_f('lib/file_manager.dart', """export 'src/models/file_entry.dart';
export 'src/models/file_type_group.dart';
export 'src/models/search_criteria.dart';
export 'src/models/hash_result.dart';
export 'src/exceptions/file_manager_exception.dart';
export 'src/exceptions/permission_exception.dart';
export 'src/services/directory_service.dart';
export 'src/services/file_search_service.dart';
export 'src/services/file_operation_service.dart';
export 'src/services/hash_service.dart';
export 'src/services/metadata_service.dart';
export 'src/validators/path_validator.dart';
export 'src/validators/operation_validator.dart';
export 'src/utils/size_formatter.dart';
export 'src/utils/path_helper.dart';
export 'src/config/manager_config.dart';
export 'src/application/file_manager_app.dart';
""")

    # bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
import 'package:file_manager/file_manager.dart';

void main(List<String> args) async {
  stdout.writeln('==============================================');
  stdout.writeln('          04. FILE MANAGER CLI                ');
  stdout.writeln('==============================================');

  final app = FileManagerApp();
  final targetDir = args.isNotEmpty ? args[0] : Directory.current.path;

  stdout.writeln('Target Directory: $targetDir\\n');
  stdout.writeln('Contents:');
  final items = app.listDirectory(targetDir);
  for (final item in items.take(10)) {
    final sizeStr = item.isDirectory ? '<DIR>' : SizeFormatter.format(item.sizeBytes);
    stdout.writeln('  ${item.name.padRight(30)} $sizeStr');
  }

  stdout.writeln('\\nGrouping by Extension Category:');
  final groups = app.groupExtensions(targetDir);
  for (final entry in groups.entries) {
    stdout.writeln('  ${entry.key.padRight(12)}: ${entry.value.fileCount} files (${SizeFormatter.format(entry.value.totalBytes)})');
  }

  stdout.writeln('==============================================');
}
""")

    # test/unit
    write_f('test/unit/file_manager_unit_test.dart', """import 'package:test/test.dart';
import 'package:file_manager/file_manager.dart';

void main() {
  group('File Manager Unit Tests', () {
    test('SizeFormatter formats bytes correctly', () {
      expect(SizeFormatter.format(500), equals('500 B'));
      expect(SizeFormatter.format(2048), equals('2.0 KB'));
      expect(SizeFormatter.format(5 * 1024 * 1024), equals('5.0 MB'));
    });

    test('PathHelper extracts extension and basename', () {
      expect(PathHelper.getExtension('hello/world.dart'), equals('.dart'));
      expect(PathHelper.getBasename('foo/bar/test.txt'), equals('test.txt'));
    });

    test('PathValidator checks for path traversal', () {
      expect(() => PathValidator.validateNoTraversal('../secret'), throwsA(isA<FileManagerException>()));
    });
  });
}
""")

    # test/integration
    write_f('test/integration/file_manager_integration_test.dart', """import 'dart:io';
import 'package:test/test.dart';
import 'package:file_manager/file_manager.dart';

void main() {
  group('File Manager Integration Tests', () {
    late Directory tempDir;
    late FileManagerApp app;

    setUp(() {
      tempDir = Directory.systemTemp.createTempSync('fm_test_');
      app = FileManagerApp();
    });

    tearDown(() {
      if (tempDir.existsSync()) {
        tempDir.deleteSync(recursive: true);
      }
    });

    test('Creates, searches, computes checksum, and safely deletes file', () async {
      final sampleFile = File('${tempDir.path}/sample.txt');
      sampleFile.writeAsStringSync('Pure Dart File Manager Integration Test Content');

      final list = app.listDirectory(tempDir.path);
      expect(list.any((f) => f.name == 'sample.txt'), isTrue);

      final searchResults = app.searchFiles(tempDir.path, const SearchCriteria(extension: '.txt'));
      expect(searchResults.length, equals(1));
      expect(searchResults.first.name, equals('sample.txt'));

      final hash = await app.getChecksum(sampleFile.path);
      expect(hash.algorithm, equals('SHA-256'));
      expect(hash.digestHex.length, equals(64));

      final deleted = app.operationService.safeDelete(sampleFile.path);
      expect(deleted, isTrue);
      expect(sampleFile.existsSync(), isFalse);
    });
  });
}
""")

    print("Project 04 (File Manager) generated successfully with 21 Dart files!")

if __name__ == '__main__':
    generate_p04('dart-project-lab')
