import '../models/transaction.dart';

class TransactionRepository {
  final List<Transaction> _items = [];

  void save(Transaction tx) {
    final idx = _items.indexWhere((t) => t.id == tx.id);
    if (idx >= 0) {
      _items[idx] = tx;
    } else {
      _items.add(tx);
    }
  }

  bool delete(String id) {
    final initialLen = _items.length;
    _items.removeWhere((t) => t.id == id);
    return _items.length < initialLen;
  }

  Transaction? findById(String id) {
    for (final t in _items) {
      if (t.id == id) return t;
    }
    return null;
  }

  List<Transaction> getAll() => List.unmodifiable(_items);

  void clear() => _items.clear();
}
