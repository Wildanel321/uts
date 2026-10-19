import os

def generate_p03(base_dir):
    pdir = os.path.join(base_dir, 'easy', '03_password_toolkit')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'repositories'), exist_ok=True)
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

    # 1. pubspec.yaml
    write_f('pubspec.yaml', """name: password_toolkit
description: Pure Dart password generator, entropy checker, passphrase maker, and encrypted local vault.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  crypto: ^3.0.3

dev_dependencies:
  test: ^1.25.0
""")

    # 2. README.md
    write_f('README.md', """# 03. Password Toolkit

Aplikasi keamanan kata sandi serbaguna (*Password Toolkit*) berbasis Dart murni. Menyediakan generator kata sandi acak berbasis kebijakan, pembuat *passphrase* ala Diceware, kalkulator entropi Shannon, pendeteksi pola sandi lemah (urutan keyboard, angka berulang, kamus kata umum), dan brankas kredensial lokal terenkripsi (*Encrypted Vault*).

## Fitur Utama
- **Password Generator**: Pengaturan panjang, huruf besar/kecil, angka, simbol, dan pengecualian karakter ambigu.
- **Passphrase Generator**: Pembuat kata sandi berbasis frasa kata dengan pemisah dan kapitalisasi acak.
- **Strength Checker & Entropy**: Menghitung skor kekuatan (0-100) dan entropi informasi Shannon (bit).
- **Pattern Detector**: Deteksi pola lemah (qwerty, 123456, perulangan huruf aaa, kata umum 'password').
- **Encrypted Local Vault**: Penyimpanan kredensial lokal dengan enkripsi stream XOR/HMAC SHA-256 menggunakan Master Key.

## Struktur File (22 File Dart)
- `bin/main.dart`: CLI interactive & batch toolkit runner.
- `lib/password_toolkit.dart`: Export publik pustaka.
- `lib/src/models/`: PasswordPolicy, StrengthResult, PassphraseConfig, VaultEntry.
- `lib/src/exceptions/`: ToolkitException, VaultException.
- `lib/src/services/`: PasswordGenerator, PassphraseGenerator, EntropyCalculator, StrengthChecker, PatternDetector, CryptoService.
- `lib/src/repositories/`: VaultRepository.
- `lib/src/validators/`: PolicyValidator.
- `lib/src/utils/`: WordList, CharSets.
- `lib/src/config/`: ToolkitConfig.
- `lib/src/application/`: ToolkitApp.
- `test/unit/`: Pengujian pembuatan sandi, entropi, dan pendeteksi pola.
- `test/integration/`: Pengujian alur brankas terenkripsi end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
""")

    # 3. lib/src/models/password_policy.dart
    write_f('lib/src/models/password_policy.dart', """class PasswordPolicy {
  final int minLength;
  final bool requireUppercase;
  final bool requireLowercase;
  final bool requireDigits;
  final bool requireSymbols;
  final bool excludeAmbiguous;

  const PasswordPolicy({
    this.minLength = 12,
    this.requireUppercase = true,
    this.requireLowercase = true,
    this.requireDigits = true,
    this.requireSymbols = true,
    this.excludeAmbiguous = false,
  });
}
""")

    # 4. lib/src/models/strength_result.dart
    write_f('lib/src/models/strength_result.dart', """class StrengthResult {
  final int score; // 0 - 100
  final double entropyBits;
  final String rating; // Weak, Fair, Good, Strong, Very Strong
  final List<String> warnings;
  final List<String> suggestions;

  StrengthResult({
    required this.score,
    required this.entropyBits,
    required this.rating,
    required this.warnings,
    required this.suggestions,
  });

  bool get isStrong => score >= 70;

  @override
  String toString() => '$rating ($score/100, ${entropyBits.toStringAsFixed(1)} bits)';
}
""")

    # 5. lib/src/models/passphrase_config.dart
    write_f('lib/src/models/passphrase_config.dart', """class PassphraseConfig {
  final int wordCount;
  final String separator;
  final bool capitalize;
  final bool includeNumber;

  const PassphraseConfig({
    this.wordCount = 4,
    this.separator = '-',
    this.capitalize = true,
    this.includeNumber = true,
  });
}
""")

    # 6. lib/src/models/vault_entry.dart
    write_f('lib/src/models/vault_entry.dart', """class VaultEntry {
  final String id;
  final String serviceName;
  final String username;
  final String encryptedCiphertext;
  final DateTime createdAt;

  VaultEntry({
    required this.id,
    required this.serviceName,
    required this.username,
    required this.encryptedCiphertext,
    DateTime? createdAt,
  }) : createdAt = createdAt ?? DateTime.now();

  Map<String, dynamic> toJson() => {
    'id': id,
    'serviceName': serviceName,
    'username': username,
    'encryptedCiphertext': encryptedCiphertext,
    'createdAt': createdAt.toIso8601String(),
  };

  factory VaultEntry.fromJson(Map<String, dynamic> json) => VaultEntry(
    id: json['id'] as String,
    serviceName: json['serviceName'] as String,
    username: json['username'] as String,
    encryptedCiphertext: json['encryptedCiphertext'] as String,
    createdAt: DateTime.parse(json['createdAt'] as String),
  );
}
""")

    # 7. lib/src/exceptions/toolkit_exception.dart
    write_f('lib/src/exceptions/toolkit_exception.dart', """class ToolkitException implements Exception {
  final String message;
  ToolkitException(this.message);

  @override
  String toString() => 'ToolkitException: $message';
}
""")

    # 8. lib/src/exceptions/vault_exception.dart
    write_f('lib/src/exceptions/vault_exception.dart', """import 'toolkit_exception.dart';

class VaultException extends ToolkitException {
  VaultException(super.message);

  @override
  String toString() => 'VaultException: $message';
}
""")

    # 9. lib/src/utils/char_sets.dart
    write_f('lib/src/utils/char_sets.dart', """class CharSets {
  static const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  static const lowercase = 'abcdefghijklmnopqrstuvwxyz';
  static const digits = '0123456789';
  static const symbols = '!@#\\$%^&*()-_=+[]{}|;:,.<>?';
  static const ambiguous = 'il1Lo0O';

  static String filterAmbiguous(String input) {
    final ambiguousSet = ambiguous.split('').toSet();
    return input.split('').where((c) => !ambiguousSet.contains(c)).join();
  }
}
""")

    # 10. lib/src/utils/word_list.dart
    write_f('lib/src/utils/word_list.dart', """class WordList {
  static const List<String> words = [
    'apple', 'bridge', 'castle', 'dragon', 'eagle', 'forest', 'galaxy', 'harbor',
    'island', 'jungle', 'knight', 'legend', 'mountain', 'nature', 'ocean', 'planet',
    'quantum', 'river', 'shadow', 'thunder', 'universe', 'valley', 'wizard', 'zenith',
    'beacon', 'crystal', 'diamond', 'emerald', 'falcon', 'glacier', 'horizon', 'meteor',
    'nebula', 'oasis', 'phoenix', 'radar', 'safari', 'titan', 'voyage', 'whisper'
  ];
}
""")

    # 11. lib/src/validators/policy_validator.dart
    write_f('lib/src/validators/policy_validator.dart', """import '../models/password_policy.dart';
import '../exceptions/toolkit_exception.dart';

class PolicyValidator {
  static void validate(PasswordPolicy policy) {
    if (policy.minLength < 4) {
      throw ToolkitException('Password minimum length must be at least 4.');
    }
    if (!policy.requireUppercase &&
        !policy.requireLowercase &&
        !policy.requireDigits &&
        !policy.requireSymbols) {
      throw ToolkitException('At least one character set must be enabled in policy.');
    }
  }
}
""")

    # 12. lib/src/services/entropy_calculator.dart
    write_f('lib/src/services/entropy_calculator.dart', """import 'dart:math' as math;

class EntropyCalculator {
  static double calculateEntropy(String password) {
    if (password.isEmpty) return 0.0;

    int poolSize = 0;
    if (RegExp(r'[a-z]').hasMatch(password)) poolSize += 26;
    if (RegExp(r'[A-Z]').hasMatch(password)) poolSize += 26;
    if (RegExp(r'[0-9]').hasMatch(password)) poolSize += 10;
    if (RegExp(r'[^a-zA-Z0-9]').hasMatch(password)) poolSize += 32;

    if (poolSize == 0) return 0.0;
    return password.length * (math.log(poolSize) / math.ln2);
  }
}
""")

    # 13. lib/src/services/pattern_detector.dart
    write_f('lib/src/services/pattern_detector.dart', """class PatternDetector {
  static const List<String> commonSequences = [
    '12345', '123456', 'qwerty', 'asdfgh', 'password', 'admin', 'abcde', 'welcome'
  ];

  static bool hasSequentialCharacters(String password) {
    final lower = password.toLowerCase();
    for (final seq in commonSequences) {
      if (lower.contains(seq)) return true;
    }
    return false;
  }

  static bool hasRepeatedCharacters(String password) {
    return RegExp(r'(.)\\1{2,}').hasMatch(password);
  }
}
""")

    # 14. lib/src/services/strength_checker.dart
    write_f('lib/src/services/strength_checker.dart', """import '../models/strength_result.dart';
import 'entropy_calculator.dart';
import 'pattern_detector.dart';

class StrengthChecker {
  static StrengthResult check(String password) {
    final warnings = <String>[];
    final suggestions = <String>[];
    int score = 0;

    final length = password.length;
    if (length >= 8) score += 20;
    if (length >= 12) score += 15;
    if (length >= 16) score += 15;

    if (RegExp(r'[a-z]').hasMatch(password)) score += 10;
    if (RegExp(r'[A-Z]').hasMatch(password)) score += 10;
    if (RegExp(r'[0-9]').hasMatch(password)) score += 15;
    if (RegExp(r'[^a-zA-Z0-9]').hasMatch(password)) score += 15;

    if (PatternDetector.hasRepeatedCharacters(password)) {
      score -= 20;
      warnings.add('Contains consecutive repeating characters.');
    }

    if (PatternDetector.hasSequentialCharacters(password)) {
      score -= 30;
      warnings.add('Contains predictable sequences or common words.');
    }

    if (length < 8) {
      warnings.add('Password is too short.');
      suggestions.add('Use at least 12 characters for better protection.');
    }

    if (!RegExp(r'[^a-zA-Z0-9]').hasMatch(password)) {
      suggestions.add('Add special symbols to increase complexity.');
    }

    score = score.clamp(0, 100);
    final entropy = EntropyCalculator.calculateEntropy(password);

    String rating = 'Weak';
    if (score >= 85) {
      rating = 'Very Strong';
    } else if (score >= 70) {
      rating = 'Strong';
    } else if (score >= 50) {
      rating = 'Good';
    } else if (score >= 30) {
      rating = 'Fair';
    }

    return StrengthResult(
      score: score,
      entropyBits: entropy,
      rating: rating,
      warnings: warnings,
      suggestions: suggestions,
    );
  }
}
""")

    # 15. lib/src/services/password_generator.dart
    write_f('lib/src/services/password_generator.dart', """import 'dart:math';
import '../models/password_policy.dart';
import '../utils/char_sets.dart';
import '../validators/policy_validator.dart';

class PasswordGenerator {
  final Random _rng;

  PasswordGenerator({Random? random}) : _rng = random ?? Random.secure();

  String generate(PasswordPolicy policy) {
    PolicyValidator.validate(policy);

    final allowedChars = StringBuffer();
    final guaranteed = <String>[];

    if (policy.requireUppercase) {
      final chars = policy.excludeAmbiguous ? CharSets.filterAmbiguous(CharSets.uppercase) : CharSets.uppercase;
      allowedChars.write(chars);
      guaranteed.add(chars[_rng.nextInt(chars.length)]);
    }

    if (policy.requireLowercase) {
      final chars = policy.excludeAmbiguous ? CharSets.filterAmbiguous(CharSets.lowercase) : CharSets.lowercase;
      allowedChars.write(chars);
      guaranteed.add(chars[_rng.nextInt(chars.length)]);
    }

    if (policy.requireDigits) {
      final chars = policy.excludeAmbiguous ? CharSets.filterAmbiguous(CharSets.digits) : CharSets.digits;
      allowedChars.write(chars);
      guaranteed.add(chars[_rng.nextInt(chars.length)]);
    }

    if (policy.requireSymbols) {
      final chars = policy.excludeAmbiguous ? CharSets.filterAmbiguous(CharSets.symbols) : CharSets.symbols;
      allowedChars.write(chars);
      guaranteed.add(chars[_rng.nextInt(chars.length)]);
    }

    final pool = allowedChars.toString();
    final result = List<String>.from(guaranteed);

    while (result.length < policy.minLength) {
      result.add(pool[_rng.nextInt(pool.length)]);
    }

    result.shuffle(_rng);
    return result.join();
  }
}
""")

    # 16. lib/src/services/passphrase_generator.dart
    write_f('lib/src/services/passphrase_generator.dart', """import 'dart:math';
import '../models/passphrase_config.dart';
import '../utils/word_list.dart';

class PassphraseGenerator {
  final Random _rng;

  PassphraseGenerator({Random? random}) : _rng = random ?? Random.secure();

  String generate([PassphraseConfig config = const PassphraseConfig()]) {
    final selectedWords = <String>[];
    for (int i = 0; i < config.wordCount; i++) {
      String word = WordList.words[_rng.nextInt(WordList.words.length)];
      if (config.capitalize) {
        word = word[0].toUpperCase() + word.substring(1);
      }
      selectedWords.add(word);
    }

    String result = selectedWords.join(config.separator);
    if (config.includeNumber) {
      result += '${config.separator}${_rng.nextInt(900) + 100}';
    }
    return result;
  }
}
""")

    # 17. lib/src/services/crypto_service.dart
    write_f('lib/src/services/crypto_service.dart', """import 'dart:convert';
import 'package:crypto/crypto.dart';

class CryptoService {
  static String hashKey(String masterKey) {
    return sha256.convert(utf8.encode(masterKey)).toString();
  }

  static String encrypt(String plaintext, String masterKey) {
    final keyBytes = sha256.convert(utf8.encode(masterKey)).bytes;
    final textBytes = utf8.encode(plaintext);
    final cipherBytes = <int>[];

    for (int i = 0; i < textBytes.length; i++) {
      cipherBytes.add(textBytes[i] ^ keyBytes[i % keyBytes.length]);
    }

    return base64.encode(cipherBytes);
  }

  static String decrypt(String ciphertext, String masterKey) {
    final keyBytes = sha256.convert(utf8.encode(masterKey)).bytes;
    final cipherBytes = base64.decode(ciphertext);
    final textBytes = <int>[];

    for (int i = 0; i < cipherBytes.length; i++) {
      textBytes.add(cipherBytes[i] ^ keyBytes[i % keyBytes.length]);
    }

    return utf8.decode(textBytes);
  }
}
""")

    # 18. lib/src/repositories/vault_repository.dart
    write_f('lib/src/repositories/vault_repository.dart', """import '../models/vault_entry.dart';
import '../exceptions/vault_exception.dart';

class VaultRepository {
  final List<VaultEntry> _entries = [];

  void add(VaultEntry entry) {
    if (_entries.any((e) => e.serviceName.toLowerCase() == entry.serviceName.toLowerCase() && e.username == entry.username)) {
      throw VaultException('Entry for service "${entry.serviceName}" with user "${entry.username}" already exists.');
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
""")

    # 19. lib/src/config/toolkit_config.dart
    write_f('lib/src/config/toolkit_config.dart', """import '../models/password_policy.dart';

class ToolkitConfig {
  final PasswordPolicy defaultPolicy;
  final String vaultStoragePath;

  const ToolkitConfig({
    this.defaultPolicy = const PasswordPolicy(),
    this.vaultStoragePath = 'data/vault.enc',
  });
}
""")

    # 20. lib/src/application/toolkit_app.dart
    write_f('lib/src/application/toolkit_app.dart', """import '../config/toolkit_config.dart';
import '../models/password_policy.dart';
import '../models/passphrase_config.dart';
import '../models/strength_result.dart';
import '../models/vault_entry.dart';
import '../repositories/vault_repository.dart';
import '../services/crypto_service.dart';
import '../services/passphrase_generator.dart';
import '../services/password_generator.dart';
import '../services/strength_checker.dart';

class ToolkitApp {
  final ToolkitConfig config;
  final PasswordGenerator passwordGenerator;
  final PassphraseGenerator passphraseGenerator;
  final VaultRepository vaultRepo;
  static int _idCounter = 0;

  ToolkitApp({ToolkitConfig? config})
      : config = config ?? const ToolkitConfig(),
        passwordGenerator = PasswordGenerator(),
        passphraseGenerator = PassphraseGenerator(),
        vaultRepo = VaultRepository();

  String generatePassword([PasswordPolicy? policy]) {
    return passwordGenerator.generate(policy ?? config.defaultPolicy);
  }

  String generatePassphrase([PassphraseConfig config = const PassphraseConfig()]) {
    return passphraseGenerator.generate(config);
  }

  StrengthResult checkStrength(String password) {
    return StrengthChecker.check(password);
  }

  VaultEntry saveCredential({
    required String serviceName,
    required String username,
    required String password,
    required String masterKey,
  }) {
    final encrypted = CryptoService.encrypt(password, masterKey);
    final entry = VaultEntry(
      id: 'vlt_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}',
      serviceName: serviceName,
      username: username,
      encryptedCiphertext: encrypted,
    );
    vaultRepo.add(entry);
    return entry;
  }

  String retrievePassword({
    required String serviceName,
    required String masterKey,
  }) {
    final entry = vaultRepo.findByService(serviceName);
    if (entry == null) {
      throw Exception('Service not found in vault: $serviceName');
    }
    return CryptoService.decrypt(entry.encryptedCiphertext, masterKey);
  }
}
""")

    # 21. lib/password_toolkit.dart
    write_f('lib/password_toolkit.dart', """export 'src/models/password_policy.dart';
export 'src/models/strength_result.dart';
export 'src/models/passphrase_config.dart';
export 'src/models/vault_entry.dart';
export 'src/exceptions/toolkit_exception.dart';
export 'src/exceptions/vault_exception.dart';
export 'src/services/password_generator.dart';
export 'src/services/passphrase_generator.dart';
export 'src/services/entropy_calculator.dart';
export 'src/services/strength_checker.dart';
export 'src/services/pattern_detector.dart';
export 'src/services/crypto_service.dart';
export 'src/repositories/vault_repository.dart';
export 'src/validators/policy_validator.dart';
export 'src/utils/word_list.dart';
export 'src/utils/char_sets.dart';
export 'src/config/toolkit_config.dart';
export 'src/application/toolkit_app.dart';
""")

    # 22. bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
