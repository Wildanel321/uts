import '../models/inventory_transaction.dart';

class TransactionRepository {
  final List<InventoryTransaction> _transactions = [];

  void save(InventoryTransaction tx) => _transactions.add(tx);

  List<InventoryTransaction> getAll() => List.unmodifiable(_transactions);

  List<InventoryTransaction> getByProduct(String productId) {
    return _transactions.where((t) => t.productId == productId).toList();
  }

  void clear() => _transactions.clear();
}
