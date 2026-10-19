import 'package:test/test.dart';
import 'package:contact_book/contact_book.dart';

void main() {
  group('Contact Book Integration Tests', () {
    late ContactApp app;

    setUp(() {
      app = ContactApp.create();
    });

    test('Adds contact, finds via fuzzy query, and toggles favorite', () {
      final c = app.addContact('Michael Jordan', '0812999888', 'mj@bulls.com',
          group: 'Sports');
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
      expect(newApp.contactService.listAll().first.name,
          equals('David Copperfield'));
    });
  });
}
