import '../models/transaction.dart';
import '../models/transaction_type.dart';
import '../repositories/transaction_repository.dart';
import '../validators/transaction_validator.dart';

class ExpenseService {
  final TransactionRepository repository;
  static int _idCounter = 0;

  ExpenseService(this.repository);

  Transaction addTransaction({
    required String title,
    required double amount,
    required TransactionType type,
    required String categoryId,
    DateTime? date,
    String note = '',
  }) {
    final id = 'tx_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}';
    final tx = Transaction(
      id: id,
      title: title,
      amount: amount,
      type: type,
      categoryId: categoryId,
      date: date,
      note: note,
    );

    TransactionValidator.validate(tx);
    repository.save(tx);
    return tx;
  }

  bool deleteTransaction(String id) => repository.delete(id);

  List<Transaction> listAll() => repository.getAll();

  List<Transaction> filterByType(TransactionType type) {
    return repository.getAll().where((t) => t.type == type).toList();
  }
}
