import '../config/scheduler_config.dart';
import '../models/scheduled_task.dart';
import '../models/scheduler_metrics.dart';
import '../models/task_priority.dart';
import '../repositories/task_repository.dart';
import '../services/scheduler_service.dart';
import '../services/task_executor.dart';

class SchedulerApp {
  final SchedulerConfig config;
  final TaskRepository repository;
  final TaskExecutor executor;
  final SchedulerService schedulerService;

  SchedulerApp({SchedulerConfig? config})
      : config = config ?? const SchedulerConfig(),
        repository = TaskRepository(),
        executor = TaskExecutor(),
        schedulerService = SchedulerService(
          TaskRepository(),
          TaskExecutor(),
          maxWorkers: (config ?? const SchedulerConfig()).maxConcurrentWorkers,
        );

  factory SchedulerApp.create({SchedulerConfig? config}) {
    final repo = TaskRepository();
    final exec = TaskExecutor();
    final cfg = config ?? const SchedulerConfig();
    return SchedulerApp._internal(
      cfg,
      repo,
      exec,
      SchedulerService(repo, exec, maxWorkers: cfg.maxConcurrentWorkers),
    );
  }

  SchedulerApp._internal(
    this.config,
    this.repository,
    this.executor,
    this.schedulerService,
  );

  void registerAction(String name, TaskActionHandler handler) {
    executor.registerHandler(name, handler);
  }

  ScheduledTask addTask(
    String name,
    String actionName, {
    TaskPriority priority = TaskPriority.medium,
    Duration? repeatInterval,
    Map<String, dynamic> payload = const {},
  }) {
    return schedulerService.schedule(
      name: name,
      actionName: actionName,
      priority: priority,
      repeatInterval: repeatInterval,
      payload: payload,
    );
  }

  Future<int> executePending() => schedulerService.runPendingBatch();
  SchedulerMetrics getMetrics() => schedulerService.getMetrics();
}
