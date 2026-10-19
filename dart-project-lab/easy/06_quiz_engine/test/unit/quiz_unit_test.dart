import 'package:test/test.dart';
import 'package:quiz_engine/quiz_engine.dart';

void main() {
  group('Quiz Engine Unit Tests', () {
    test('GradeCalculator computes correct letter grades', () {
      expect(GradeCalculator.calculateGrade(95.0), equals('A'));
      expect(GradeCalculator.calculateGrade(82.5), equals('B'));
      expect(GradeCalculator.calculateGrade(71.0), equals('C'));
      expect(GradeCalculator.calculateGrade(65.0), equals('D'));
      expect(GradeCalculator.calculateGrade(40.0), equals('F'));
    });

    test('ScoringEngine evaluates multiple choice correctly', () {
      const q = Question(
        id: '1',
        text: 'Capital of France?',
        type: QuestionType.multipleChoice,
        options: ['Paris', 'London'],
        correctAnswers: ['Paris'],
        points: 20,
      );

      expect(ScoringEngine.evaluate(q, ['Paris']), equals(20));
      expect(ScoringEngine.evaluate(q, ['London']), equals(0));
    });

    test(
        'AnswerValidator prevents multiple selections on single choice questions',
        () {
      const q = Question(
        id: '2',
        text: 'Test?',
        type: QuestionType.multipleChoice,
        correctAnswers: ['A'],
      );

      expect(() => AnswerValidator.validateSubmission(q, ['A', 'B']),
          throwsA(isA<QuizException>()));
    });
  });
}
