import '../models/audit_entry.dart';

class AuditRepository {
  final List<AuditEntry> _logs = [];

  void log(String action, String entityId, String details) {
    final entry = AuditEntry(
      id: 'aud_${DateTime.now().microsecondsSinceEpoch}',
      action: action,
      entityId: entityId,
      details: details,
    );
    _logs.add(entry);
  }

  List<AuditEntry> getAll() => List.unmodifiable(_logs);
}
