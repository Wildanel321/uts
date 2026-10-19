import '../models/budget.dart';
import '../models/transaction_type.dart';
import '../repositories/budget_repository.dart';
import '../repositories/transaction_repository.dart';
import '../utils/date_helper.dart';

class BudgetService {
  final BudgetRepository budgetRepo;
  final TransactionRepository transactionRepo;

  BudgetService(this.budgetRepo, this.transactionRepo);

  void setBudget(int year, int month, double limitAmount) {
    budgetRepo
        .setBudget(Budget(year: year, month: month, limitAmount: limitAmount));
  }

  Budget? getBudget(int year, int month) => budgetRepo.getBudget(year, month);

  double getMonthlyExpense(int year, int month) {
    return transactionRepo
        .getAll()
        .where((t) =>
            t.type == TransactionType.expense &&
            DateHelper.isSameMonth(t.date, year, month))
        .fold(0.0, (sum, t) => sum + t.amount);
  }

  bool isBudgetExceeded(int year, int month) {
    final budget = getBudget(year, month);
    if (budget == null) return false;
    return getMonthlyExpense(year, month) > budget.limitAmount;
  }
}
