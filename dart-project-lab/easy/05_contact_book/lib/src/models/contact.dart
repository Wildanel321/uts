class Contact {
  final String id;
  final String name;
  final String phone;
  final String email;
  final String address;
  final String notes;
  final String group;
  final bool isFavorite;
  final DateTime updatedAt;

  Contact({
    required this.id,
    required this.name,
    required this.phone,
    required this.email,
    this.address = '',
    this.notes = '',
    this.group = 'General',
    this.isFavorite = false,
    DateTime? updatedAt,
  }) : updatedAt = updatedAt ?? DateTime.now();

  Contact copyWith({
    String? name,
    String? phone,
    String? email,
    String? address,
    String? notes,
    String? group,
    bool? isFavorite,
  }) {
    return Contact(
      id: id,
      name: name ?? this.name,
      phone: phone ?? this.phone,
      email: email ?? this.email,
      address: address ?? this.address,
      notes: notes ?? this.notes,
      group: group ?? this.group,
      isFavorite: isFavorite ?? this.isFavorite,
      updatedAt: DateTime.now(),
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'name': name,
        'phone': phone,
        'email': email,
        'address': address,
        'notes': notes,
        'group': group,
        'isFavorite': isFavorite,
        'updatedAt': updatedAt.toIso8601String(),
      };

  factory Contact.fromJson(Map<String, dynamic> json) => Contact(
        id: json['id'] as String,
        name: json['name'] as String,
        phone: json['phone'] as String,
        email: json['email'] as String,
        address: json['address'] as String? ?? '',
        notes: json['notes'] as String? ?? '',
        group: json['group'] as String? ?? 'General',
        isFavorite: json['isFavorite'] as bool? ?? false,
        updatedAt: DateTime.parse(json['updatedAt'] as String),
      );
}
