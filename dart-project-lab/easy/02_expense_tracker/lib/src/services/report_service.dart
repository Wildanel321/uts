import '../models/expense_summary.dart';
import '../models/transaction_type.dart';
import '../repositories/transaction_repository.dart';
import '../utils/date_helper.dart';

class ReportService {
  final TransactionRepository repository;

  ReportService(this.repository);

  ExpenseSummary generateMonthlySummary(int year, int month) {
    final txs = repository
        .getAll()
        .where((t) => DateHelper.isSameMonth(t.date, year, month))
        .toList();

    double income = 0;
    double expense = 0;
    final breakdown = <String, double>{};

    for (final t in txs) {
      if (t.type == TransactionType.income) {
        income += t.amount;
      } else {
        expense += t.amount;
        breakdown[t.categoryId] = (breakdown[t.categoryId] ?? 0.0) + t.amount;
      }
    }

    return ExpenseSummary(
      totalIncome: income,
      totalExpense: expense,
      netBalance: income - expense,
      categoryBreakdown: breakdown,
    );
  }
}
