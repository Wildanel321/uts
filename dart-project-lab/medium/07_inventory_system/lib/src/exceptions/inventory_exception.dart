class InventoryException implements Exception {
  final String message;
  InventoryException(this.message);

  @override
  String toString() => 'InventoryException: $message';
}
