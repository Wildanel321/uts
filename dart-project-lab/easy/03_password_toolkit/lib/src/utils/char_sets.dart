class CharSets {
  static const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  static const lowercase = 'abcdefghijklmnopqrstuvwxyz';
  static const digits = '0123456789';
  static const symbols = '!@#\$%^&*()-_=+[]{}|;:,.<>?';
  static const ambiguous = 'il1Lo0O';

  static String filterAmbiguous(String input) {
    final ambiguousSet = ambiguous.split('').toSet();
    return input.split('').where((c) => !ambiguousSet.contains(c)).join();
  }
}
