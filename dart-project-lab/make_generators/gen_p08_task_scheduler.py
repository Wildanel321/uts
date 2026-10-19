import os

def generate_p08(base_dir):
    pdir = os.path.join(base_dir, 'medium', '08_task_scheduler')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'repositories'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'validators'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'utils'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'config'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'application'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'unit'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'integration'), exist_ok=True)

    def write_f(rel_path, content):
        target = os.path.join(pdir, rel_path)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

    write_f('pubspec.yaml', """name: task_scheduler
description: Pure Dart Task Scheduler with priority queues, recurring cron-like timers, retry backoff, and worker pool.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dev_dependencies:
  test: ^1.25.0
""")

    write_f('README.md', """# 08. Task Scheduler

Aplikasi penjadwal tugas (*Task Scheduler & Worker Pool*) tingkat menengah berbasis Dart murni. Menyediakan antrean tugas dengan berbagai tingkat prioritas (*Low, Medium, High, Urgent*), eksekusi satu kali (*one-off*) maupun berulang (*recurring intervals/cron-like*), manajemen konkurensi worker, serta mekanisme *retry* cerdas jika terjadi kegagalan.

## Fitur Utama
- **Manajemen Tugas Berprioritas**: 4 level prioritas untuk menentukan urutan eksekusi pekerjaan.
- **Tugas Berulang & Terjadwal**: Dukungan interval berulang (detik, menit, jam) dan penjadwalan masa depan.
- **Worker Pool Berbasis Dart**: Kolam worker dengan pembatasan konkurensi untuk mencegah *resource exhaustion*.
- **Penanganan Kegagalan (Retry Backoff)**: Percobaan ulang otomatis dengan batas maksimal dan pencatatan riwayat error.
- **Pelacakan Metrik & Audit**: Log riwayat eksekusi, durasi waktu komputasi, dan status tugas kekal.

## Struktur File (22 File Dart)
- `bin/main.dart`: Entry point CLI interaktif.
- `lib/task_scheduler.dart`: Export publik modul.
- `lib/src/models/`: ScheduledTask, TaskStatus, TaskPriority, ExecutionLog, SchedulerMetrics.
- `lib/src/exceptions/`: SchedulerException.
- `lib/src/repositories/`: TaskRepository.
- `lib/src/services/`: CronParser, RetryManager, TaskExecutor, WorkerPool, SchedulerService.
- `lib/src/validators/`: TaskValidator.
- `lib/src/utils/`: TimeUtils.
- `lib/src/config/`: SchedulerConfig.
- `lib/src/application/`: SchedulerApp.
- `test/unit/`: Pengujian prioritas tugas, retry backoff, dan parser ekspresi waktu.
- `test/integration/`: Pengujian alur eksekusi tugas dalam worker pool end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
""")

    # models
    write_f('lib/src/models/task_status.dart', """enum TaskStatus {
  pending,
  running,
  completed,
  failed,
  cancelled,
}
""")

    write_f('lib/src/models/task_priority.dart', """enum TaskPriority {
  low,
  medium,
  high,
  urgent;

  int get weight {
    switch (this) {
      case TaskPriority.low:
        return 1;
      case TaskPriority.medium:
        return 2;
      case TaskPriority.high:
        return 3;
      case TaskPriority.urgent:
        return 4;
    }
  }
}
""")

    write_f('lib/src/models/execution_log.dart', """class ExecutionLog {
  final String taskId;
  final DateTime executedAt;
  final bool isSuccess;
  final int durationMs;
  final String? errorMessage;

  ExecutionLog({
    required this.taskId,
    required this.executedAt,
    required this.isSuccess,
    required this.durationMs,
    this.errorMessage,
  });

  @override
  String toString() => '[$executedAt] Task $taskId: ${isSuccess ? "SUCCESS" : "FAILED ($errorMessage)"} (${durationMs}ms)';
}
""")

    write_f('lib/src/models/scheduler_metrics.dart', """class SchedulerMetrics {
  final int totalTasks;
  final int pendingCount;
  final int completedCount;
  final int failedCount;

  const SchedulerMetrics({
    required this.totalTasks,
    required this.pendingCount,
    required this.completedCount,
    required this.failedCount,
  });

  @override
  String toString() => 'Total: $totalTasks | Pending: $pendingCount | Done: $completedCount | Failed: $failedCount';
}
""")

    write_f('lib/src/models/scheduled_task.dart', """import 'task_priority.dart';
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
""")

    # exceptions
    write_f('lib/src/exceptions/scheduler_exception.dart', """class SchedulerException implements Exception {
  final String message;
  SchedulerException(this.message);

  @override
  String toString() => 'SchedulerException: $message';
}
""")

    # utils
    write_f('lib/src/utils/time_utils.dart', """class TimeUtils {
  static String formatDuration(Duration duration) {
    if (duration.inSeconds < 60) return '${duration.inSeconds}s';
    if (duration.inMinutes < 60) return '${duration.inMinutes}m';
    return '${duration.inHours}h ${duration.inMinutes % 60}m';
  }
}
""")

    # validators
    write_f('lib/src/validators/task_validator.dart', """import '../exceptions/scheduler_exception.dart';
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
""")

    # repositories
    write_f('lib/src/repositories/task_repository.dart', """import '../models/execution_log.dart';
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
""")

    # services
    write_f('lib/src/services/cron_parser.dart', """class CronParser {
  // Simple cron parser: supports "@every Xs" or "@every Xm"
  static Duration? parseSimple(String cronExpr) {
    final trimmed = cronExpr.trim().toLowerCase();
    if (trimmed.startsWith('@every ')) {
      final spec = trimmed.substring(7).trim();
      if (spec.endsWith('s')) {
        final sec = int.tryParse(spec.replaceAll('s', ''));
        if (sec != null) return Duration(seconds: sec);
      } else if (spec.endsWith('m')) {
        final min = int.tryParse(spec.replaceAll('m', ''));
        if (min != null) return Duration(minutes: min);
      } else if (spec.endsWith('h')) {
        final hr = int.tryParse(spec.replaceAll('h', ''));
        if (hr != null) return Duration(hours: hr);
      }
    }
    return null;
  }
}
""")

    write_f('lib/src/services/retry_manager.dart', """import 'dart:math';

class RetryManager {
  static Duration calculateBackoff(int retryAttempt, {Duration baseDelay = const Duration(seconds: 1)}) {
    final factor = pow(2, retryAttempt).toInt();
    return baseDelay * factor;
  }
}
""")

    write_f('lib/src/services/task_executor.dart', """import 'dart:async';
import '../models/execution_log.dart';
import '../models/scheduled_task.dart';
import '../models/task_status.dart';

typedef TaskActionHandler = FutureOr<void> Function(Map<String, dynamic> payload);

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
""")

    write_f('lib/src/services/worker_pool.dart', """import 'dart:async';
import '../models/scheduled_task.dart';
import 'task_executor.dart';

class WorkerPool {
  final int maxConcurrent;
  final TaskExecutor executor;
  int _activeWorkers = 0;

  WorkerPool({required this.executor, this.maxConcurrent = 2});

  int get availableSlots => maxConcurrent - _activeWorkers;
  bool get hasCapacity => _activeWorkers < maxConcurrent;

  Future<void> runTask(ScheduledTask task, void Function(ScheduledTask t, bool success) onDone) async {
    _activeWorkers++;
    try {
      final log = await executor.execute(task);
      onDone(task, log.isSuccess);
    } finally {
      _activeWorkers--;
    }
  }
}
""")

    write_f('lib/src/services/scheduler_service.dart', """import '../models/scheduled_task.dart';
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
""")

    # config
    write_f('lib/src/config/scheduler_config.dart', """class SchedulerConfig {
  final int maxConcurrentWorkers;
  final Duration tickInterval;

  const SchedulerConfig({
    this.maxConcurrentWorkers = 4,
    this.tickInterval = const Duration(seconds: 1),
  });
}
""")

    # application
    write_f('lib/src/application/scheduler_app.dart', """import '../config/scheduler_config.dart';
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
""")

    # lib export
    write_f('lib/task_scheduler.dart', """export 'src/models/scheduled_task.dart';
export 'src/models/task_status.dart';
export 'src/models/task_priority.dart';
export 'src/models/execution_log.dart';
export 'src/models/scheduler_metrics.dart';
export 'src/exceptions/scheduler_exception.dart';
export 'src/repositories/task_repository.dart';
export 'src/services/cron_parser.dart';
export 'src/services/retry_manager.dart';
export 'src/services/task_executor.dart';
export 'src/services/worker_pool.dart';
export 'src/services/scheduler_service.dart';
export 'src/validators/task_validator.dart';
export 'src/utils/time_utils.dart';
export 'src/config/scheduler_config.dart';
export 'src/application/scheduler_app.dart';
""")

    # bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
