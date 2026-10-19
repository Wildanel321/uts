import '../models/transaction.dart';
import '../models/transaction_type.dart';
import '../repositories/transaction_repository.dart';

class AnalyticsService {
  final TransactionRepository repository;

  AnalyticsService(this.repository);

  Transaction? getHighestExpense() {
    final expenses = repository
        .getAll()
        .where((t) => t.type == TransactionType.expense)
        .toList();
    if (expenses.isEmpty) return null;
    expenses.sort((a, b) => b.amount.compareTo(a.amount));
    return expenses.first;
  }

  double getAverageExpense() {
    final expenses = repository
        .getAll()
        .where((t) => t.type == TransactionType.expense)
        .toList();
    if (expenses.isEmpty) return 0.0;
    final total = expenses.fold(0.0, (acc, t) => acc + t.amount);
    return total / expenses.length;
  }

  Map<String, double> getExpensePercentages() {
    final expenses = repository
        .getAll()
        .where((t) => t.type == TransactionType.expense)
        .toList();
    final total = expenses.fold(0.0, (acc, t) => acc + t.amount);
    if (total == 0) return {};

    final categoryTotals = <String, double>{};
    for (final e in expenses) {
      categoryTotals[e.categoryId] =
          (categoryTotals[e.categoryId] ?? 0.0) + e.amount;
    }

    return categoryTotals.map((cat, amt) => MapEntry(cat, (amt / total) * 100));
  }
}
