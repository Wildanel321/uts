class ExecutionLog {
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
  String toString() =>
      '[$executedAt] Task $taskId: ${isSuccess ? "SUCCESS" : "FAILED ($errorMessage)"} (${durationMs}ms)';
}
