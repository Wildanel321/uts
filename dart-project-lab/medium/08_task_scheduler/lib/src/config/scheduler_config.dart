class SchedulerConfig {
  final int maxConcurrentWorkers;
  final Duration tickInterval;

  const SchedulerConfig({
    this.maxConcurrentWorkers = 4,
    this.tickInterval = const Duration(seconds: 1),
  });
}
