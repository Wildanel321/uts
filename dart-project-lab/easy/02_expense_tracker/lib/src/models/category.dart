import 'transaction_type.dart';

class Category {
  final String id;
  final String name;
  final TransactionType type;

  const Category({
    required this.id,
    required this.name,
    required this.type,
  });

  Map<String, dynamic> toJson() => {
        'id': id,
        'name': name,
        'type': type.name,
      };

  factory Category.fromJson(Map<String, dynamic> json) => Category(
        id: json['id'] as String,
        name: json['name'] as String,
        type: TransactionType.values.byName(json['type'] as String),
      );

  @override
  String toString() => '$name (${type.name})';
}
