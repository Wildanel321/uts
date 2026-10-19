import 'dart:io';
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
    stdout.writeln(
        '  [WORKER] Generating analytics report for: ${payload['reportName']}');
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

  stdout.writeln('Initial Metrics: ${app.getMetrics()}\n');
  stdout.writeln('Executing pending tasks...');
  final count = await app.executePending();
  stdout.writeln('Dispatched $count tasks.');

  stdout.writeln('\nUpdated Metrics: ${app.getMetrics()}');
  stdout.writeln('==============================================');
}
