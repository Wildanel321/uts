import 'toolkit_exception.dart';

class VaultException extends ToolkitException {
  VaultException(super.message);

  @override
  String toString() => 'VaultException: $message';
}
