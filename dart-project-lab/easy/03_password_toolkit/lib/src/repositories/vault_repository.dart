import '../models/vault_entry.dart';
import '../exceptions/vault_exception.dart';

class VaultRepository {
  final List<VaultEntry> _entries = [];

  void add(VaultEntry entry) {
    if (_entries.any((e) =>
        e.serviceName.toLowerCase() == entry.serviceName.toLowerCase() &&
        e.username == entry.username)) {
      throw VaultException(
          'Entry for service "${entry.serviceName}" with user "${entry.username}" already exists.');
    }
    _entries.add(entry);
  }

  List<VaultEntry> getAll() => List.unmodifiable(_entries);

  VaultEntry? findByService(String serviceName) {
    for (final e in _entries) {
      if (e.serviceName.toLowerCase() == serviceName.toLowerCase()) {
        return e;
      }
    }
    return null;
  }

  bool delete(String id) {
    final count = _entries.length;
    _entries.removeWhere((e) => e.id == id);
    return _entries.length < count;
  }

  void clear() => _entries.clear();
}
