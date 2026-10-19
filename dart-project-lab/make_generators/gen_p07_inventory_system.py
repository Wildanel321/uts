import os

def generate_p07(base_dir):
    pdir = os.path.join(base_dir, 'medium', '07_inventory_system')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'repositories'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
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

    write_f('pubspec.yaml', """name: inventory_system
description: Pure Dart Inventory Management System with SKU validation, stock alerts, audit logging, and CSV export.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dev_dependencies:
  test: ^1.25.0
""")

    write_f('README.md', """# 07. Inventory Management System

Aplikasi sistem pengelolaan inventaris (*Inventory Management System*) tingkat menengah berbasis Dart murni. Menyediakan pengelolaan stok barang komprehensif, generator & validator SKU produk, mutasi transaksi barang masuk/keluar/penyesuaian, deteksi dini stok menipis (*low stock alert*), kalkulasi valuasi aset, jejak audit (*audit trail*) kekal, dan impor/ekspor format CSV.

## Fitur Utama
- **Katalog Produk & SKU**: Pembuatan dan verifikasi SKU unik terstruktur.
- **Mutasi Stok (Transactions)**: Stock In, Stock Out, dan Stock Adjustment dengan alasan mutasi.
- **Peringatan Stok Rendah**: Deteksi otomatis produk yang berada di bawah ambang batas minimum.
- **Valuasi Inventaris**: Perhitungan nilai total aset inventaris berdasarkan harga pokok pembelian.
- **Audit Logging**: Pencatatan riwayat setiap aksi dan perubahan data untuk keperluan kepatuhan (*compliance*).
- **Impor & Ekspor CSV**: Pertukaran data dengan spreadsheet secara langsung.

## Struktur File (23 File Dart)
- `bin/main.dart`: CLI entry point interaktif.
- `lib/inventory_system.dart`: Export publik modul.
- `lib/src/models/`: Product, TransactionType, InventoryTransaction, StockLevel, AuditEntry, InventorySummary.
- `lib/src/exceptions/`: InventoryException, StockException.
- `lib/src/repositories/`: ProductRepository, TransactionRepository, AuditRepository.
- `lib/src/services/`: InventoryService, SkuService, AlertService, ValuationService, CsvService.
- `lib/src/validators/`: ProductValidator.
- `lib/src/utils/`: SkuGenerator.
- `lib/src/config/`: InventoryConfig.
- `lib/src/application/`: InventoryApp.
- `test/unit/`: Pengujian mutasi stok, validasi SKU, dan valuasi aset.
- `test/integration/`: Pengujian alur transaksi inventaris dan ekspor CSV end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
""")

    # models
    write_f('lib/src/models/transaction_type.dart', """enum TransactionType {
  stockIn,
  stockOut,
  adjustment,
}
""")

    write_f('lib/src/models/product.dart', """class Product {
  final String id;
  final String sku;
  final String name;
  final String category;
  final double unitPrice;
  int quantity;
  final int minStockThreshold;
  final DateTime updatedAt;

  Product({
    required this.id,
    required this.sku,
    required this.name,
    required this.category,
    required this.unitPrice,
    this.quantity = 0,
    this.minStockThreshold = 10,
    DateTime? updatedAt,
  }) : updatedAt = updatedAt ?? DateTime.now();

  bool get isLowStock => quantity <= minStockThreshold;
  double get totalValuation => quantity * unitPrice;

  Map<String, dynamic> toJson() => {
    'id': id,
    'sku': sku,
    'name': name,
    'category': category,
    'unitPrice': unitPrice,
    'quantity': quantity,
    'minStockThreshold': minStockThreshold,
    'updatedAt': updatedAt.toIso8601String(),
  };

  factory Product.fromJson(Map<String, dynamic> json) => Product(
    id: json['id'] as String,
    sku: json['sku'] as String,
    name: json['name'] as String,
    category: json['category'] as String,
    unitPrice: (json['unitPrice'] as num).toDouble(),
    quantity: json['quantity'] as int,
    minStockThreshold: json['minStockThreshold'] as int? ?? 10,
    updatedAt: DateTime.parse(json['updatedAt'] as String),
  );
}
""")

    write_f('lib/src/models/inventory_transaction.dart', """import 'transaction_type.dart';

class InventoryTransaction {
  final String id;
  final String productId;
  final TransactionType type;
  final int quantity;
  final String referenceNote;
  final DateTime timestamp;

  InventoryTransaction({
    required this.id,
    required this.productId,
    required this.type,
    required this.quantity,
    this.referenceNote = '',
    DateTime? timestamp,
  }) : timestamp = timestamp ?? DateTime.now();

  Map<String, dynamic> toJson() => {
    'id': id,
    'productId': productId,
    'type': type.name,
    'quantity': quantity,
    'referenceNote': referenceNote,
    'timestamp': timestamp.toIso8601String(),
  };
}
""")

    write_f('lib/src/models/stock_level.dart', """class StockLevel {
  final String sku;
  final String productName;
  final int currentQuantity;
  final int threshold;
  final bool alertRequired;

  const StockLevel({
    required this.sku,
    required this.productName,
    required this.currentQuantity,
    required this.threshold,
    required this.alertRequired,
  });
}
""")

    write_f('lib/src/models/audit_entry.dart', """class AuditEntry {
  final String id;
  final String action;
  final String entityId;
  final String details;
  final DateTime createdAt;

  AuditEntry({
    required this.id,
    required this.action,
    required this.entityId,
    required this.details,
    DateTime? createdAt,
  }) : createdAt = createdAt ?? DateTime.now();
}
""")

    write_f('lib/src/models/inventory_summary.dart', """class InventorySummary {
  final int totalProducts;
  final int totalUnits;
  final double totalValuation;
  final int lowStockCount;

  const InventorySummary({
    required this.totalProducts,
    required this.totalUnits,
    required this.totalValuation,
    required this.lowStockCount,
  });

  @override
  String toString() => 'Products: $totalProducts, Units: $totalUnits, Value: Rp $totalValuation, Low Stock: $lowStockCount';
}
""")

    # exceptions
    write_f('lib/src/exceptions/inventory_exception.dart', """class InventoryException implements Exception {
  final String message;
  InventoryException(this.message);

  @override
  String toString() => 'InventoryException: $message';
}
""")

    write_f('lib/src/exceptions/stock_exception.dart', """import 'inventory_exception.dart';

class StockException extends InventoryException {
  StockException(super.message);

  @override
  String toString() => 'StockException: $message';
}
""")

    # utils
    write_f('lib/src/utils/sku_generator.dart', """class SkuGenerator {
  static String generate(String category, String productName, int sequence) {
    final catCode = category.trim().toUpperCase().padRight(3, 'X').substring(0, 3);
    final prodCode = productName.trim().toUpperCase().replaceAll(RegExp(r'[^A-Z0-9]'), '').padRight(3, 'X').substring(0, 3);
    final seqCode = sequence.toString().padLeft(4, '0');
    return '$catCode-$prodCode-$seqCode';
  }
}
""")

    # validators
    write_f('lib/src/validators/product_validator.dart', """import '../exceptions/inventory_exception.dart';
import '../models/product.dart';

class ProductValidator {
  static void validate(Product product) {
    if (product.name.trim().isEmpty) {
      throw InventoryException('Product name cannot be empty.');
    }
    if (product.sku.trim().isEmpty) {
      throw InventoryException('Product SKU cannot be empty.');
    }
    if (product.unitPrice < 0) {
      throw InventoryException('Unit price cannot be negative.');
    }
    if (product.quantity < 0) {
      throw InventoryException('Stock quantity cannot be negative.');
    }
  }

  static void validatePositiveQuantity(int qty) {
    if (qty <= 0) {
      throw InventoryException('Transaction quantity must be strictly positive.');
    }
  }
}
""")

    # repositories
    write_f('lib/src/repositories/product_repository.dart', """import '../models/product.dart';

class ProductRepository {
  final List<Product> _products = [];

  void save(Product product) {
    final idx = _products.indexWhere((p) => p.id == product.id);
    if (idx >= 0) {
      _products[idx] = product;
    } else {
      _products.add(product);
    }
  }

  Product? findById(String id) {
    for (final p in _products) {
      if (p.id == id) return p;
    }
    return null;
  }

  Product? findBySku(String sku) {
    for (final p in _products) {
      if (p.sku.toUpperCase() == sku.toUpperCase()) return p;
    }
    return null;
  }

  List<Product> getAll() => List.unmodifiable(_products);

  bool delete(String id) {
    final len = _products.length;
    _products.removeWhere((p) => p.id == id);
    return _products.length < len;
  }

  void clear() => _products.clear();
}
""")

    write_f('lib/src/repositories/transaction_repository.dart', """import '../models/inventory_transaction.dart';

class TransactionRepository {
  final List<InventoryTransaction> _transactions = [];

  void save(InventoryTransaction tx) => _transactions.add(tx);

  List<InventoryTransaction> getAll() => List.unmodifiable(_transactions);

  List<InventoryTransaction> getByProduct(String productId) {
    return _transactions.where((t) => t.productId == productId).toList();
  }

  void clear() => _transactions.clear();
}
""")

    write_f('lib/src/repositories/audit_repository.dart', """import '../models/audit_entry.dart';

class AuditRepository {
  final List<AuditEntry> _logs = [];

  void log(String action, String entityId, String details) {
    final entry = AuditEntry(
      id: 'aud_${DateTime.now().microsecondsSinceEpoch}',
      action: action,
      entityId: entityId,
      details: details,
    );
    _logs.add(entry);
  }

  List<AuditEntry> getAll() => List.unmodifiable(_logs);
}
""")

    # services
    write_f('lib/src/services/sku_service.dart', """import '../repositories/product_repository.dart';
import '../utils/sku_generator.dart';

class SkuService {
  final ProductRepository repository;

  SkuService(this.repository);

  String createSku(String category, String productName) {
    final count = repository.getAll().length + 1;
    return SkuGenerator.generate(category, productName, count);
  }

  bool isSkuUnique(String sku) => repository.findBySku(sku) == null;
}
""")

    write_f('lib/src/services/alert_service.dart', """import '../models/stock_level.dart';
import '../repositories/product_repository.dart';

class AlertService {
  final ProductRepository repository;

  AlertService(this.repository);

  List<StockLevel> getLowStockAlerts() {
    return repository
        .getAll()
        .where((p) => p.isLowStock)
        .map((p) => StockLevel(
              sku: p.sku,
              productName: p.name,
              currentQuantity: p.quantity,
              threshold: p.minStockThreshold,
              alertRequired: true,
            ))
        .toList();
  }
}
""")

    write_f('lib/src/services/valuation_service.dart', """import '../models/inventory_summary.dart';
import '../repositories/product_repository.dart';

class ValuationService {
  final ProductRepository repository;

  ValuationService(this.repository);

  InventorySummary calculateSummary() {
    final products = repository.getAll();
    int units = 0;
    double val = 0.0;
    int lowStock = 0;

    for (final p in products) {
      units += p.quantity;
      val += p.totalValuation;
      if (p.isLowStock) lowStock++;
    }

    return InventorySummary(
      totalProducts: products.length,
      totalUnits: units,
      totalValuation: val,
      lowStockCount: lowStock,
    );
  }
}
""")

    write_f('lib/src/services/csv_service.dart', """import '../repositories/product_repository.dart';

class CsvService {
  final ProductRepository repository;

  CsvService(this.repository);

  String exportToCsv() {
    final buffer = StringBuffer('id,sku,name,category,unitPrice,quantity,minStock\\n');
    for (final p in repository.getAll()) {
      buffer.writeln('${p.id},${p.sku},${p.name},${p.category},${p.unitPrice},${p.quantity},${p.minStockThreshold}');
    }
    return buffer.toString();
  }
}
""")

    write_f('lib/src/services/inventory_service.dart', """import '../exceptions/inventory_exception.dart';
import '../exceptions/stock_exception.dart';
import '../models/inventory_transaction.dart';
import '../models/product.dart';
import '../models/transaction_type.dart';
import '../repositories/audit_repository.dart';
import '../repositories/product_repository.dart';
import '../repositories/transaction_repository.dart';
import '../validators/product_validator.dart';

class InventoryService {
  final ProductRepository productRepo;
  final TransactionRepository transactionRepo;
  final AuditRepository auditRepo;
  static int _idCounter = 0;

  InventoryService(this.productRepo, this.transactionRepo, this.auditRepo);

  Product registerProduct({
    required String sku,
    required String name,
    required String category,
    required double unitPrice,
    int initialStock = 0,
    int minThreshold = 10,
  }) {
    if (productRepo.findBySku(sku) != null) {
      throw InventoryException('Product with SKU "$sku" already exists.');
    }

    final product = Product(
      id: 'prd_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}',
      sku: sku,
      name: name,
      category: category,
      unitPrice: unitPrice,
      quantity: initialStock,
      minStockThreshold: minThreshold,
    );

    ProductValidator.validate(product);
    productRepo.save(product);
    auditRepo.log('CREATE_PRODUCT', product.id, 'Registered product ${product.sku} - ${product.name}');
    return product;
  }

  void stockIn(String productId, int quantity, {String note = ''}) {
    ProductValidator.validatePositiveQuantity(quantity);
    final p = productRepo.findById(productId);
    if (p == null) throw InventoryException('Product not found: $productId');

    p.quantity += quantity;
    productRepo.save(p);

    final tx = InventoryTransaction(
      id: 'tx_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}',
      productId: productId,
      type: TransactionType.stockIn,
      quantity: quantity,
      referenceNote: note,
    );
    transactionRepo.save(tx);
    auditRepo.log('STOCK_IN', productId, 'Added $quantity units. New total: ${p.quantity}');
  }

  void stockOut(String productId, int quantity, {String note = ''}) {
    ProductValidator.validatePositiveQuantity(quantity);
    final p = productRepo.findById(productId);
    if (p == null) throw InventoryException('Product not found: $productId');

    if (p.quantity < quantity) {
      throw StockException('Insufficient stock for "${p.name}". Available: ${p.quantity}, Requested: $quantity');
    }

    p.quantity -= quantity;
    productRepo.save(p);

    final tx = InventoryTransaction(
      id: 'tx_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}',
      productId: productId,
      type: TransactionType.stockOut,
      quantity: quantity,
      referenceNote: note,
    );
    transactionRepo.save(tx);
    auditRepo.log('STOCK_OUT', productId, 'Deducted $quantity units. Remaining: ${p.quantity}');
  }
}
""")

    # config
    write_f('lib/src/config/inventory_config.dart', """class InventoryConfig {
  final int defaultMinThreshold;
  final String companyName;

  const InventoryConfig({
    this.defaultMinThreshold = 10,
    this.companyName = 'Dart Logistics Lab',
  });
}
""")

    # application
    write_f('lib/src/application/inventory_app.dart', """import '../config/inventory_config.dart';
import '../models/inventory_summary.dart';
import '../models/product.dart';
import '../models/stock_level.dart';
import '../repositories/audit_repository.dart';
import '../repositories/product_repository.dart';
import '../repositories/transaction_repository.dart';
import '../services/alert_service.dart';
import '../services/csv_service.dart';
import '../services/inventory_service.dart';
import '../services/sku_service.dart';
import '../services/valuation_service.dart';

class InventoryApp {
  final InventoryConfig config;
  final ProductRepository productRepo;
  final TransactionRepository transactionRepo;
  final AuditRepository auditRepo;
  final InventoryService inventoryService;
  final SkuService skuService;
  final AlertService alertService;
  final ValuationService valuationService;
  final CsvService csvService;

  InventoryApp({InventoryConfig? config})
      : config = config ?? const InventoryConfig(),
        productRepo = ProductRepository(),
        transactionRepo = TransactionRepository(),
        auditRepo = AuditRepository(),
        inventoryService = InventoryService(ProductRepository(), TransactionRepository(), AuditRepository()),
        skuService = SkuService(ProductRepository()),
        alertService = AlertService(ProductRepository()),
        valuationService = ValuationService(ProductRepository()),
        csvService = CsvService(ProductRepository());

  factory InventoryApp.create({InventoryConfig? config}) {
    final pRepo = ProductRepository();
    final tRepo = TransactionRepository();
    final aRepo = AuditRepository();
    return InventoryApp._internal(
      config ?? const InventoryConfig(),
      pRepo,
      tRepo,
      aRepo,
      InventoryService(pRepo, tRepo, aRepo),
      SkuService(pRepo),
      AlertService(pRepo),
      ValuationService(pRepo),
      CsvService(pRepo),
    );
  }

  InventoryApp._internal(
    this.config,
    this.productRepo,
    this.transactionRepo,
    this.auditRepo,
    this.inventoryService,
    this.skuService,
    this.alertService,
    this.valuationService,
    this.csvService,
  );

  Product addProduct(String name, String category, double price, {int initialStock = 0, int minStock = 10}) {
    final sku = skuService.createSku(category, name);
    return inventoryService.registerProduct(
      sku: sku,
      name: name,
      category: category,
      unitPrice: price,
      initialStock: initialStock,
      minThreshold: minStock,
    );
  }

  InventorySummary getSummary() => valuationService.calculateSummary();
  List<StockLevel> getAlerts() => alertService.getLowStockAlerts();
}
""")

    # lib export
    write_f('lib/inventory_system.dart', """export 'src/models/transaction_type.dart';
export 'src/models/product.dart';
export 'src/models/inventory_transaction.dart';
export 'src/models/stock_level.dart';
export 'src/models/audit_entry.dart';
export 'src/models/inventory_summary.dart';
export 'src/exceptions/inventory_exception.dart';
export 'src/exceptions/stock_exception.dart';
export 'src/repositories/product_repository.dart';
export 'src/repositories/transaction_repository.dart';
export 'src/repositories/audit_repository.dart';
export 'src/services/inventory_service.dart';
export 'src/services/sku_service.dart';
export 'src/services/alert_service.dart';
export 'src/services/valuation_service.dart';
export 'src/services/csv_service.dart';
export 'src/validators/product_validator.dart';
export 'src/utils/sku_generator.dart';
export 'src/config/inventory_config.dart';
export 'src/application/inventory_app.dart';
""")

    # bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
