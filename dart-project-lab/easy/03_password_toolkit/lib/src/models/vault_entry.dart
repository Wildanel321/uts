class VaultEntry {
  final String id;
  final String serviceName;
  final String username;
  final String encryptedCiphertext;
  final DateTime createdAt;

  VaultEntry({
    required this.id,
    required this.serviceName,
    required this.username,
    required this.encryptedCiphertext,
    DateTime? createdAt,
  }) : createdAt = createdAt ?? DateTime.now();

  Map<String, dynamic> toJson() => {
        'id': id,
        'serviceName': serviceName,
        'username': username,
        'encryptedCiphertext': encryptedCiphertext,
        'createdAt': createdAt.toIso8601String(),
      };

  factory VaultEntry.fromJson(Map<String, dynamic> json) => VaultEntry(
        id: json['id'] as String,
        serviceName: json['serviceName'] as String,
        username: json['username'] as String,
        encryptedCiphertext: json['encryptedCiphertext'] as String,
        createdAt: DateTime.parse(json['createdAt'] as String),
      );
}
