import 'package:test/test.dart';
import 'package:contact_book/contact_book.dart';

void main() {
  group('Contact Book Unit Tests', () {
    test('PhoneNormalizer normalizes indonesian 08 prefix', () {
      expect(PhoneNormalizer.normalize('0812-3456-7890'),
          equals('+6281234567890'));
      expect(PhoneNormalizer.normalize('+62811223344'), equals('+62811223344'));
    });

    test('Levenshtein distance detects fuzzy match', () {
      expect(
          StringSimilarity.levenshteinDistance('kitten', 'sitting'), equals(3));
      expect(StringSimilarity.isFuzzyMatch('Alexander', 'Alexandr'), isTrue);
    });

    test('Validator checks email format and name presence', () {
      final invalidEmail =
          Contact(id: '1', name: 'John', phone: '123', email: 'invalid_email');
      expect(() => ContactValidator.validate(invalidEmail),
          throwsA(isA<ValidationException>()));

      final emptyName =
          Contact(id: '2', name: '', phone: '123', email: 'valid@test.com');
      expect(() => ContactValidator.validate(emptyName),
          throwsA(isA<ValidationException>()));
    });
  });
}
