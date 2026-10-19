import '../models/scheduled_task.dart';
import '../models/scheduler_metrics.dart';
import '../models/task_priority.dart';
import '../models/task_status.dart';
import '../repositories/task_repository.dart';
import '../validators/task_validator.dart';
import 'retry_manager.dart';
import 'task_executor.dart';
import 'worker_pool.dart';

class SchedulerService {
  final TaskRepository repository;
  final TaskExecutor executor;
  final WorkerPool workerPool;
  static int _idCounter = 0;

  SchedulerService(this.repository, this.executor, {int maxWorkers = 2})
      : workerPool = WorkerPool(executor: executor, maxConcurrent: maxWorkers);

  ScheduledTask schedule({
    required String name,
    required String actionName,
    TaskPriority priority = TaskPriority.medium,
    DateTime? runAt,
    Duration? repeatInterval,
    int maxRetries = 3,
    Map<String, dynamic> payload = const {},
  }) {
    final task = ScheduledTask(
      id: 'tsk_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}',
      name: name,
      actionName: actionName,
      priority: priority,
      nextRun: runAt ?? DateTime.now(),
      repeatInterval: repeatInterval,
      maxRetries: maxRetries,
      payload: payload,
    );

    TaskValidator.validate(task);
    repository.save(task);
    return task;
  }

  Future<int> runPendingBatch({DateTime? currentTime}) async {
    final now = currentTime ?? DateTime.now();
    final due = repository.getPendingDueTasks(now);
    int dispatched = 0;

    for (final task in due) {
      if (!workerPool.hasCapacity) break;

      dispatched++;
      await workerPool.runTask(task, (t, success) {
        if (success) {
          if (t.isRecurring) {
            t.status = TaskStatus.pending;
            t.nextRun = now.add(t.repeatInterval!);
            t.retryCount = 0;
          } else {
            t.status = TaskStatus.completed;
          }
        } else {
          if (t.canRetry) {
            t.retryCount++;
            t.status = TaskStatus.pending;
            t.nextRun = now.add(RetryManager.calculateBackoff(t.retryCount));
          } else {
            t.status = TaskStatus.failed;
          }
        }
        repository.save(t);
      });
    }

    return dispatched;
  }

  SchedulerMetrics getMetrics() {
    final all = repository.getAll();
    return SchedulerMetrics(
      totalTasks: all.length,
      pendingCount: all.where((t) => t.status == TaskStatus.pending).length,
      completedCount: all.where((t) => t.status == TaskStatus.completed).length,
      failedCount: all.where((t) => t.status == TaskStatus.failed).length,
    );
  }
}
