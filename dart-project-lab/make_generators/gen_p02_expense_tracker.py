import os

def generate_p02(base_dir):
    pdir = os.path.join(base_dir, 'easy', '02_expense_tracker')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'repositories'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'parsers'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'validators'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'utils'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'config'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'application'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'unit'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'integration'), exist_ok=True)

    def write_f(rel_path, content):
        target = os.path.join(pdir, rel_path)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

    write_f('pubspec.yaml', """name: expense_tracker
description: Modular personal finance, expense and budget tracker in pure Dart.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dev_dependencies:
  test: ^1.25.0
""")

    write_f('README.md', """# 02. Expense Tracker

Aplikasi pelacak keuangan dan anggaran pribadi (*Expense & Budget Tracker*) berbasis Dart murni. Menyediakan pencatatan transaksi masuk dan keluar, pengelompokan kategori, batas anggaran bulanan, analitik statistik, serta impor/ekspor data CSV dan JSON.

## Fitur Utama
- **Pencatatan Transaksi**: Pemasukan (*Income*) dan Pengeluaran (*Expense*) dengan metadata lengkap.
- **Kategori Fleksibel**: Makanan, Transportasi, Gaji, Belanja, Tagihan, dan kategori kustom.
- **Anggaran Bulanan**: Peringatan jika pengeluaran melebihi batas anggaran yang ditentukan.
- **Laporan & Statistik**: Laporan harian, rekapitulasi bulanan, rasio persentase per kategori, dan transaksi tertinggi.
- **Serialisasi Data**: Impor dan ekspor data dalam format JSON dan CSV.

## Struktur File (24 File Dart)
- `bin/main.dart`: Entry point CLI.
- `lib/expense_tracker.dart`: Export publik modul.
- `lib/src/models/`: Transaction, TransactionType, Category, Budget, ExpenseSummary.
- `lib/src/exceptions/`: ExpenseException, ValidationException.
- `lib/src/repositories/`: TransactionRepository, BudgetRepository.
- `lib/src/services/`: ExpenseService, BudgetService, ReportService, AnalyticsService.
- `lib/src/parsers/`: CsvParser, JsonParser.
- `lib/src/validators/`: TransactionValidator.
- `lib/src/utils/`: CurrencyFormatter, DateHelper.
- `lib/src/config/`: TrackerConfig.
- `lib/src/application/`: TrackerApp.
- `test/unit/`: Pengujian transaksi, kalkulasi anggaran, dan analitik.
- `test/integration/`: Pengujian alur transaksi dan ekspor data.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
""")

    # models
    write_f('lib/src/models/transaction_type.dart', """enum TransactionType {
  income,
  expense,
}
""")

    write_f('lib/src/models/category.dart', """import 'transaction_type.dart';

class Category {
  final String id;
  final String name;
  final TransactionType type;

  const Category({
    required this.id,
    required this.name,
    required this.type,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'name': name,
    'type': type.name,
  };

  factory Category.fromJson(Map<String, dynamic> json) => Category(
    id: json['id'] as String,
    name: json['name'] as String,
    type: TransactionType.values.byName(json['type'] as String),
  );

  @override
  String toString() => '$name (${type.name})';
}
""")

    write_f('lib/src/models/transaction.dart', """import 'transaction_type.dart';

class Transaction {
  final String id;
  final String title;
  final double amount;
  final TransactionType type;
  final String categoryId;
  final DateTime date;
  final String note;

  Transaction({
    required this.id,
    required this.title,
    required this.amount,
    required this.type,
    required this.categoryId,
    DateTime? date,
    this.note = '',
  }) : date = date ?? DateTime.now();

  Map<String, dynamic> toJson() => {
    'id': id,
    'title': title,
    'amount': amount,
    'type': type.name,
    'categoryId': categoryId,
    'date': date.toIso8601String(),
    'note': note,
  };

  factory Transaction.fromJson(Map<String, dynamic> json) => Transaction(
    id: json['id'] as String,
    title: json['title'] as String,
    amount: (json['amount'] as num).toDouble(),
    type: TransactionType.values.byName(json['type'] as String),
    categoryId: json['categoryId'] as String,
    date: DateTime.parse(json['date'] as String),
    note: json['note'] as String? ?? '',
  );
}
""")

    write_f('lib/src/models/budget.dart', """class Budget {
  final int month;
  final int year;
  final double limitAmount;

  Budget({
    required this.month,
    required this.year,
    required this.limitAmount,
  });

  Map<String, dynamic> toJson() => {
    'month': month,
    'year': year,
    'limitAmount': limitAmount,
  };

  factory Budget.fromJson(Map<String, dynamic> json) => Budget(
    month: json['month'] as int,
    year: json['year'] as int,
    limitAmount: (json['limitAmount'] as num).toDouble(),
  );
}
""")

    write_f('lib/src/models/expense_summary.dart', """class ExpenseSummary {
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
  String toString() => 'Summary: Income=$totalIncome, Expense=$totalExpense, Net=$netBalance';
}
""")

    # exceptions
    write_f('lib/src/exceptions/expense_exception.dart', """class ExpenseException implements Exception {
  final String message;
  ExpenseException(this.message);

  @override
  String toString() => 'ExpenseException: $message';
}
""")

    write_f('lib/src/exceptions/validation_exception.dart', """import 'expense_exception.dart';

class ValidationException extends ExpenseException {
  ValidationException(super.message);

  @override
  String toString() => 'ValidationException: $message';
}
""")

    # utils
    write_f('lib/src/utils/currency_formatter.dart', """class CurrencyFormatter {
  static String format(double amount, {String symbol = 'Rp '}) {
    final isNegative = amount < 0;
    final absAmount = amount.abs();
    final parts = absAmount.toStringAsFixed(2).split('.');
    final integerPart = parts[0];
    final decimalPart = parts[1];

    final buffer = StringBuffer();
    for (int i = 0; i < integerPart.length; i++) {
      if (i > 0 && (integerPart.length - i) % 3 == 0) {
        buffer.write('.');
      }
      buffer.write(integerPart[i]);
    }

    final formatted = '$symbol${buffer.toString()},${decimalPart == '00' ? '-' : decimalPart}';
    return isNegative ? '-$formatted' : formatted;
  }
}
""")

    write_f('lib/src/utils/date_helper.dart', """class DateHelper {
  static String formatDate(DateTime dt) {
    final y = dt.year.toString().padLeft(4, '0');
    final m = dt.month.toString().padLeft(2, '0');
    final d = dt.day.toString().padLeft(2, '0');
    return '$y-$m-$d';
  }

  static bool isSameMonth(DateTime a, int year, int month) {
    return a.year == year && a.month == month;
  }
}
""")

    # validators
    write_f('lib/src/validators/transaction_validator.dart', """import '../models/transaction.dart';
import '../exceptions/validation_exception.dart';

class TransactionValidator {
  static void validate(Transaction tx) {
    if (tx.title.trim().isEmpty) {
      throw ValidationException('Transaction title cannot be empty.');
    }
    if (tx.amount <= 0) {
      throw ValidationException('Transaction amount must be strictly positive.');
    }
    if (tx.categoryId.trim().isEmpty) {
      throw ValidationException('Category ID must be provided.');
    }
  }
}
""")

    # repositories
    write_f('lib/src/repositories/transaction_repository.dart', """import '../models/transaction.dart';

class TransactionRepository {
  final List<Transaction> _items = [];

  void save(Transaction tx) {
    final idx = _items.indexWhere((t) => t.id == tx.id);
    if (idx >= 0) {
      _items[idx] = tx;
    } else {
      _items.add(tx);
    }
  }

  bool delete(String id) {
    final initialLen = _items.length;
    _items.removeWhere((t) => t.id == id);
    return _items.length < initialLen;
  }

  Transaction? findById(String id) {
    for (final t in _items) {
      if (t.id == id) return t;
    }
    return null;
  }

  List<Transaction> getAll() => List.unmodifiable(_items);

  void clear() => _items.clear();
}
""")

    write_f('lib/src/repositories/budget_repository.dart', """import '../models/budget.dart';

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
""")

    # parsers
    write_f('lib/src/parsers/csv_parser.dart', """import '../models/transaction.dart';
import '../models/transaction_type.dart';

class CsvParser {
  static String toCsv(List<Transaction> transactions) {
    final buffer = StringBuffer('id,title,amount,type,categoryId,date,note\\n');
    for (final t in transactions) {
      final safeTitle = t.title.replaceAll(',', ' ');
      final safeNote = t.note.replaceAll(',', ' ');
      buffer.writeln('${t.id},$safeTitle,${t.amount},${t.type.name},${t.categoryId},${t.date.toIso8601String()},$safeNote');
    }
    return buffer.toString();
  }

  static List<Transaction> fromCsv(String csv) {
    final lines = csv.split('\\n').map((l) => l.trim()).where((l) => l.isNotEmpty).toList();
    if (lines.isEmpty) return [];

    final list = <Transaction>[];
    for (int i = 1; i < lines.length; i++) {
      final cols = lines[i].split(',');
      if (cols.length >= 6) {
        list.add(Transaction(
          id: cols[0],
          title: cols[1],
          amount: double.tryParse(cols[2]) ?? 0.0,
          type: TransactionType.values.byName(cols[3]),
          categoryId: cols[4],
          date: DateTime.parse(cols[5]),
          note: cols.length > 6 ? cols[6] : '',
        ));
      }
    }
    return list;
  }
}
""")

    write_f('lib/src/parsers/json_parser.dart', """import 'dart:convert';
import '../models/transaction.dart';

class JsonParser {
  static String toJsonString(List<Transaction> txs) {
    final list = txs.map((t) => t.toJson()).toList();
    return const JsonEncoder.withIndent('  ').convert(list);
  }

  static List<Transaction> fromJsonString(String jsonStr) {
    final decoded = jsonDecode(jsonStr) as List<dynamic>;
    return decoded.map((item) => Transaction.fromJson(item as Map<String, dynamic>)).toList();
  }
}
""")

    # services
    write_f('lib/src/services/expense_service.dart', """import '../models/transaction.dart';
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
""")

    write_f('lib/src/services/budget_service.dart', """import '../models/budget.dart';
import '../models/transaction_type.dart';
import '../repositories/budget_repository.dart';
import '../repositories/transaction_repository.dart';
import '../utils/date_helper.dart';

class BudgetService {
  final BudgetRepository budgetRepo;
  final TransactionRepository transactionRepo;

  BudgetService(this.budgetRepo, this.transactionRepo);

  void setBudget(int year, int month, double limitAmount) {
    budgetRepo.setBudget(Budget(year: year, month: month, limitAmount: limitAmount));
  }

  Budget? getBudget(int year, int month) => budgetRepo.getBudget(year, month);

  double getMonthlyExpense(int year, int month) {
    return transactionRepo
        .getAll()
        .where((t) => t.type == TransactionType.expense && DateHelper.isSameMonth(t.date, year, month))
        .fold(0.0, (sum, t) => sum + t.amount);
  }

  bool isBudgetExceeded(int year, int month) {
    final budget = getBudget(year, month);
    if (budget == null) return false;
    return getMonthlyExpense(year, month) > budget.limitAmount;
  }
}
""")

    write_f('lib/src/services/report_service.dart', """import '../models/expense_summary.dart';
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
""")

    write_f('lib/src/services/analytics_service.dart', """import '../models/transaction.dart';
import '../models/transaction_type.dart';
import '../repositories/transaction_repository.dart';

class AnalyticsService {
  final TransactionRepository repository;

  AnalyticsService(this.repository);

  Transaction? getHighestExpense() {
    final expenses = repository.getAll().where((t) => t.type == TransactionType.expense).toList();
    if (expenses.isEmpty) return null;
    expenses.sort((a, b) => b.amount.compareTo(a.amount));
    return expenses.first;
  }

  double getAverageExpense() {
    final expenses = repository.getAll().where((t) => t.type == TransactionType.expense).toList();
    if (expenses.isEmpty) return 0.0;
    final total = expenses.fold(0.0, (acc, t) => acc + t.amount);
    return total / expenses.length;
  }

  Map<String, double> getExpensePercentages() {
    final expenses = repository.getAll().where((t) => t.type == TransactionType.expense).toList();
    final total = expenses.fold(0.0, (acc, t) => acc + t.amount);
    if (total == 0) return {};

    final categoryTotals = <String, double>{};
    for (final e in expenses) {
      categoryTotals[e.categoryId] = (categoryTotals[e.categoryId] ?? 0.0) + e.amount;
    }

    return categoryTotals.map((cat, amt) => MapEntry(cat, (amt / total) * 100));
  }
}
""")

    # config
    write_f('lib/src/config/tracker_config.dart', """class TrackerConfig {
  final String currencySymbol;
  final String defaultStoragePath;

  const TrackerConfig({
    this.currencySymbol = 'Rp ',
    this.defaultStoragePath = 'data/expenses.json',
  });
}
""")

    # application
    write_f('lib/src/application/tracker_app.dart', """import '../config/tracker_config.dart';
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
        budgetService = BudgetService(BudgetRepository(), TransactionRepository()),
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

  String formatAmount(double amount) => CurrencyFormatter.format(amount, symbol: config.currencySymbol);
}
""")

    # library export
    write_f('lib/expense_tracker.dart', """export 'src/models/transaction_type.dart';
export 'src/models/category.dart';
export 'src/models/transaction.dart';
export 'src/models/budget.dart';
export 'src/models/expense_summary.dart';
export 'src/exceptions/expense_exception.dart';
export 'src/exceptions/validation_exception.dart';
export 'src/repositories/transaction_repository.dart';
export 'src/repositories/budget_repository.dart';
export 'src/services/expense_service.dart';
export 'src/services/budget_service.dart';
export 'src/services/report_service.dart';
export 'src/services/analytics_service.dart';
export 'src/parsers/csv_parser.dart';
export 'src/parsers/json_parser.dart';
export 'src/validators/transaction_validator.dart';
export 'src/utils/currency_formatter.dart';
export 'src/utils/date_helper.dart';
export 'src/config/tracker_config.dart';
export 'src/application/tracker_app.dart';
""")

    # bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
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
  stdout.writeln('  Exceeded?     : ${app.budgetService.isBudgetExceeded(now.year, now.month) ? "YES" : "NO"}');
  stdout.writeln('----------------------------------------------');
  stdout.writeln('Highest Expense : ${app.analyticsService.getHighestExpense()?.title}');
  stdout.writeln('Average Expense : ${app.formatAmount(app.analyticsService.getAverageExpense())}');
  stdout.writeln('==============================================');
}
""")

    # test/unit
    write_f('test/unit/expense_unit_test.dart', """import 'package:test/test.dart';
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
""")

    # test/integration
    write_f('test/integration/tracker_integration_test.dart', """import 'package:test/test.dart';
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

      final summary = app.reportService.generateMonthlySummary(now.year, now.month);
      expect(summary.totalIncome, equals(5000000));
      expect(summary.totalExpense, equals(3500000));
      expect(summary.netBalance, equals(1500000));

      final percentages = app.analyticsService.getExpensePercentages();
      expect(percentages['gadget'], closeTo(85.71, 0.1));
    });
  });
}
""")

    print("Project 02 (Expense Tracker) generated successfully with 24 Dart files!")

if __name__ == '__main__':
    generate_p02('dart-project-lab')
