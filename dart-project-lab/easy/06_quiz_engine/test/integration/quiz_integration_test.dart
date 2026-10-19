import 'package:test/test.dart';
import 'package:quiz_engine/quiz_engine.dart';

void main() {
  group('Quiz Engine Integration Flow Tests', () {
    late QuizApp app;

    setUp(() {
      app = QuizApp.create();
      app.loadQuestions([
        const Question(
          id: 'q1',
          text: '2 + 2 = ?',
          type: QuestionType.multipleChoice,
          options: ['3', '4', '5'],
          correctAnswers: ['4'],
          points: 50,
        ),
        const Question(
          id: 'q2',
          text: 'Dart is object-oriented.',
          type: QuestionType.trueFalse,
          options: ['true', 'false'],
          correctAnswers: ['true'],
          points: 50,
        ),
      ]);
    });

    test('Runs quiz session and scores 100% on correct submissions', () {
      final session = app.startQuiz('Math and Dart');
      session.submitAnswer('q1', ['4']);
      session.submitAnswer('q2', ['true']);

      final result = app.completeQuiz(session, 'Alice');
      expect(result.totalScore, equals(100));
      expect(result.percentage, equals(100.0));
      expect(result.letterGrade, equals('A'));
      expect(result.isPassed, isTrue);

      final top = app.leaderboardService.getTopScores();
      expect(top.length, equals(1));
      expect(top.first.username, equals('Alice'));
      expect(top.first.score, equals(100));
    });
  });
}
