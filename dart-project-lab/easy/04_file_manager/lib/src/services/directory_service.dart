import 'dart:io';
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

  Map<String, FileTypeGroup> groupFilesByCategory(String dirPath,
      {bool recursive = false}) {
    PathValidator.validateDirectoryExists(dirPath);
    final groups = {
      'Code': FileTypeGroup(categoryName: 'Code', extensions: [
        '.dart',
        '.js',
        '.py',
        '.html',
        '.css',
        '.json',
        '.yaml'
      ]),
      'Images': FileTypeGroup(
          categoryName: 'Images',
          extensions: ['.png', '.jpg', '.jpeg', '.gif', '.svg']),
      'Documents': FileTypeGroup(
          categoryName: 'Documents',
          extensions: ['.txt', '.md', '.pdf', '.docx']),
      'Other': FileTypeGroup(categoryName: 'Other', extensions: []),
    };

    final entities =
        Directory(dirPath).listSync(recursive: recursive).whereType<File>();
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
