import 'package:test/test.dart';
import 'package:expense_tracker/expense_tracker.dart';

void main() {
  group('Expense Tracker Integration Flow Tests', () {
    test('Calculates budget overflow and category breakdown correctly', () {
      final app = TrackerApp.create();
      final now = DateTime.now();

      app.addIncome('Freelance Project', 5000000, 'work');
      app.addExpense('Smartphone installment', 3000000, 'gadget');
      app.addExpense('Dinner', 500000, 'food');

      app.budgetService.setBudget(now.year, now.month, 2500000);
      expect(app.budgetService.isBudgetExceeded(now.year, now.month), isTrue);

      final summary =
          app.reportService.generateMonthlySummary(now.year, now.month);
      expect(summary.totalIncome, equals(5000000));
      expect(summary.totalExpense, equals(3500000));
      expect(summary.netBalance, equals(1500000));

      final percentages = app.analyticsService.getExpensePercentages();
      expect(percentages['gadget'], closeTo(85.71, 0.1));
    });
  });
}
