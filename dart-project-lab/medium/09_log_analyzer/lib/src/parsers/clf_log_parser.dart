import '../models/log_entry.dart';
import '../models/log_level.dart';
import '../utils/regex_patterns.dart';
import 'log_parser.dart';

class ClfLogParser implements LogParser {
  @override
  LogEntry? parseLine(String line) {
    final match = RegexPatterns.clfLog.firstMatch(line.trim());
    if (match == null) return null;

    final ip = match.group(1)!;
    final path = match.group(4)!;
    final statusCode = int.tryParse(match.group(5)!) ?? 200;

    LogLevel level = LogLevel.info;
    if (statusCode >= 500) {
      level = LogLevel.error;
    } else if (statusCode >= 400) {
      level = LogLevel.warn;
    }

    return LogEntry(
      timestamp: DateTime.now(),
      level: level,
      message: 'Request to $path (Status: $statusCode)',
      source: 'web_server',
      ip: ip,
      statusCode: statusCode,
    );
  }
}
