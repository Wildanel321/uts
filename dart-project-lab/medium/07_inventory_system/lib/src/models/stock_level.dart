class StockLevel {
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
