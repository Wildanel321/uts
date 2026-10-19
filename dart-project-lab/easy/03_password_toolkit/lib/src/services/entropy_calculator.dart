import 'dart:math' as math;

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