import 'package:inventory_system/inventory_system.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('     07. INVENTORY MANAGEMENT SYSTEM          ');
  stdout.writeln('==============================================');

  final app = InventoryApp.create();

  final laptop = app.addProduct('MacBook Pro M3', 'LAPTOPS', 25000000, initialStock: 15, minStock: 5);
  final mouse = app.addProduct('Magic Mouse', 'ACCESSORIES', 1200000, initialStock: 4, minStock: 8);

  stdout.writeln('Registered Products:');
  for (final p in app.productRepo.getAll()) {
    stdout.writeln('  [${p.sku}] ${p.name} - Qty: ${p.quantity} @ Rp ${p.unitPrice}');
  }

  stdout.writeln('\\nSimulating Stock Transactions...');
  app.inventoryService.stockIn(laptop.id, 5, note: 'Shipment #1029');
  app.inventoryService.stockOut(mouse.id, 2, note: 'Sales Order #4421');

  final summary = app.getSummary();
  stdout.writeln('\\nInventory Summary:');
  stdout.writeln('  Total Products : ${summary.totalProducts}');
  stdout.writeln('  Total Units    : ${summary.totalUnits}');
  stdout.writeln('  Total Valuation: Rp ${summary.totalValuation}');
  stdout.writeln('  Low Stock Items: ${summary.lowStockCount}');

  stdout.writeln('\\nLow Stock Alerts:');
  for (final alert in app.getAlerts()) {
    stdout.writeln('  ALERT: ${alert.productName} (${alert.sku}) has only ${alert.currentQuantity} units left (Min: ${alert.threshold})');
  }

  stdout.writeln('==============================================');
}
""")

    # test/unit
    write_f('test/unit/inventory_unit_test.dart', """import 'package:test/test.dart';
