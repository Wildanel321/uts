class StrengthResult {
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
  String toString() =>
      '$rating ($score/100, ${entropyBits.toStringAsFixed(1)} bits)';
}
