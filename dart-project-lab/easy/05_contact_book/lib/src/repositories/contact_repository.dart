import '../models/contact.dart';

class ContactRepository {
  final List<Contact> _contacts = [];

  void save(Contact contact) {
    final idx = _contacts.indexWhere((c) => c.id == contact.id);
    if (idx >= 0) {
      _contacts[idx] = contact;
    } else {
      _contacts.add(contact);
    }
  }

  bool delete(String id) {
    final count = _contacts.length;
    _contacts.removeWhere((c) => c.id == id);
    return _contacts.length < count;
  }

  Contact? findById(String id) {
    for (final c in _contacts) {
      if (c.id == id) return c;
    }
    return null;
  }

  List<Contact> getAll() => List.unmodifiable(_contacts);

  void clear() => _contacts.clear();
}
