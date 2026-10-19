import 'package:test/test.dart';
import 'package:task_scheduler/task_scheduler.dart';

void main() {
  group('Task Scheduler Integration Flow Tests', () {
    late SchedulerApp app;

    setUp(() {
      app = SchedulerApp.create();
    });

    test('Executes tasks in priority order and updates status', () async {
      final executed = <String>[];

      app.registerAction('action_low', (payload) => executed.add('low'));
      app.registerAction('action_urgent', (payload) => executed.add('urgent'));

      app.addTask('Low Task', 'action_low', priority: TaskPriority.low);
      app.addTask('Urgent Task', 'action_urgent',
          priority: TaskPriority.urgent);

      final dispatched = await app.executePending();
      expect(dispatched, equals(2));
      expect(executed.first, equals('urgent'));
      expect(executed.last, equals('low'));

      final metrics = app.getMetrics();
      expect(metrics.completedCount, equals(2));
    });

    test('Reschedules recurring task for next interval', () async {
      int count = 0;
      app.registerAction('recurring_action', (payload) => count++);

      final task = app.addTask(
        'Heartbeat',
        'recurring_action',
        repeatInterval: const Duration(minutes: 5),
      );

      await app.executePending();
      expect(count, equals(1));
      expect(task.status, equals(TaskStatus.pending));
      expect(task.nextRun.isAfter(DateTime.now()), isTrue);
    });
  });
}
