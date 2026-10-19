class SkuGenerator {
  static String generate(String category, String productName, int sequence) {
    final catCode =
        category.trim().toUpperCase().padRight(3, 'X').substring(0, 3);
    final prodCode = productName
        .trim()
        .toUpperCase()
        .replaceAll(RegExp(r'[^A-Z0-9]'), '')
        .padRight(3, 'X')
        .substring(0, 3);
    final seqCode = sequence.toString().padLeft(4, '0');
    return '$catCode-$prodCode-$seqCode';
  }
}
