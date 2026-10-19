import 'dart:math';

class StringSimilarity {
  static int levenshteinDistance(String a, String b) {
    final s1 = a.toLowerCase();
    final s2 = b.toLowerCase();

    final d = List.generate(
      s1.length + 1,
      (i) => List.filled(s2.length + 1, 0),
    );

    for (int i = 0; i <= s1.length; i++) {
      d[i][0] = i;
    }
    for (int j = 0; j <= s2.length; j++) {
      d[0][j] = j;
    }

    for (int i = 1; i <= s1.length; i++) {
      for (int j = 1; j <= s2.length; j++) {
        final cost = s1[i - 1] == s2[j - 1] ? 0 : 1;
        d[i][j] = min(
          d[i - 1][j] + 1,
          min(d[i][j - 1] + 1, d[i - 1][j - 1] + cost),
        );
      }
    }

    return d[s1.length][s2.length];
  }

  static bool isFuzzyMatch(String target, String query, {int maxDistance = 2}) {
    if (target.toLowerCase().contains(query.toLowerCase())) return true;
    return levenshteinDistance(target, query) <= maxDistance;
  }
}
