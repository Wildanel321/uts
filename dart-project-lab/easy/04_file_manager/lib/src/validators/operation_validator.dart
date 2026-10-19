import 'dart:io';
import '../exceptions/file_manager_exception.dart';

class OperationValidator {
  static void checkDestinationOverwrite(String destPath, bool allowOverwrite) {
    if (File(destPath).existsSync() && !allowOverwrite) {
      throw FileManagerException(
          'Destination file already exists and overwrite is disabled: $destPath');
    }
  }
}
