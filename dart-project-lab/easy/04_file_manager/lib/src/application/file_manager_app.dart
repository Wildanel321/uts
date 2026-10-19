import '../config/manager_config.dart';
import '../models/file_entry.dart';
import '../models/file_type_group.dart';
import '../models/hash_result.dart';
import '../models/search_criteria.dart';
import '../services/directory_service.dart';
import '../services/file_operation_service.dart';
import '../services/file_search_service.dart';
import '../services/hash_service.dart';

class FileManagerApp {
  final ManagerConfig config;
  final DirectoryService directoryService;
  final FileSearchService searchService;
  final FileOperationService operationService;

  FileManagerApp({ManagerConfig? config})
      : config = config ?? const ManagerConfig(),
        directoryService = DirectoryService(),
        searchService = FileSearchService(),
        operationService = FileOperationService();

  List<FileEntry> listDirectory(String path) =>
      directoryService.listDirectory(path);

  Map<String, FileTypeGroup> groupExtensions(String path,
      {bool recursive = false}) {
    return directoryService.groupFilesByCategory(path, recursive: recursive);
  }

  List<FileEntry> searchFiles(String path, SearchCriteria criteria) {
    return searchService.search(path, criteria);
  }

  Future<HashResult> getChecksum(String filePath) =>
      HashService.computeSha256(filePath);
}
