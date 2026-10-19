import '../models/quiz_result.dart';
import '../models/quiz_session.dart';
import '../repositories/quiz_repository.dart';
import '../utils/grade_calculator.dart';
import '../validators/answer_validator.dart';
import 'question_shuffler.dart';
import 'scoring_engine.dart';

class QuizService {
  final QuizRepository repository;
  final QuestionShuffler shuffler;
  static int _idCounter = 0;

  QuizService(this.repository, {QuestionShuffler? shuffler})
      : shuffler = shuffler ?? QuestionShuffler();

  QuizSession createSession(String title,
      {bool shuffle = true, int? questionLimit}) {
    var questions = repository.getAllQuestions();
    if (shuffle) {
      questions = shuffler.shuffleQuestions(questions);
    }
    if (questionLimit != null && questions.length > questionLimit) {
      questions = questions.take(questionLimit).toList();
    }

    return QuizSession(
      id: 'qs_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}',
      title: title,
      questions: questions,
    );
  }

  QuizResult evaluateSession(QuizSession session,
      {double passingThreshold = 70.0}) {
    session.finish();
    int totalScore = 0;
    int maxPossible = 0;
    int correctCount = 0;

    for (final q in session.questions) {
      maxPossible += q.points;
      final sub = session.submissions[q.id];
      if (sub != null) {
        AnswerValidator.validateSubmission(q, sub.selectedAnswers);
        final score = ScoringEngine.evaluate(q, sub.selectedAnswers);
        totalScore += score;
        if (score == q.points) {
          correctCount++;
        }
      }
    }

    final percentage =
        maxPossible > 0 ? (totalScore / maxPossible) * 100.0 : 0.0;
    final grade = GradeCalculator.calculateGrade(percentage);
    final isPassed = percentage >= passingThreshold;

    return QuizResult(
      sessionId: session.id,
      totalScore: totalScore,
      maxPossibleScore: maxPossible,
      percentage: percentage,
      letterGrade: grade,
      isPassed: isPassed,
      correctCount: correctCount,
      totalQuestions: session.questions.length,
    );
  }
}
