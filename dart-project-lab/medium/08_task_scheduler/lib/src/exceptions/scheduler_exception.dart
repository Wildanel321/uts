class SchedulerException implements Exception {
  final String message;
  SchedulerException(this.message);

  @override
  String toString() => 'SchedulerException: $message';
}
