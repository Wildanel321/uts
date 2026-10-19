import 'package:test/test.dart';
import 'package:task_scheduler/task_scheduler.dart';

void main() {
  group('Scheduler Unit Tests', () {
    test('TaskPriority weight comparison', () {
      expect(TaskPriority.urgent.weight, greaterThan(TaskPriority.high.weight));
      expect(TaskPriority.high.weight, greaterThan(TaskPriority.medium.weight));
      expect(TaskPriority.medium.weight, greaterThan(TaskPriority.low.weight));
    });

    test('RetryManager calculates exponential backoff', () {
      final delay1 = RetryManager.calculateBackoff(1,
          baseDelay: const Duration(seconds: 1));
      final delay2 = RetryManager.calculateBackoff(2,
          baseDelay: const Duration(seconds: 1));
      final delay3 = RetryManager.calculateBackoff(3,
          baseDelay: const Duration(seconds: 1));

      expect(delay1.inSeconds, equals(2));
      expect(delay2.inSeconds, equals(4));
      expect(delay3.inSeconds, equals(8));
    });

    test('CronParser parses simple @every intervals', () {
      expect(CronParser.parseSimple('@every 30s')?.inSeconds, equals(30));
      expect(CronParser.parseSimple('@every 5m')?.inMinutes, equals(5));
      expect(CronParser.parseSimple('invalid'), isNull);
    });
  });
}
