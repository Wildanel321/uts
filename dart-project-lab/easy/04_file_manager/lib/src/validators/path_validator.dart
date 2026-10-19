import 'dart:io';
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
      throw FileManagerException(
          'Path traversal with ".." is forbidden: $path');
    }
  }
}
