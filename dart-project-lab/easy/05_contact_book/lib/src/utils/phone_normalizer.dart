class PhoneNormalizer {
  static String normalize(String phone) {
    String clean = phone.replaceAll(RegExp(r'[\s\-\(\)]'), '');
    if (clean.startsWith('08')) {
      clean = '+628${clean.substring(2)}';
    }
    return clean;
  }
}
