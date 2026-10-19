import 'package:test/test.dart';
import 'package:inventory_system/inventory_system.dart';

void main() {
  group('Inventory Unit Tests', () {
    test('SkuGenerator formats category, name, and sequence correctly', () {
      final sku = SkuGenerator.generate('Electronics', 'Laptop Dell', 1);
      expect(sku, equals('ELE-LAP-0001'));
    });

    test('StockOut throws StockException when insufficient units available',
        () {
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
