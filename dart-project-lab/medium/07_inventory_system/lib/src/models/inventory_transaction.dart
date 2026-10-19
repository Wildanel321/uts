import 'transaction_type.dart';

class InventoryTransaction {
  final String id;
  final String productId;
  final TransactionType type;
  final int quantity;
  final String referenceNote;
  final DateTime timestamp;

  InventoryTransaction({
    required this.id,
    required this.productId,
    required this.type,
    required this.quantity,
    this.referenceNote = '',
    DateTime? timestamp,
  }) : timestamp = timestamp ?? DateTime.now();

  Map<String, dynamic> toJson() => {
        'id': id,
        'productId': productId,
        'type': type.name,
        'quantity': quantity,
        'referenceNote': referenceNote,
        'timestamp': timestamp.toIso8601String(),
      };
}
