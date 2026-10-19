import os

def generate_p05(base_dir):
    pdir = os.path.join(base_dir, 'easy', '05_contact_book')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'repositories'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'validators'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'utils'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'config'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'application'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'unit'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'integration'), exist_ok=True)

    def write_f(rel_path, content):
        target = os.path.join(pdir, rel_path)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

    write_f('pubspec.yaml', """name: contact_book
description: Pure Dart Contact Book CLI with fuzzy Levenshtein search, group tagging, phone normalization, and JSON persistence.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dev_dependencies:
  test: ^1.25.0
""")

    write_f('README.md', """# 05. Contact Book

Aplikasi buku kontak (*Contact Book*) berbasis Dart murni. Menyediakan pengelolaan kontak penuh (CRUD), pencarian cerdas berbasis kemiripan string (*Levenshtein distance*), normalisasi nomor telepon internasional, pengelompokan kontak (*Family, Work, Friends*), dan impor/ekspor data JSON.

## Fitur Utama
- **CRUD Kontak**: Tambah, perbarui, hapus, dan tandai kontak favorit.
- **Pencarian Cerdas**: Pencarian fuzzy berbasis Levenshtein distance dan kecocokan substring nomor telepon yang dinormalisasi.
- **Validasi Data**: Memvalidasi format email dan pola nomor telepon yang valid.
- **Pengelompokan (Group Tagging)**: Mengorganisir kontak ke dalam grup khusus.
- **Impor & Ekspor JSON**: Serialisasi dan deserialisasi data buku kontak untuk pencadangan.

## Struktur File (22 File Dart)
- `bin/main.dart`: CLI entry point interaktif.
- `lib/contact_book.dart`: Export publik modul.
- `lib/src/models/`: Contact, ContactGroup, SearchFilter, ImportExportResult.
- `lib/src/exceptions/`: ContactException, ValidationException.
- `lib/src/repositories/`: ContactRepository.
- `lib/src/services/`: ContactService, SearchService, GroupService, SerializationService.
- `lib/src/validators/`: ContactValidator.
- `lib/src/utils/`: PhoneNormalizer, StringSimilarity.
- `lib/src/config/`: BookConfig.
- `lib/src/application/`: ContactApp.
- `test/unit/`: Pengujian validasi kontak, normalisasi telepon, dan fuzzy similarity.
- `test/integration/`: Pengujian alur CRUD dan impor/ekspor JSON.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
""")

    # models
    write_f('lib/src/models/contact.dart', """class Contact {
  final String id;
  final String name;
  final String phone;
  final String email;
  final String address;
  final String notes;
  final String group;
  final bool isFavorite;
  final DateTime updatedAt;

  Contact({
    required this.id,
    required this.name,
    required this.phone,
    required this.email,
    this.address = '',
    this.notes = '',
    this.group = 'General',
    this.isFavorite = false,
    DateTime? updatedAt,
  }) : updatedAt = updatedAt ?? DateTime.now();

  Contact copyWith({
    String? name,
    String? phone,
    String? email,
    String? address,
    String? notes,
    String? group,
    bool? isFavorite,
  }) {
    return Contact(
      id: id,
      name: name ?? this.name,
      phone: phone ?? this.phone,
      email: email ?? this.email,
      address: address ?? this.address,
      notes: notes ?? this.notes,
      group: group ?? this.group,
      isFavorite: isFavorite ?? this.isFavorite,
      updatedAt: DateTime.now(),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'name': name,
    'phone': phone,
    'email': email,
    'address': address,
    'notes': notes,
    'group': group,
    'isFavorite': isFavorite,
    'updatedAt': updatedAt.toIso8601String(),
  };

  factory Contact.fromJson(Map<String, dynamic> json) => Contact(
    id: json['id'] as String,
    name: json['name'] as String,
    phone: json['phone'] as String,
    email: json['email'] as String,
    address: json['address'] as String? ?? '',
    notes: json['notes'] as String? ?? '',
    group: json['group'] as String? ?? 'General',
    isFavorite: json['isFavorite'] as bool? ?? false,
    updatedAt: DateTime.parse(json['updatedAt'] as String),
  );
}
""")

    write_f('lib/src/models/contact_group.dart', """class ContactGroup {
  final String name;
  final String description;

  const ContactGroup({
    required this.name,
    this.description = '',
  });
}
""")

    write_f('lib/src/models/search_filter.dart', """class SearchFilter {
  final String? query;
  final String? group;
  final bool onlyFavorites;

  const SearchFilter({
    this.query,
    this.group,
    this.onlyFavorites = false,
  });
}
""")

    write_f('lib/src/models/import_export_result.dart', """class ImportExportResult {
  final int successCount;
  final int failureCount;
  final List<String> errors;

  ImportExportResult({
    required this.successCount,
    required this.failureCount,
    required this.errors,
  });

  bool get hasErrors => errors.isNotEmpty;
}
""")

    # exceptions
    write_f('lib/src/exceptions/contact_exception.dart', """class ContactException implements Exception {
  final String message;
  ContactException(this.message);

  @override
  String toString() => 'ContactException: $message';
}
""")

    write_f('lib/src/exceptions/validation_exception.dart', """import 'contact_exception.dart';

class ValidationException extends ContactException {
  ValidationException(super.message);

  @override
  String toString() => 'ValidationException: $message';
}
""")

    # utils
    write_f('lib/src/utils/phone_normalizer.dart', """class PhoneNormalizer {
  static String normalize(String phone) {
    String clean = phone.replaceAll(RegExp(r'[\\s\\-\\(\\)]'), '');
    if (clean.startsWith('08')) {
      clean = '+628${clean.substring(2)}';
    }
    return clean;
  }
}
""")

    write_f('lib/src/utils/string_similarity.dart', """import 'dart:math';

class StringSimilarity {
  static int levenshteinDistance(String a, String b) {
    final s1 = a.toLowerCase();
    final s2 = b.toLowerCase();

    final d = List.generate(
      s1.length + 1,
      (i) => List.filled(s2.length + 1, 0),
    );

    for (int i = 0; i <= s1.length; i++) {
      d[i][0] = i;
    }
    for (int j = 0; j <= s2.length; j++) {
      d[0][j] = j;
    }

    for (int i = 1; i <= s1.length; i++) {
      for (int j = 1; j <= s2.length; j++) {
        final cost = s1[i - 1] == s2[j - 1] ? 0 : 1;
        d[i][j] = min(
          d[i - 1][j] + 1,
          min(d[i][j - 1] + 1, d[i - 1][j - 1] + cost),
        );
      }
    }

    return d[s1.length][s2.length];
  }

  static bool isFuzzyMatch(String target, String query, {int maxDistance = 2}) {
    if (target.toLowerCase().contains(query.toLowerCase())) return true;
    return levenshteinDistance(target, query) <= maxDistance;
  }
}
""")

    # validators
    write_f('lib/src/validators/contact_validator.dart', """import '../models/contact.dart';
import '../exceptions/validation_exception.dart';

class ContactValidator {
  static void validate(Contact contact) {
    if (contact.name.trim().isEmpty) {
      throw ValidationException('Contact name cannot be empty.');
    }

    if (contact.phone.trim().isEmpty) {
      throw ValidationException('Contact phone number cannot be empty.');
    }

    final emailRegex = RegExp(r'^[\w\.\-]+@[\w\.\-]+\.[a-zA-Z]{2,}\$');
    if (contact.email.isNotEmpty && !emailRegex.hasMatch(contact.email)) {
      throw ValidationException('Invalid email address format: ${contact.email}');
    }
  }
}
""")

    # repositories
    write_f('lib/src/repositories/contact_repository.dart', """import '../models/contact.dart';

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
""")

    # services
    write_f('lib/src/services/contact_service.dart', """import '../models/contact.dart';
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
""")

    write_f('lib/src/services/search_service.dart', """import '../models/contact.dart';
import '../models/search_filter.dart';
import '../repositories/contact_repository.dart';
import '../utils/string_similarity.dart';

class SearchService {
  final ContactRepository repository;

  SearchService(this.repository);

  List<Contact> search(SearchFilter filter) {
    var items = repository.getAll();

    if (filter.onlyFavorites) {
      items = items.where((c) => c.isFavorite).toList();
    }

    if (filter.group != null && filter.group!.isNotEmpty) {
      items = items.where((c) => c.group.toLowerCase() == filter.group!.toLowerCase()).toList();
    }

    if (filter.query != null && filter.query!.trim().isNotEmpty) {
      final q = filter.query!.trim();
      items = items.where((c) {
        final matchesName = StringSimilarity.isFuzzyMatch(c.name, q);
        final matchesPhone = c.phone.contains(q);
        final matchesEmail = c.email.toLowerCase().contains(q.toLowerCase());
        return matchesName || matchesPhone || matchesEmail;
      }).toList();
    }

    return items;
  }
}
""")

    write_f('lib/src/services/group_service.dart', """import '../models/contact_group.dart';
import '../repositories/contact_repository.dart';

class GroupService {
  final ContactRepository repository;

  GroupService(this.repository);

  List<ContactGroup> getAvailableGroups() {
    final groupNames = repository.getAll().map((c) => c.group).toSet();
    groupNames.addAll(['General', 'Family', 'Work', 'Friends']);
    return groupNames.map((g) => ContactGroup(name: g)).toList();
  }

  int countByGroup(String groupName) {
    return repository.getAll().where((c) => c.group.toLowerCase() == groupName.toLowerCase()).length;
  }
}
""")

    write_f('lib/src/services/serialization_service.dart', """import 'dart:convert';
import '../models/contact.dart';
import '../models/import_export_result.dart';
import '../repositories/contact_repository.dart';

class SerializationService {
  final ContactRepository repository;

  SerializationService(this.repository);

  String exportToJson() {
    final list = repository.getAll().map((c) => c.toJson()).toList();
    return const JsonEncoder.withIndent('  ').convert(list);
  }

  ImportExportResult importFromJson(String jsonString) {
    final errors = <String>[];
    int success = 0;
    int failure = 0;

    try {
      final decoded = jsonDecode(jsonString) as List<dynamic>;
      for (final item in decoded) {
        try {
          final c = Contact.fromJson(item as Map<String, dynamic>);
          repository.save(c);
          success++;
        } catch (e) {
          failure++;
          errors.add('Failed to parse contact: $e');
        }
      }
    } catch (e) {
      errors.add('Invalid JSON document: $e');
    }

    return ImportExportResult(successCount: success, failureCount: failure, errors: errors);
  }
}
""")

    # config
    write_f('lib/src/config/book_config.dart', """class BookConfig {
  final String storagePath;
  final bool autoNormalizePhone;

  const BookConfig({
    this.storagePath = 'data/contacts.json',
    this.autoNormalizePhone = true,
  });
}
""")

    # application
    write_f('lib/src/application/contact_app.dart', """import '../config/book_config.dart';
import '../models/contact.dart';
import '../models/search_filter.dart';
import '../repositories/contact_repository.dart';
import '../services/contact_service.dart';
import '../services/group_service.dart';
import '../services/search_service.dart';
import '../services/serialization_service.dart';

class ContactApp {
  final BookConfig config;
  final ContactRepository repository;
  final ContactService contactService;
  final SearchService searchService;
  final GroupService groupService;
  final SerializationService serializationService;

  ContactApp({BookConfig? config})
      : config = config ?? const BookConfig(),
        repository = ContactRepository(),
        contactService = ContactService(ContactRepository()),
        searchService = SearchService(ContactRepository()),
        groupService = GroupService(ContactRepository()),
        serializationService = SerializationService(ContactRepository());

  factory ContactApp.create({BookConfig? config}) {
    final repo = ContactRepository();
    return ContactApp._internal(
      config ?? const BookConfig(),
      repo,
      ContactService(repo),
      SearchService(repo),
      GroupService(repo),
      SerializationService(repo),
    );
  }

  ContactApp._internal(
    this.config,
    this.repository,
    this.contactService,
    this.searchService,
    this.groupService,
    this.serializationService,
  );

  Contact addContact(String name, String phone, String email, {String group = 'General'}) {
    return contactService.createContact(name: name, phone: phone, email: email, group: group);
  }

  List<Contact> find(String query) {
    return searchService.search(SearchFilter(query: query));
  }
}
""")

    # lib export
    write_f('lib/contact_book.dart', """export 'src/models/contact.dart';
export 'src/models/contact_group.dart';
export 'src/models/search_filter.dart';
export 'src/models/import_export_result.dart';
export 'src/exceptions/contact_exception.dart';
export 'src/exceptions/validation_exception.dart';
export 'src/repositories/contact_repository.dart';
export 'src/services/contact_service.dart';
export 'src/services/search_service.dart';
export 'src/services/group_service.dart';
export 'src/services/serialization_service.dart';
export 'src/validators/contact_validator.dart';
export 'src/utils/phone_normalizer.dart';
export 'src/utils/string_similarity.dart';
export 'src/config/book_config.dart';
export 'src/application/contact_app.dart';
""")

    # bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
