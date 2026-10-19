import '../models/inventory_summary.dart';
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
