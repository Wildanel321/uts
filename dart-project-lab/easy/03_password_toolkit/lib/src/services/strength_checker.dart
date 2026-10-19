import '../models/strength_result.dart';
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
