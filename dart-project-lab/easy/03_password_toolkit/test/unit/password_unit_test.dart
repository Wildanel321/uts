import 'package:test/test.dart';
import 'package:password_toolkit/password_toolkit.dart';

void main() {
  group('Password Generator & Policy Tests', () {
    final generator = PasswordGenerator();

    test('Generates requested length and respect character sets', () {
      const policy = PasswordPolicy(
        minLength: 14,
        requireUppercase: true,
        requireLowercase: true,
        requireDigits: true,
        requireSymbols: true,
      );
      final pwd = generator.generate(policy);
      expect(pwd.length, equals(14));
      expect(RegExp(r'[A-Z]').hasMatch(pwd), isTrue);
      expect(RegExp(r'[a-z]').hasMatch(pwd), isTrue);
      expect(RegExp(r'[0-9]').hasMatch(pwd), isTrue);
      expect(RegExp(r'[^a-zA-Z0-9]').hasMatch(pwd), isTrue);
    });

    test('Throws exception on invalid policy length', () {
      expect(() => generator.generate(const PasswordPolicy(minLength: 2)),
          throwsA(isA<ToolkitException>()));
    });
  });

  group('Strength & Pattern Detector Tests', () {
    test('Flags sequential characters as weak', () {
      final res = StrengthChecker.check('qwerty123456');
      expect(res.score, lessThan(50));
      expect(res.warnings,
          contains('Contains predictable sequences or common words.'));
    });

    test('Rates complex diverse password as strong', () {
      final res = StrengthChecker.check('K9#mQ2!vL7&wXp0@');
      expect(res.score, greaterThanOrEqualTo(70));
      expect(res.isStrong, isTrue);
    });
  });
}
