import 'contact_exception.dart';

class ValidationException extends ContactException {
  ValidationException(super.message);

  @override
  String toString() => 'ValidationException: $message';
}
