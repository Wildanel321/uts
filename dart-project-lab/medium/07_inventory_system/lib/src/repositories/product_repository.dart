import '../models/product.dart';

class ProductRepository {
  final List<Product> _products = [];

  void save(Product product) {
    final idx = _products.indexWhere((p) => p.id == product.id);
    if (idx >= 0) {
      _products[idx] = product;
    } else {
      _products.add(product);
    }
  }

  Product? findById(String id) {
    for (final p in _products) {
      if (p.id == id) return p;
    }
    return null;
  }

  Product? findBySku(String sku) {
    for (final p in _products) {
      if (p.sku.toUpperCase() == sku.toUpperCase()) return p;
    }
    return null;
  }

  List<Product> getAll() => List.unmodifiable(_products);

  bool delete(String id) {
    final len = _products.length;
    _products.removeWhere((p) => p.id == id);
    return _products.length < len;
  }

  void clear() => _products.clear();
}
