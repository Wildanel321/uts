import 'task_priority.dart';
import 'task_status.dart';

class ScheduledTask {
  final String id;
  final String name;
  final String actionName;
  final TaskPriority priority;
  TaskStatus status;
  DateTime nextRun;
  final Duration? repeatInterval;
  final int maxRetries;
  int retryCount;
  final Map<String, dynamic> payload;

  ScheduledTask({
    required this.id,
    required this.name,
    required this.actionName,
    this.priority = TaskPriority.medium,
    this.status = TaskStatus.pending,
    DateTime? nextRun,
    this.repeatInterval,
    this.maxRetries = 3,
    this.retryCount = 0,
    this.payload = const {},
  }) : nextRun = nextRun ?? DateTime.now();

  bool get isRecurring => repeatInterval != null;
  bool get canRetry => retryCount < maxRetries;

  Map<String, dynamic> toJson() => {
        'id': id,
        'name': name,
        'actionName': actionName,
        'priority': priority.name,
        'status': status.name,
        'nextRun': nextRun.toIso8601String(),
        'repeatIntervalSeconds': repeatInterval?.inSeconds,
        'maxRetries': maxRetries,
        'retryCount': retryCount,
      };
}
