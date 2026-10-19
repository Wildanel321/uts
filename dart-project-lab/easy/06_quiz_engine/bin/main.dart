import 'dart:io';
import 'package:quiz_engine/quiz_engine.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('          06. QUIZ ENGINE CLI                 ');
  stdout.writeln('==============================================');

  final app = QuizApp.create();

  // Load sample questions
  app.loadQuestions([
    const Question(
      id: 'q1',
      text: 'What is the main language used in Pure Dart projects?',
      type: QuestionType.multipleChoice,
      options: ['Dart', 'Kotlin', 'Java', 'Python'],
      correctAnswers: ['Dart'],
      points: 10,
    ),
    const Question(
      id: 'q2',
      text: 'Dart supports sound null safety.',
      type: QuestionType.trueFalse,
      options: ['true', 'false'],
      correctAnswers: ['true'],
      points: 10,
    ),
    const Question(
      id: 'q3',
      text: 'What keyword defines an immutable variable assigned at runtime?',
      type: QuestionType.fillBlank,
      correctAnswers: ['final'],
      points: 10,
    ),
  ]);

  final session = app.startQuiz('Dart Fundamentals Quiz');
  stdout.writeln(
      'Starting session: ${session.title} (${session.questions.length} questions)\n');

  // Simulate answers
  session.submitAnswer('q1', ['Dart']);
  session.submitAnswer('q2', ['true']);
  session.submitAnswer('q3', ['final']);

  final result = app.completeQuiz(session, 'Developer123');
  stdout.writeln('Quiz Result: $result');
  stdout.writeln('Passed: ${result.isPassed ? "YES" : "NO"}');
  stdout.writeln('==============================================');
}
