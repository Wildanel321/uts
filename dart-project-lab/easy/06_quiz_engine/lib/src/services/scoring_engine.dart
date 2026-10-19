import '../models/question.dart';
import '../models/question_type.dart';

class ScoringEngine {
  static int evaluate(Question question, List<String> submitted) {
    final normSubmitted = submitted.map((s) => s.trim().toLowerCase()).toSet();
    final normCorrect =
        question.correctAnswers.map((s) => s.trim().toLowerCase()).toSet();

    switch (question.type) {
      case QuestionType.multipleChoice:
      case QuestionType.trueFalse:
      case QuestionType.fillBlank:
        if (normSubmitted.isNotEmpty &&
            normCorrect.contains(normSubmitted.first)) {
          return question.points;
        }
        return 0;

      case QuestionType.multipleAnswer:
        if (normSubmitted.isEmpty) return 0;
        int matched = 0;
        for (final ans in normSubmitted) {
          if (normCorrect.contains(ans)) {
            matched++;
          } else {
            matched--; // penalty for wrong checkbox
          }
        }
        if (matched <= 0) return 0;
        final score = (matched / normCorrect.length) * question.points;
        return score.round();
    }
  }
}
