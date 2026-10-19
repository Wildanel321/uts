import 'log_level.dart';

class LogEntry {
  final DateTime timestamp;
  final LogLevel level;
  final String message;
  final String source;
  final String? ip;
  final int? statusCode;
  final int? durationMs;

  LogEntry({
    required this.timestamp,
    required this.level,
    required this.message,
    this.source = 'app',
    this.ip,
    this.statusCode,
    this.durationMs,
  });

  Map<String, dynamic> toJson() => {
        'timestamp': timestamp.toIso8601String(),
        'level': level.name,
        'message': message,
        'source': source,
        'ip': ip,
        'statusCode': statusCode,
        'durationMs': durationMs,
      };
}
