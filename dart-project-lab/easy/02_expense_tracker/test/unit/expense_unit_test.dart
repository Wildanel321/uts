import 'package:test/test.dart';
import 'package:expense_tracker/expense_tracker.dart';

void main() {
  group('Expense Tracker Unit Tests', () {
    late TransactionRepository txRepo;
    late ExpenseService expenseService;

    setUp(() {
      txRepo = TransactionRepository();
      expenseService = ExpenseService(txRepo);
    });

    test('Adds valid transaction successfully', () {
      final tx = expenseService.addTransaction(
        title: 'Lunch',
        amount: 50000,
        type: TransactionType.expense,
        categoryId: 'food',
      );
      expect(tx.id, startsWith('tx_'));
      expect(txRepo.getAll().length, equals(1));
    });

    test('Throws ValidationException for invalid amount or title', () {
      expect(
        () => expenseService.addTransaction(
          title: '',
          amount: 50000,
          type: TransactionType.expense,
          categoryId: 'food',
        ),
        throwsA(isA<ValidationException>()),
      );

      expect(
        () => expenseService.addTransaction(
          title: 'Test',
          amount: -100,
          type: TransactionType.expense,
          categoryId: 'food',
        ),
        throwsA(isA<ValidationException>()),
      );
    });

    test('CSV Parser serialize and deserialize roundtrip', () {
      final tx = Transaction(
        id: '1',
        title: 'Books',
        amount: 120000,
        type: TransactionType.expense,
        categoryId: 'education',
        date: DateTime(2026, 1, 1),
      );
      final csv = CsvParser.toCsv([tx]);
      final restored = CsvParser.fromCsv(csv);
      expect(restored.length, equals(1));
      expect(restored.first.title, equals('Books'));
      expect(restored.first.amount, equals(120000));
    });
  });
}
