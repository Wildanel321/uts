class PatternDetector {
  static const List<String> commonSequences = [
    '12345',
    '123456',
    'qwerty',
    'asdfgh',
    'password',
    'admin',
    'abcde',
    'welcome'
  ];

  static bool hasSequentialCharacters(String password) {
    final lower = password.toLowerCase();
    for (final seq in commonSequences) {
      if (lower.contains(seq)) return true;
    }
    return false;
  }

  static bool hasRepeatedCharacters(String password) {
    return RegExp(r'(.)\1{2,}').hasMatch(password);
  }
}
