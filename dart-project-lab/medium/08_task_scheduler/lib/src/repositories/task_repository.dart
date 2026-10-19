import '../models/execution_log.dart';
import '../models/scheduled_task.dart';
import '../models/task_status.dart';

class TaskRepository {
  final List<ScheduledTask> _tasks = [];
  final List<ExecutionLog> _logs = [];

  void save(ScheduledTask task) {
    final idx = _tasks.indexWhere((t) => t.id == task.id);
    if (idx >= 0) {
      _tasks[idx] = task;
    } else {
      _tasks.add(task);
    }
  }

  ScheduledTask? findById(String id) {
    for (final t in _tasks) {
      if (t.id == id) return t;
    }
    return null;
  }

  List<ScheduledTask> getAll() => List.unmodifiable(_tasks);

  List<ScheduledTask> getPendingDueTasks(DateTime now) {
    return _tasks
        .where((t) => t.status == TaskStatus.pending && !t.nextRun.isAfter(now))
        .toList()
      ..sort((a, b) => b.priority.weight.compareTo(a.priority.weight));
  }

  void addLog(ExecutionLog log) => _logs.add(log);
  List<ExecutionLog> getLogs() => List.unmodifiable(_logs);

  void clear() {
    _tasks.clear();
    _logs.clear();
  }
}