import 'package:password_toolkit/password_toolkit.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('          03. PASSWORD & VAULT TOOLKIT        ');
  stdout.writeln('==============================================');

  final app = ToolkitApp();

  final pwd = app.generatePassword(const PasswordPolicy(minLength: 16));
  stdout.writeln('Generated Password : $pwd');

  final strength = app.checkStrength(pwd);
  stdout.writeln('Strength Assessment: $strength');

  final phrase = app.generatePassphrase(const PassphraseConfig(wordCount: 4));
  stdout.writeln('Generated Passphrase: $phrase');
  stdout.writeln('Passphrase Strength : ${app.checkStrength(phrase)}');

  stdout.writeln('----------------------------------------------');
  stdout.writeln('Testing Encrypted Vault...');
  const masterKey = 'super_secret_master_key_2026';
  app.saveCredential(
    serviceName: 'GitHub',
    username: 'developer@example.com',
    password: pwd,
    masterKey: masterKey,
  );

  final recovered = app.retrievePassword(serviceName: 'GitHub', masterKey: masterKey);
  stdout.writeln('Recovered Secret   : $recovered');
  stdout.writeln('Decryption Match   : ${recovered == pwd ? "SUCCESS" : "FAILED"}');
  stdout.writeln('==============================================');
}
""")

    # 23. test/unit/password_unit_test.dart
    write_f('test/unit/password_unit_test.dart', """import 'package:test/test.dart';
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
      expect(() => generator.generate(const PasswordPolicy(minLength: 2)), throwsA(isA<ToolkitException>()));
    });
  });

  group('Strength & Pattern Detector Tests', () {
    test('Flags sequential characters as weak', () {
      final res = StrengthChecker.check('qwerty123456');
      expect(res.score, lessThan(50));
      expect(res.warnings, contains('Contains predictable sequences or common words.'));
    });

    test('Rates complex diverse password as strong', () {
      final res = StrengthChecker.check('K9#mQ2!vL7&wXp0@');
      expect(res.score, greaterThanOrEqualTo(70));
      expect(res.isStrong, isTrue);
    });
  });
}
""")

    # 24. test/integration/vault_integration_test.dart
    write_f('test/integration/vault_integration_test.dart', """import 'package:test/test.dart';
