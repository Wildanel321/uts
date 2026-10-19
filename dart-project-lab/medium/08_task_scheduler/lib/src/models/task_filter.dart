import 'task_priority.dart';
import 'task_status.dart';

class TaskFilter {
  final TaskStatus? status;
  final TaskPriority? minPriority;
  final String? actionName;

  const TaskFilter({
    this.status,
    this.minPriority,
    this.actionName,
  });
}
