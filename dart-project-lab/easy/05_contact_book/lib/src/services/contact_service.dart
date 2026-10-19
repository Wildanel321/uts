import '../models/contact.dart';
import '../repositories/contact_repository.dart';
import '../utils/phone_normalizer.dart';
import '../validators/contact_validator.dart';

class ContactService {
  final ContactRepository repository;
  static int _idCounter = 0;

  ContactService(this.repository);

  Contact createContact({
    required String name,
    required String phone,
    required String email,
    String address = '',
    String notes = '',
    String group = 'General',
  }) {
    final normalizedPhone = PhoneNormalizer.normalize(phone);
    final contact = Contact(
      id: 'cnt_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}',
      name: name.trim(),
      phone: normalizedPhone,
      email: email.trim(),
      address: address,
      notes: notes,
      group: group,
    );

    ContactValidator.validate(contact);
    repository.save(contact);
    return contact;
  }

  Contact? updateContact(Contact contact) {
    ContactValidator.validate(contact);
    if (repository.findById(contact.id) != null) {
      repository.save(contact);
      return contact;
    }
    return null;
  }

  bool deleteContact(String id) => repository.delete(id);

  Contact? toggleFavorite(String id) {
    final c = repository.findById(id);
    if (c == null) return null;
    final updated = c.copyWith(isFavorite: !c.isFavorite);
    repository.save(updated);
    return updated;
  }

  List<Contact> listAll() => repository.getAll();
}
