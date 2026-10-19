import 'dart:convert';
import '../models/contact.dart';
import '../models/import_export_result.dart';
import '../repositories/contact_repository.dart';

class SerializationService {
  final ContactRepository repository;

  SerializationService(this.repository);

  String exportToJson() {
    final list = repository.getAll().map((c) => c.toJson()).toList();
    return const JsonEncoder.withIndent('  ').convert(list);
  }

  ImportExportResult importFromJson(String jsonString) {
    final errors = <String>[];
    int success = 0;
    int failure = 0;

    try {
      final decoded = jsonDecode(jsonString) as List<dynamic>;
      for (final item in decoded) {
        try {
          final c = Contact.fromJson(item as Map<String, dynamic>);
          repository.save(c);
          success++;
        } catch (e) {
          failure++;
          errors.add('Failed to parse contact: $e');
        }
      }
    } catch (e) {
      errors.add('Invalid JSON document: $e');
    }

    return ImportExportResult(
        successCount: success, failureCount: failure, errors: errors);
  }
}
