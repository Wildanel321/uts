import '../models/stock_level.dart';
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
