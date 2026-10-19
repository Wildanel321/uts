class TimerService {
  final DateTime _startedAt = DateTime.now();

  Duration get elapsed => DateTime.now().difference(_startedAt);

  bool isExpired(Duration timeLimit) => elapsed > timeLimit;
}
