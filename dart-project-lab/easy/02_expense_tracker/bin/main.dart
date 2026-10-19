import 'dart:io';
import 'package:expense_tracker/expense_tracker.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('          02. EXPENSE & BUDGET TRACKER        ');
  stdout.writeln('==============================================');

  final app = TrackerApp.create();

  // Seed sample transactions
  app.addIncome('Monthly Salary', 15000000, 'salary');
  app.addExpense('Grocery Shopping', 750000, 'food');
  app.addExpense('Internet & Utilities', 450000, 'bills');
  app.addExpense('Fuel & Transit', 200000, 'transport');

  final now = DateTime.now();
  app.budgetService.setBudget(now.year, now.month, 5000000);

  final summary = app.reportService.generateMonthlySummary(now.year, now.month);

  stdout.writeln('Monthly Summary (${now.year}-${now.month}):');
  stdout.writeln('  Total Income  : ${app.formatAmount(summary.totalIncome)}');
  stdout.writeln('  Total Expense : ${app.formatAmount(summary.totalExpense)}');
  stdout.writeln('  Net Balance   : ${app.formatAmount(summary.netBalance)}');
  stdout.writeln('  Budget Limit  : ${app.formatAmount(5000000)}');
  stdout.writeln(
      '  Exceeded?     : ${app.budgetService.isBudgetExceeded(now.year, now.month) ? "YES" : "NO"}');
  stdout.writeln('----------------------------------------------');
  stdout.writeln(
      'Highest Expense : ${app.analyticsService.getHighestExpense()?.title}');
  stdout.writeln(
      'Average Expense : ${app.formatAmount(app.analyticsService.getAverageExpense())}');
  stdout.writeln('==============================================');
}