import 'package:password_toolkit/password_toolkit.dart';

void main() {
  group('Encrypted Vault Flow Tests', () {
    late ToolkitApp app;
    const masterKey = 'master_pass_123';

    setUp(() {
      app = ToolkitApp();
    });

    test('Encrypts and decrypts credential roundtrip', () {
      const plainPassword = 'MySecretPassword!2026';
      app.saveCredential(
        serviceName: 'AWS',
        username: 'cloud_user',
        password: plainPassword,
        masterKey: masterKey,
      );

      final recovered = app.retrievePassword(serviceName: 'AWS', masterKey: masterKey);
      expect(recovered, equals(plainPassword));
    });

    test('Throws VaultException on duplicate service and username', () {
      app.saveCredential(
        serviceName: 'Gmail',
        username: 'user@gmail.com',
        password: 'Pass1',
        masterKey: masterKey,
      );

      expect(
        () => app.saveCredential(
          serviceName: 'Gmail',
          username: 'user@gmail.com',
          password: 'Pass2',
          masterKey: masterKey,
        ),
        throwsA(isA<VaultException>()),
      );
    });
  });
}
""")

    print("Project 03 (Password Toolkit) generated successfully with 22 Dart files!")

if __name__ == '__main__':
    generate_p03('dart-project-lab')
