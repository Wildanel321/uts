import 'answer_submission.dart';
import 'question.dart';

class QuizSession {
  final String id;
  final String title;
  final List<Question> questions;
  final Map<String, AnswerSubmission> submissions = {};
  final DateTime startedAt;
  DateTime? endedAt;

  QuizSession({
    required this.id,
    required this.title,
    required this.questions,
    DateTime? startedAt,
  }) : startedAt = startedAt ?? DateTime.now();

  void submitAnswer(String questionId, List<String> answers) {
    submissions[questionId] = AnswerSubmission(
      questionId: questionId,
      selectedAnswers: answers,
    );
  }

  void finish() {
    endedAt = DateTime.now();
  }
}
