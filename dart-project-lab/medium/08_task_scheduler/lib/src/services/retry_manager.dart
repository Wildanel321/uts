import 'dart:math';

class RetryManager {
  static Duration calculateBackoff(int retryAttempt,
      {Duration baseDelay = const Duration(seconds: 1)}) {
    final factor = pow(2, retryAttempt).toInt();
    return baseDelay * factor;
  }
}