import 'package:inventory_system/inventory_system.dart';

void main() {
  group('Inventory Unit Tests', () {
    test('SkuGenerator formats category, name, and sequence correctly', () {
      final sku = SkuGenerator.generate('Electronics', 'Laptop Dell', 1);
      expect(sku, equals('ELE-LAP-0001'));
    });

    test('StockOut throws StockException when insufficient units available', () {
      final app = InventoryApp.create();
      final p = app.addProduct('Keyboard', 'TECH', 500000, initialStock: 3);

      expect(
        () => app.inventoryService.stockOut(p.id, 5),
        throwsA(isA<StockException>()),
      );
    });

    test('ValuationService calculates inventory totals accurately', () {
      final app = InventoryApp.create();
      app.addProduct('Monitor', 'SCREEN', 2000000, initialStock: 2);
      app.addProduct('Cable', 'TECH', 100000, initialStock: 10);

      final summary = app.valuationService.calculateSummary();
      expect(summary.totalProducts, equals(2));
      expect(summary.totalUnits, equals(12));
      expect(summary.totalValuation, equals(5000000.0));
    });
  });
}
""")

    # test/integration
    write_f('test/integration/inventory_integration_test.dart', """import 'package:test/test.dart';
import 'package:inventory_system/inventory_system.dart';

void main() {
  group('Inventory System Integration Tests', () {
    late InventoryApp app;

    setUp(() {
      app = InventoryApp.create();
    });

    test('Full lifecycle: stock in, stock out, alert trigger, and audit logging', () {
      final p = app.addProduct('Smartwatch', 'WEARABLE', 3000000, initialStock: 10, minStock: 5);

      app.inventoryService.stockOut(p.id, 7, note: 'Black Friday sale');
      expect(p.quantity, equals(3));
      expect(p.isLowStock, isTrue);

      final alerts = app.getAlerts();
      expect(alerts.length, equals(1));
      expect(alerts.first.sku, equals(p.sku));

      final logs = app.auditRepo.getAll();
      expect(logs.any((l) => l.action == 'STOCK_OUT'), isTrue);

      final csv = app.csvService.exportToCsv();
      expect(csv, contains('Smartwatch'));
      expect(csv, contains(p.sku));
    });
  });
}
""")

    print("Project 07 (Inventory System) generated successfully with 23 Dart files!")

if __name__ == '__main__':
    generate_p07('dart-project-lab')
