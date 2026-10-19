import '../models/transaction.dart';
import '../exceptions/validation_exception.dart';

class TransactionValidator {
  static void validate(Transaction tx) {
    if (tx.title.trim().isEmpty) {
      throw ValidationException('Transaction title cannot be empty.');
    }
    if (tx.amount <= 0) {
      throw ValidationException(
          'Transaction amount must be strictly positive.');
    }
    if (tx.categoryId.trim().isEmpty) {
      throw ValidationException('Category ID must be provided.');
    }
  }
}