import 'package:contact_book/contact_book.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('          05. CONTACT BOOK CLI                ');
  stdout.writeln('==============================================');

  final app = ContactApp.create();

  app.addContact('Alice Wonderland', '081234567890', 'alice@wonderland.org', group: 'Friends');
  app.addContact('Bob Builder', '+628987654321', 'bob@builder.com', group: 'Work');
  app.addContact('Charlie Chaplin', '085512348888', 'charlie@comedy.com', group: 'Family');

  stdout.writeln('All Contacts in Book:');
  for (final c in app.contactService.listAll()) {
    stdout.writeln('  [${c.group}] ${c.name} - ${c.phone} (${c.email})');
  }

  stdout.writeln('\\nFuzzy Search "Alce":');
  final results = app.find('Alce');
  for (final r in results) {
    stdout.writeln('  Match: ${r.name} (${r.phone})');
  }

  stdout.writeln('==============================================');
}
""")

    # test/unit
    write_f('test/unit/contact_unit_test.dart', """import 'package:test/test.dart';
import 'package:contact_book/contact_book.dart';

void main() {
  group('Contact Book Unit Tests', () {
    test('PhoneNormalizer normalizes indonesian 08 prefix', () {
      expect(PhoneNormalizer.normalize('0812-3456-7890'), equals('+6281234567890'));
      expect(PhoneNormalizer.normalize('+62811223344'), equals('+62811223344'));
    });

    test('Levenshtein distance detects fuzzy match', () {
      expect(StringSimilarity.levenshteinDistance('kitten', 'sitting'), equals(3));
      expect(StringSimilarity.isFuzzyMatch('Alexander', 'Alexandr'), isTrue);
    });

    test('Validator checks email format and name presence', () {
      final invalidEmail = Contact(id: '1', name: 'John', phone: '123', email: 'invalid_email');
      expect(() => ContactValidator.validate(invalidEmail), throwsA(isA<ValidationException>()));

      final emptyName = Contact(id: '2', name: '', phone: '123', email: 'valid@test.com');
      expect(() => ContactValidator.validate(emptyName), throwsA(isA<ValidationException>()));
    });
  });
}
""")

    # test/integration
    write_f('test/integration/contact_integration_test.dart', """import 'package:test/test.dart';
