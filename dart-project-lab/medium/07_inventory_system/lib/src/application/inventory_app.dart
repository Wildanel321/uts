import '../config/inventory_config.dart';
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
        inventoryService = InventoryService(
            ProductRepository(), TransactionRepository(), AuditRepository()),
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

  Product addProduct(String name, String category, double price,
      {int initialStock = 0, int minStock = 10}) {
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
