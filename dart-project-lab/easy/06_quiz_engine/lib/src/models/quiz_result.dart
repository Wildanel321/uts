class QuizResult {
  final String sessionId;
  final int totalScore;
  final int maxPossibleScore;
  final double percentage;
  final String letterGrade;
  final bool isPassed;
  final int correctCount;
  final int totalQuestions;

  QuizResult({
    required this.sessionId,
    required this.totalScore,
    required this.maxPossibleScore,
    required this.percentage,
    required this.letterGrade,
    required this.isPassed,
    required this.correctCount,
    required this.totalQuestions,
  });

  @override
  String toString() =>
      'Score: $totalScore/$maxPossibleScore ($letterGrade, ${percentage.toStringAsFixed(1)}%)';
}
