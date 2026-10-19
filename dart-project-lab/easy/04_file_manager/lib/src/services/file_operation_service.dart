import 'dart:io';
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
