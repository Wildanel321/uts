class QuizConfig {
  final double passingScorePercentage;
  final Duration defaultTimeLimit;

  const QuizConfig({
    this.passingScorePercentage = 70.0,
    this.defaultTimeLimit = const Duration(minutes: 10),
  });
}
