import '../exceptions/inventory_exception.dart';
import '../models/product.dart';

class ProductValidator {
  static void validate(Product product) {
    if (product.name.trim().isEmpty) {
      throw InventoryException('Product name cannot be empty.');
    }
    if (product.sku.trim().isEmpty) {
      throw InventoryException('Product SKU cannot be empty.');
    }
    if (product.unitPrice < 0) {
      throw InventoryException('Unit price cannot be negative.');
    }
    if (product.quantity < 0) {
      throw InventoryException('Stock quantity cannot be negative.');
    }
  }

  static void validatePositiveQuantity(int qty) {
    if (qty <= 0) {
      throw InventoryException(
          'Transaction quantity must be strictly positive.');
    }
  }
}
