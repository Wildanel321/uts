import 'dart:io';
import 'package:file_manager/file_manager.dart';

void main(List<String> args) async {
  stdout.writeln('==============================================');
  stdout.writeln('          04. FILE MANAGER CLI                ');
  stdout.writeln('==============================================');

  final app = FileManagerApp();
  final targetDir = args.isNotEmpty ? args[0] : Directory.current.path;

  stdout.writeln('Target Directory: $targetDir\n');
  stdout.writeln('Contents:');
  final items = app.listDirectory(targetDir);
  for (final item in items.take(10)) {
    final sizeStr =
        item.isDirectory ? '<DIR>' : SizeFormatter.format(item.sizeBytes);
    stdout.writeln('  ${item.name.padRight(30)} $sizeStr');
  }

  stdout.writeln('\nGrouping by Extension Category:');
  final groups = app.groupExtensions(targetDir);
  for (final entry in groups.entries) {
    stdout.writeln(
        '  ${entry.key.padRight(12)}: ${entry.value.fileCount} files (${SizeFormatter.format(entry.value.totalBytes)})');
  }

  stdout.writeln('==============================================');
}
