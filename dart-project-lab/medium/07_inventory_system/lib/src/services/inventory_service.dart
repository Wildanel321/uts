import '../exceptions/inventory_exception.dart';
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
    auditRepo.log('CREATE_PRODUCT', product.id,
        'Registered product ${product.sku} - ${product.name}');
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
    auditRepo.log('STOCK_IN', productId,
        'Added $quantity units. New total: ${p.quantity}');
  }

  void stockOut(String productId, int quantity, {String note = ''}) {
    ProductValidator.validatePositiveQuantity(quantity);
    final p = productRepo.findById(productId);
    if (p == null) throw InventoryException('Product not found: $productId');

    if (p.quantity < quantity) {
      throw StockException(
          'Insufficient stock for "${p.name}". Available: ${p.quantity}, Requested: $quantity');
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
    auditRepo.log('STOCK_OUT', productId,
        'Deducted $quantity units. Remaining: ${p.quantity}');
  }
}
