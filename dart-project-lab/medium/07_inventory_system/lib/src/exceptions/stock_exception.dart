import 'inventory_exception.dart';

class StockException extends InventoryException {
  StockException(super.message);

  @override
  String toString() => 'StockException: $message';
}
