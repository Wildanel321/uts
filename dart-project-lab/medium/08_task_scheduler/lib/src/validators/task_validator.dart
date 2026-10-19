import '../exceptions/scheduler_exception.dart';
import '../models/scheduled_task.dart';

class TaskValidator {
  static void validate(ScheduledTask task) {
    if (task.name.trim().isEmpty) {
      throw SchedulerException('Task name cannot be empty.');
    }
    if (task.actionName.trim().isEmpty) {
      throw SchedulerException('Task actionName must be specified.');
    }
    if (task.maxRetries < 0) {
      throw SchedulerException('maxRetries cannot be negative.');
    }
  }
}