import 'package:task_scheduler/task_scheduler.dart';

void main(List<String> args) async {
  stdout.writeln('==============================================');
  stdout.writeln('         08. TASK SCHEDULER CLI               ');
  stdout.writeln('==============================================');

  final app = SchedulerApp.create();

  // Register worker actions
  app.registerAction('send_email', (payload) {
    stdout.writeln('  [WORKER] Sending email to: ${payload['email']}');
  });

  app.registerAction('generate_report', (payload) {
    stdout.writeln('  [WORKER] Generating analytics report for: ${payload['reportName']}');
  });

  // Schedule tasks
  app.addTask(
    'Welcome Email',
    'send_email',
    priority: TaskPriority.urgent,
    payload: {'email': 'user@example.com'},
  );

  app.addTask(
    'Daily Report',
    'generate_report',
    priority: TaskPriority.medium,
    repeatInterval: const Duration(hours: 24),
    payload: {'reportName': 'Daily Sales Summary'},
  );

  stdout.writeln('Initial Metrics: ${app.getMetrics()}\\n');
  stdout.writeln('Executing pending tasks...');
  final count = await app.executePending();
  stdout.writeln('Dispatched $count tasks.');

  stdout.writeln('\\nUpdated Metrics: ${app.getMetrics()}');
  stdout.writeln('==============================================');
}
""")

    # test/unit
    write_f('test/unit/scheduler_unit_test.dart', """import 'package:test/test.dart';
import 'package:task_scheduler/task_scheduler.dart';

void main() {
  group('Scheduler Unit Tests', () {
    test('TaskPriority weight comparison', () {
      expect(TaskPriority.urgent.weight, greaterThan(TaskPriority.high.weight));
      expect(TaskPriority.high.weight, greaterThan(TaskPriority.medium.weight));
      expect(TaskPriority.medium.weight, greaterThan(TaskPriority.low.weight));
    });

    test('RetryManager calculates exponential backoff', () {
      final delay1 = RetryManager.calculateBackoff(1, baseDelay: const Duration(seconds: 1));
      final delay2 = RetryManager.calculateBackoff(2, baseDelay: const Duration(seconds: 1));
      final delay3 = RetryManager.calculateBackoff(3, baseDelay: const Duration(seconds: 1));

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
""")

    # test/integration
    write_f('test/integration/scheduler_integration_test.dart', """import 'package:test/test.dart';
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
      app.addTask('Urgent Task', 'action_urgent', priority: TaskPriority.urgent);

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
""")

    print("Project 08 (Task Scheduler) generated successfully with 22 Dart files!")

if __name__ == '__main__':
    generate_p08('dart-project-lab')
