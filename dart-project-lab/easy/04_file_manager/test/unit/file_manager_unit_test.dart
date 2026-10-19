import 'package:test/test.dart';
import 'package:file_manager/file_manager.dart';

void main() {
  group('File Manager Unit Tests', () {
    test('SizeFormatter formats bytes correctly', () {
      expect(SizeFormatter.format(500), equals('500 B'));
      expect(SizeFormatter.format(2048), equals('2.0 KB'));
      expect(SizeFormatter.format(5 * 1024 * 1024), equals('5.0 MB'));
    });

    test('PathHelper extracts extension and basename', () {
      expect(PathHelper.getExtension('hello/world.dart'), equals('.dart'));
      expect(PathHelper.getBasename('foo/bar/test.txt'), equals('test.txt'));
    });

    test('PathValidator checks for path traversal', () {
      expect(() => PathValidator.validateNoTraversal('../secret'),
          throwsA(isA<FileManagerException>()));
    });
  });
}
