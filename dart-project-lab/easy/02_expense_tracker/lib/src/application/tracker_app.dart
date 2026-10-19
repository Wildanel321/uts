import '../config/tracker_config.dart';
import '../models/transaction.dart';
import '../models/transaction_type.dart';
import '../repositories/budget_repository.dart';
import '../repositories/transaction_repository.dart';
import '../services/analytics_service.dart';
import '../services/budget_service.dart';
import '../services/expense_service.dart';
import '../services/report_service.dart';
import '../utils/currency_formatter.dart';

class TrackerApp {
  final TrackerConfig config;
  final TransactionRepository transactionRepo;
  final BudgetRepository budgetRepo;
  final ExpenseService expenseService;
  final BudgetService budgetService;
  final ReportService reportService;
  final AnalyticsService analyticsService;

  TrackerApp({TrackerConfig? config})
      : config = config ?? const TrackerConfig(),
        transactionRepo = TransactionRepository(),
        budgetRepo = BudgetRepository(),
        expenseService = ExpenseService(TransactionRepository()),
        budgetService =
            BudgetService(BudgetRepository(), TransactionRepository()),
        reportService = ReportService(TransactionRepository()),
        analyticsService = AnalyticsService(TransactionRepository());

  factory TrackerApp.create({TrackerConfig? config}) {
    final txRepo = TransactionRepository();
    final bgRepo = BudgetRepository();
    return TrackerApp._internal(
      config ?? const TrackerConfig(),
      txRepo,
      bgRepo,
      ExpenseService(txRepo),
      BudgetService(bgRepo, txRepo),
      ReportService(txRepo),
      AnalyticsService(txRepo),
    );
  }

  TrackerApp._internal(
    this.config,
    this.transactionRepo,
    this.budgetRepo,
    this.expenseService,
    this.budgetService,
    this.reportService,
    this.analyticsService,
  );

  Transaction addIncome(String title, double amount, String categoryId) {
    return expenseService.addTransaction(
      title: title,
      amount: amount,
      type: TransactionType.income,
      categoryId: categoryId,
    );
  }

  Transaction addExpense(String title, double amount, String categoryId) {
    return expenseService.addTransaction(
      title: title,
      amount: amount,
      type: TransactionType.expense,
      categoryId: categoryId,
    );
  }

  String formatAmount(double amount) =>
      CurrencyFormatter.format(amount, symbol: config.currencySymbol);
}
