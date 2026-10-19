class NumberFormatter {
  static String format(double value, {int precision = 8}) {
    if (value.isNaN) return 'NaN';
    if (value.isInfinite) return value.isNegative ? '-Infinity' : 'Infinity';

    // Check if whole integer
    if (value == value.roundToDouble() && value.abs() < 1e12) {
      return value.toInt().toString();
    }

    final str = value.toStringAsFixed(precision);
    // Trim trailing zeroes
    final trimmed =
        str.replaceAll(RegExp(r'0+$'), '').replaceAll(RegExp(r'\.$'), '');
    return trimmed;
  }
}
