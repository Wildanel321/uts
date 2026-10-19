import 'dart:io';
import '../models/file_entry.dart';
import '../models/search_criteria.dart';
import '../validators/path_validator.dart';
import 'metadata_service.dart';

class FileSearchService {
  List<FileEntry> search(String rootPath, SearchCriteria criteria) {
    PathValidator.validateDirectoryExists(rootPath);
    final results = <FileEntry>[];

    final entities =
        Directory(rootPath).listSync(recursive: criteria.recursive);
    for (final entity in entities) {
      final entry = MetadataService.extract(entity);

      if (criteria.nameQuery != null &&
          !entry.name
              .toLowerCase()
              .contains(criteria.nameQuery!.toLowerCase())) {
        continue;
      }

      if (criteria.extension != null &&
          entry.extension != criteria.extension!.toLowerCase()) {
        continue;
      }

      if (!entry.isDirectory) {
        if (criteria.minSizeBytes != null &&
            entry.sizeBytes < criteria.minSizeBytes!) {
          continue;
        }
        if (criteria.maxSizeBytes != null &&
            entry.sizeBytes > criteria.maxSizeBytes!) {
          continue;
        }
      }

      results.add(entry);
    }

    return results;
  }
}
