import 'dart:async';
import '../models/execution_log.dart';
import '../models/scheduled_task.dart';
import '../models/task_status.dart';

typedef TaskActionHandler = FutureOr<void> Function(
    Map<String, dynamic> payload);

class TaskExecutor {
  final Map<String, TaskActionHandler> _handlers = {};

  void registerHandler(String actionName, TaskActionHandler handler) {
    _handlers[actionName] = handler;
  }

  Future<ExecutionLog> execute(ScheduledTask task) async {
    final handler = _handlers[task.actionName];
    final start = DateTime.now();

    if (handler == null) {
      return ExecutionLog(
        taskId: task.id,
        executedAt: start,
        isSuccess: false,
        durationMs: 0,
        errorMessage: 'Handler not registered for action "${task.actionName}"',
      );
    }

    try {
      task.status = TaskStatus.running;
      await handler(task.payload);
      final duration = DateTime.now().difference(start).inMilliseconds;
      task.status = TaskStatus.completed;

      return ExecutionLog(
        taskId: task.id,
        executedAt: start,
        isSuccess: true,
        durationMs: duration,
      );
    } catch (e) {
      final duration = DateTime.now().difference(start).inMilliseconds;
      task.status = TaskStatus.failed;
      return ExecutionLog(
        taskId: task.id,
        executedAt: start,
        isSuccess: false,
        durationMs: duration,
        errorMessage: e.toString(),
      );
    }
  }
}
