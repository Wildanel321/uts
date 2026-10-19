import 'package:test/test.dart';
import 'package:inventory_system/inventory_system.dart';

void main() {
  group('Inventory System Integration Tests', () {
    late InventoryApp app;

    setUp(() {
      app = InventoryApp.create();
    });

    test(
        'Full lifecycle: stock in, stock out, alert trigger, and audit logging',
        () {
      final p = app.addProduct('Smartwatch', 'WEARABLE', 3000000,
          initialStock: 10, minStock: 5);

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
