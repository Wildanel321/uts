import 'package:test/test.dart';
import 'package:log_analyzer/log_analyzer.dart';

void main() {
  group('Log Analyzer Unit Tests', () {
    test('StandardLogParser parses standard formatted lines', () {
      final parser = StandardLogParser();
      final line =
          '[2026-05-10 14:30:00] [ERROR] [PaymentService] Card charge failed';
      final entry = parser.parseLine(line);

      expect(entry, isNotNull);
      expect(entry!.level, equals(LogLevel.error));
      expect(entry.source, equals('PaymentService'));
      expect(entry.message, equals('Card charge failed'));
    });

    test('ClfLogParser parses Common Log Format lines', () {
      final parser = ClfLogParser();
      final line =
          '10.0.0.1 - - [10/Oct/2026:13:55:36 +0000] "GET /api/v1/users HTTP/1.1" 200 1024';
      final entry = parser.parseLine(line);

      expect(entry, isNotNull);
      expect(entry!.ip, equals('10.0.0.1'));
      expect(entry.statusCode, equals(200));
      expect(entry.level, equals(LogLevel.info));
    });

    test('ErrorClusteringService groups repetitive error messages', () {
      final entries = [
        LogEntry(
            timestamp: DateTime.now(),
            level: LogLevel.error,
            message: 'Timeout connecting to 192.168.1.100:8080'),
        LogEntry(
            timestamp: DateTime.now(),
            level: LogLevel.error,
            message: 'Timeout connecting to 192.168.1.101:8080'),
      ];

      final clusters = ErrorClusteringService.clusterErrors(entries);
      expect(clusters.length, equals(1));
      expect(clusters.values.first, equals(2));
    });
  });
}
