class BookConfig {
  final String storagePath;
  final bool autoNormalizePhone;

  const BookConfig({
    this.storagePath = 'data/contacts.json',
    this.autoNormalizePhone = true,
  });
}
