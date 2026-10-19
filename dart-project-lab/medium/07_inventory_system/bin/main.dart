import 'dart:io';
import 'package:inventory_system/inventory_system.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('     07. INVENTORY MANAGEMENT SYSTEM          ');
  stdout.writeln('==============================================');

  final app = InventoryApp.create();

  final laptop = app.addProduct('MacBook Pro M3', 'LAPTOPS', 25000000,
      initialStock: 15, minStock: 5);
  final mouse = app.addProduct('Magic Mouse', 'ACCESSORIES', 1200000,
      initialStock: 4, minStock: 8);

  stdout.writeln('Registered Products:');
  for (final p in app.productRepo.getAll()) {
    stdout.writeln(
        '  [${p.sku}] ${p.name} - Qty: ${p.quantity} @ Rp ${p.unitPrice}');
  }

  stdout.writeln('\nSimulating Stock Transactions...');
  app.inventoryService.stockIn(laptop.id, 5, note: 'Shipment #1029');
  app.inventoryService.stockOut(mouse.id, 2, note: 'Sales Order #4421');

  final summary = app.getSummary();
  stdout.writeln('\nInventory Summary:');
  stdout.writeln('  Total Products : ${summary.totalProducts}');
  stdout.writeln('  Total Units    : ${summary.totalUnits}');
  stdout.writeln('  Total Valuation: Rp ${summary.totalValuation}');
  stdout.writeln('  Low Stock Items: ${summary.lowStockCount}');

  stdout.writeln('\nLow Stock Alerts:');
  for (final alert in app.getAlerts()) {
    stdout.writeln(
        '  ALERT: ${alert.productName} (${alert.sku}) has only ${alert.currentQuantity} units left (Min: ${alert.threshold})');
  }

  stdout.writeln('==============================================');
}
