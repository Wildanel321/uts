import '../models/budget.dart';

class BudgetRepository {
  final Map<String, Budget> _budgets = {};

  String _key(int year, int month) => '$year-$month';

  void setBudget(Budget budget) {
    _budgets[_key(budget.year, budget.month)] = budget;
  }

  Budget? getBudget(int year, int month) {
    return _budgets[_key(year, month)];
  }

  void clear() => _budgets.clear();
}
