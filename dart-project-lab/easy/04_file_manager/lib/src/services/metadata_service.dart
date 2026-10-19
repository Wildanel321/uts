import 'dart:io';
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
