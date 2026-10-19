import 'expense_exception.dart';

class ValidationException extends ExpenseException {
  ValidationException(super.message);

  @override
  String toString() => 'ValidationException: $message';
}
