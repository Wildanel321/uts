class CurrencyFormatter {
  static String format(double amount, {String symbol = 'Rp '}) {
    final isNegative = amount < 0;
    final absAmount = amount.abs();
    final parts = absAmount.toStringAsFixed(2).split('.');
    final integerPart = parts[0];
    final decimalPart = parts[1];

    final buffer = StringBuffer();
    for (int i = 0; i < integerPart.length; i++) {
      if (i > 0 && (integerPart.length - i) % 3 == 0) {
        buffer.write('.');
      }
      buffer.write(integerPart[i]);
    }

    final formatted =
        '$symbol${buffer.toString()},${decimalPart == '00' ? '-' : decimalPart}';
    return isNegative ? '-$formatted' : formatted;
  }
}
