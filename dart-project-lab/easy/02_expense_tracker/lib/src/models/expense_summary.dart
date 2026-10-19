class ExpenseSummary {
  final double totalIncome;
  final double totalExpense;
  final double netBalance;
  final Map<String, double> categoryBreakdown;

  ExpenseSummary({
    required this.totalIncome,
    required this.totalExpense,
    required this.netBalance,
    required this.categoryBreakdown,
  });

  @override
  String toString() =>
      'Summary: Income=$totalIncome, Expense=$totalExpense, Net=$netBalance';
}
