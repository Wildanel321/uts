class SchedulerMetrics {
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
  String toString() =>
      'Total: $totalTasks | Pending: $pendingCount | Done: $completedCount | Failed: $failedCount';
}
