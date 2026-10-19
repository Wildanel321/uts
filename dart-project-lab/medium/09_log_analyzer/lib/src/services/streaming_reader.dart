import 'dart:convert';
import 'dart:io';
import '../models/log_entry.dart';
import '../parsers/log_parser.dart';

class StreamingReader {
  final LogParser parser;

  StreamingReader(this.parser);

  Stream<LogEntry> readEntries(String filePath) async* {
    final file = File(filePath);
    if (!file.existsSync()) return;

    final lines =
        file.openRead().transform(utf8.decoder).transform(const LineSplitter());
    await for (final line in lines) {
      final entry = parser.parseLine(line);
      if (entry != null) {
        yield entry;
      }
    }
  }
}
