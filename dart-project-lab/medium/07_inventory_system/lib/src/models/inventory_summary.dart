class InventorySummary {
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
  String toString() =>
      'Products: $totalProducts, Units: $totalUnits, Value: Rp $totalValuation, Low Stock: $lowStockCount';
}
