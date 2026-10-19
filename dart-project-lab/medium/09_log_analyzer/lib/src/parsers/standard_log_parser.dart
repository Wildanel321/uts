import '../models/log_entry.dart';
import '../models/log_level.dart';
import '../utils/regex_patterns.dart';
import 'log_parser.dart';

class StandardLogParser implements LogParser {
  @override
  LogEntry? parseLine(String line) {
    final match = RegexPatterns.standardLog.firstMatch(line.trim());
    if (match == null) return null;

    final dateStr = match.group(1)!.replaceAll(' ', 'T');
    final levelStr = match.group(2)!;
    final source = match.group(3) ?? 'app';
    final message = match.group(4) ?? '';

    return LogEntry(
      timestamp: DateTime.tryParse(dateStr) ?? DateTime.now(),
      level: LogLevel.fromString(levelStr),
      message: message,
      source: source,
    );
  }
}