import 'package:contact_book/contact_book.dart';

void main() {
  group('Contact Book Integration Tests', () {
    late ContactApp app;

    setUp(() {
      app = ContactApp.create();
    });

    test('Adds contact, finds via fuzzy query, and toggles favorite', () {
      final c = app.addContact('Michael Jordan', '0812999888', 'mj@bulls.com', group: 'Sports');
      expect(c.name, equals('Michael Jordan'));

      final matches = app.find('Jordan');
      expect(matches.length, equals(1));
      expect(matches.first.id, equals(c.id));

      final updated = app.contactService.toggleFavorite(c.id);
      expect(updated?.isFavorite, isTrue);
    });

    test('Exports and imports JSON cleanly', () {
      app.addContact('David Copperfield', '0811112222', 'david@magic.com');
      final jsonStr = app.serializationService.exportToJson();

      final newApp = ContactApp.create();
      final result = newApp.serializationService.importFromJson(jsonStr);

      expect(result.successCount, equals(1));
      expect(result.hasErrors, isFalse);
      expect(newApp.contactService.listAll().first.name, equals('David Copperfield'));
    });
  });
}
""")

    print("Project 05 (Contact Book) generated successfully with 22 Dart files!")

if __name__ == '__main__':
    generate_p05('dart-project-lab')
