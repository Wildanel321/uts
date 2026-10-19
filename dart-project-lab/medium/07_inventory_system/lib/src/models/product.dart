class Product {
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
