import 'dart:io';
import 'package:test/test.dart';
import 'package:file_manager/file_manager.dart';

void main() {
  group('File Manager Integration Tests', () {
    late Directory tempDir;
    late FileManagerApp app;

    setUp(() {
      tempDir = Directory.systemTemp.createTempSync('fm_test_');
      app = FileManagerApp();
    });

    tearDown(() {
      if (tempDir.existsSync()) {
        tempDir.deleteSync(recursive: true);
      }
    });

    test('Creates, searches, computes checksum, and safely deletes file',
        () async {
      final sampleFile = File('${tempDir.path}/sample.txt');
      sampleFile
          .writeAsStringSync('Pure Dart File Manager Integration Test Content');

      final list = app.listDirectory(tempDir.path);
      expect(list.any((f) => f.name == 'sample.txt'), isTrue);

      final searchResults = app.searchFiles(
          tempDir.path, const SearchCriteria(extension: '.txt'));
      expect(searchResults.length, equals(1));
      expect(searchResults.first.name, equals('sample.txt'));

      final hash = await app.getChecksum(sampleFile.path);
      expect(hash.algorithm, equals('SHA-256'));
      expect(hash.digestHex.length, equals(64));

      final deleted = app.operationService.safeDelete(sampleFile.path);
      expect(deleted, isTrue);
      expect(sampleFile.existsSync(), isFalse);
    });
  });
}
