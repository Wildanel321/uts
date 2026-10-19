class QuizException implements Exception {
  final String message;
  QuizException(this.message);

  @override
  String toString() => 'QuizException: $message';
}
