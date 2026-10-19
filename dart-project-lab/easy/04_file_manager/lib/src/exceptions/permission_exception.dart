import 'file_manager_exception.dart';

class PermissionException extends FileManagerException {
  PermissionException(super.message);

  @override
  String toString() => 'PermissionException: $message';
}
