class AuditEntry {
  final String id;
  final String action;
  final String entityId;
  final String details;
  final DateTime createdAt;

  AuditEntry({
    required this.id,
    required this.action,
    required this.entityId,
    required this.details,
    DateTime? createdAt,
  }) : createdAt = createdAt ?? DateTime.now();
}
