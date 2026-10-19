import 'dart:math';
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
      final chars = policy.excludeAmbiguous
          ? CharSets.filterAmbiguous(CharSets.uppercase)
          : CharSets.uppercase;
      allowedChars.write(chars);
      guaranteed.add(chars[_rng.nextInt(chars.length)]);
    }

    if (policy.requireLowercase) {
      final chars = policy.excludeAmbiguous
          ? CharSets.filterAmbiguous(CharSets.lowercase)
          : CharSets.lowercase;
      allowedChars.write(chars);
      guaranteed.add(chars[_rng.nextInt(chars.length)]);
    }

    if (policy.requireDigits) {
      final chars = policy.excludeAmbiguous
          ? CharSets.filterAmbiguous(CharSets.digits)
          : CharSets.digits;
      allowedChars.write(chars);
      guaranteed.add(chars[_rng.nextInt(chars.length)]);
    }

    if (policy.requireSymbols) {
      final chars = policy.excludeAmbiguous
          ? CharSets.filterAmbiguous(CharSets.symbols)
          : CharSets.symbols;
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
