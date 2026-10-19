import 'dart:async';
import '../models/scheduled_task.dart';
import 'task_executor.dart';

class WorkerPool {
  final int maxConcurrent;
  final TaskExecutor executor;
  int _activeWorkers = 0;

  WorkerPool({required this.executor, this.maxConcurrent = 2});

  int get availableSlots => maxConcurrent - _activeWorkers;
  bool get hasCapacity => _activeWorkers < maxConcurrent;

  Future<void> runTask(ScheduledTask task,
      void Function(ScheduledTask t, bool success) onDone) async {
    _activeWorkers++;
    try {
      final log = await executor.execute(task);
      onDone(task, log.isSuccess);
    } finally {
      _activeWorkers--;
    }
  }
}
