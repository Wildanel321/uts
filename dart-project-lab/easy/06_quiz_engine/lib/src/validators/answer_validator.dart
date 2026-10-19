import '../exceptions/quiz_exception.dart';
import '../models/question.dart';
import '../models/question_type.dart';

class AnswerValidator {
  static void validateSubmission(Question question, List<String> answers) {
    if (answers.isEmpty) {
      throw QuizException('Submission must contain at least one answer.');
    }

    if (question.type == QuestionType.multipleChoice && answers.length > 1) {
      throw QuizException(
          'Multiple choice questions only accept a single answer.');
    }

    if (question.type == QuestionType.trueFalse) {
      final ans = answers.first.toLowerCase();
      if (ans != 'true' && ans != 'false') {
        throw QuizException('True/False questions must be "true" or "false".');
      }
    }
  }
}
