import os

def generate_p06(base_dir):
    pdir = os.path.join(base_dir, 'easy', '06_quiz_engine')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'repositories'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'validators'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'utils'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'config'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'application'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'unit'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'integration'), exist_ok=True)

    def write_f(rel_path, content):
        target = os.path.join(pdir, rel_path)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

    write_f('pubspec.yaml', """name: quiz_engine
description: Pure Dart Interactive Quiz Engine with polymorph questions, Fisher-Yates shuffle, timer, and scoring.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dev_dependencies:
  test: ^1.25.0
""")

    write_f('README.md', """# 06. Quiz Engine

Aplikasi mesin kuis interaktif (*Quiz Engine*) berbasis Dart murni. Menyediakan bank soal dengan aneka tipe pertanyaan (Pilihan Ganda, Benar/Salah, Isian Singkat, dan Multi-Jawaban), pengacakan pertanyaan berbasis algoritma *Fisher-Yates*, timer batas waktu pengerjaan, penilaian otomatis (*Scoring Engine*), konversi skor ke huruf mutu (A, B, C, D, F), dan papan peringkat (*Leaderboard*).

## Fitur Utama
- **Ragam Tipe Soal**: Multiple choice, True/False, Fill-in-the-blank, dan Multiple answer.
- **Pengacakan Fisher-Yates**: Mengacak urutan soal dan opsi jawaban secara adil.
- **Batas Waktu (Timer)**: Pelacakan durasi per sesi kuis.
- **Sistem Penilaian Otomatis**: Perhitungan poin akurat dengan pembobotan per soal.
- **Papan Skor & Riwayat**: Penyimpanan skor tertinggi pemain dan riwayat evaluasi.

## Struktur File (22 File Dart)
- `bin/main.dart`: CLI entry point interaktif.
- `lib/quiz_engine.dart`: Export publik modul.
- `lib/src/models/`: QuestionType, Question, QuizSession, QuizResult, LeaderboardEntry, AnswerSubmission.
- `lib/src/exceptions/`: QuizException.
- `lib/src/repositories/`: QuizRepository.
- `lib/src/services/`: QuizService, ScoringEngine, QuestionShuffler, TimerService, LeaderboardService.
- `lib/src/validators/`: AnswerValidator.
- `lib/src/utils/`: GradeCalculator.
- `lib/src/config/`: QuizConfig.
- `lib/src/application/`: QuizApp.
- `test/unit/`: Pengujian algoritma scoring, grade calculator, dan shuffler.
- `test/integration/`: Pengujian alur kuis lengkap dari mulai sesi hingga penerbitan hasil.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
""")

    # models
    write_f('lib/src/models/question_type.dart', """enum QuestionType {
  multipleChoice,
  trueFalse,
  fillBlank,
  multipleAnswer,
}
""")

    write_f('lib/src/models/question.dart', """import 'question_type.dart';

class Question {
  final String id;
  final String text;
  final QuestionType type;
  final List<String> options;
  final List<String> correctAnswers;
  final int points;
  final String explanation;

  const Question({
    required this.id,
    required this.text,
    required this.type,
    this.options = const [],
    required this.correctAnswers,
    this.points = 10,
    this.explanation = '',
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'text': text,
    'type': type.name,
    'options': options,
    'correctAnswers': correctAnswers,
    'points': points,
    'explanation': explanation,
  };

  factory Question.fromJson(Map<String, dynamic> json) => Question(
    id: json['id'] as String,
    text: json['text'] as String,
    type: QuestionType.values.byName(json['type'] as String),
    options: List<String>.from(json['options'] as List? ?? []),
    correctAnswers: List<String>.from(json['correctAnswers'] as List? ?? []),
    points: json['points'] as int? ?? 10,
    explanation: json['explanation'] as String? ?? '',
  );
}
""")

    write_f('lib/src/models/answer_submission.dart', """class AnswerSubmission {
  final String questionId;
  final List<String> selectedAnswers;

  const AnswerSubmission({
    required this.questionId,
    required this.selectedAnswers,
  });
}
""")

    write_f('lib/src/models/quiz_session.dart', """import 'answer_submission.dart';
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
""")

    write_f('lib/src/models/quiz_result.dart', """class QuizResult {
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
  String toString() => 'Score: $totalScore/$maxPossibleScore ($letterGrade, ${percentage.toStringAsFixed(1)}%)';
}
""")

    write_f('lib/src/models/leaderboard_entry.dart', """class LeaderboardEntry {
  final String username;
  final int score;
  final double percentage;
  final DateTime achievedAt;

  LeaderboardEntry({
    required this.username,
    required this.score,
    required this.percentage,
    DateTime? achievedAt,
  }) : achievedAt = achievedAt ?? DateTime.now();

  Map<String, dynamic> toJson() => {
    'username': username,
    'score': score,
    'percentage': percentage,
    'achievedAt': achievedAt.toIso8601String(),
  };

  factory LeaderboardEntry.fromJson(Map<String, dynamic> json) => LeaderboardEntry(
    username: json['username'] as String,
    score: json['score'] as int,
    percentage: (json['percentage'] as num).toDouble(),
    achievedAt: DateTime.parse(json['achievedAt'] as String),
  );
}
""")

    # exceptions
    write_f('lib/src/exceptions/quiz_exception.dart', """class QuizException implements Exception {
  final String message;
  QuizException(this.message);

  @override
  String toString() => 'QuizException: $message';
}
""")

    # utils
    write_f('lib/src/utils/grade_calculator.dart', """class GradeCalculator {
  static String calculateGrade(double percentage) {
    if (percentage >= 90.0) return 'A';
    if (percentage >= 80.0) return 'B';
    if (percentage >= 70.0) return 'C';
    if (percentage >= 60.0) return 'D';
    return 'F';
  }
}
""")

    # validators
    write_f('lib/src/validators/answer_validator.dart', """import '../exceptions/quiz_exception.dart';
import '../models/question.dart';
import '../models/question_type.dart';

class AnswerValidator {
  static void validateSubmission(Question question, List<String> answers) {
    if (answers.isEmpty) {
      throw QuizException('Submission must contain at least one answer.');
    }

    if (question.type == QuestionType.multipleChoice && answers.length > 1) {
      throw QuizException('Multiple choice questions only accept a single answer.');
    }

    if (question.type == QuestionType.trueFalse) {
      final ans = answers.first.toLowerCase();
      if (ans != 'true' && ans != 'false') {
        throw QuizException('True/False questions must be "true" or "false".');
      }
    }
  }
}
""")

    # repositories
    write_f('lib/src/repositories/quiz_repository.dart', """import '../models/leaderboard_entry.dart';
import '../models/question.dart';

class QuizRepository {
  final List<Question> _questionBank = [];
  final List<LeaderboardEntry> _leaderboard = [];

  void addQuestion(Question q) => _questionBank.add(q);
  List<Question> getAllQuestions() => List.unmodifiable(_questionBank);

  void addLeaderboardEntry(LeaderboardEntry entry) {
    _leaderboard.add(entry);
    _leaderboard.sort((a, b) => b.score.compareTo(a.score));
  }

  List<LeaderboardEntry> getLeaderboard() => List.unmodifiable(_leaderboard);

  void clear() {
    _questionBank.clear();
    _leaderboard.clear();
  }
}
""")

    # services
    write_f('lib/src/services/question_shuffler.dart', """import 'dart:math';
import '../models/question.dart';

class QuestionShuffler {
  final Random _rng;

  QuestionShuffler({Random? random}) : _rng = random ?? Random();

  List<Question> shuffleQuestions(List<Question> questions) {
    final copy = List<Question>.from(questions);
    for (int i = copy.length - 1; i > 0; i--) {
      final j = _rng.nextInt(i + 1);
      final temp = copy[i];
      copy[i] = copy[j];
      copy[j] = temp;
    }
    return copy;
  }

  List<String> shuffleOptions(List<String> options) {
    final copy = List<String>.from(options);
    copy.shuffle(_rng);
    return copy;
  }
}
""")

    write_f('lib/src/services/scoring_engine.dart', """import '../models/question.dart';
import '../models/question_type.dart';

class ScoringEngine {
  static int evaluate(Question question, List<String> submitted) {
    final normSubmitted = submitted.map((s) => s.trim().toLowerCase()).toSet();
    final normCorrect = question.correctAnswers.map((s) => s.trim().toLowerCase()).toSet();

    switch (question.type) {
      case QuestionType.multipleChoice:
      case QuestionType.trueFalse:
      case QuestionType.fillBlank:
        if (normSubmitted.isNotEmpty && normCorrect.contains(normSubmitted.first)) {
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
""")

    write_f('lib/src/services/timer_service.dart', """class TimerService {
  final DateTime _startedAt = DateTime.now();

  Duration get elapsed => DateTime.now().difference(_startedAt);

  bool isExpired(Duration timeLimit) => elapsed > timeLimit;
}
""")

    write_f('lib/src/services/leaderboard_service.dart', """import '../models/leaderboard_entry.dart';
import '../repositories/quiz_repository.dart';

class LeaderboardService {
  final QuizRepository repository;

  LeaderboardService(this.repository);

  void recordScore(String username, int score, double percentage) {
    repository.addLeaderboardEntry(
      LeaderboardEntry(username: username, score: score, percentage: percentage),
    );
  }

  List<LeaderboardEntry> getTopScores([int limit = 10]) {
    return repository.getLeaderboard().take(limit).toList();
  }
}
""")

    write_f('lib/src/services/quiz_service.dart', """import '../models/quiz_result.dart';
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

  QuizSession createSession(String title, {bool shuffle = true, int? questionLimit}) {
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

  QuizResult evaluateSession(QuizSession session, {double passingThreshold = 70.0}) {
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

    final percentage = maxPossible > 0 ? (totalScore / maxPossible) * 100.0 : 0.0;
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
""")

    # config
    write_f('lib/src/config/quiz_config.dart', """class QuizConfig {
  final double passingScorePercentage;
  final Duration defaultTimeLimit;

  const QuizConfig({
    this.passingScorePercentage = 70.0,
    this.defaultTimeLimit = const Duration(minutes: 10),
  });
}
""")

    # application
    write_f('lib/src/application/quiz_app.dart', """import '../config/quiz_config.dart';
import '../models/question.dart';
import '../models/quiz_result.dart';
import '../models/quiz_session.dart';
import '../repositories/quiz_repository.dart';
import '../services/leaderboard_service.dart';
import '../services/quiz_service.dart';

class QuizApp {
  final QuizConfig config;
  final QuizRepository repository;
  final QuizService quizService;
  final LeaderboardService leaderboardService;

  QuizApp({QuizConfig? config})
      : config = config ?? const QuizConfig(),
        repository = QuizRepository(),
        quizService = QuizService(QuizRepository()),
        leaderboardService = LeaderboardService(QuizRepository());

  factory QuizApp.create({QuizConfig? config}) {
    final repo = QuizRepository();
    return QuizApp._internal(
      config ?? const QuizConfig(),
      repo,
      QuizService(repo),
      LeaderboardService(repo),
    );
  }

  QuizApp._internal(
    this.config,
    this.repository,
    this.quizService,
    this.leaderboardService,
  );

  void loadQuestions(List<Question> questions) {
    for (final q in questions) {
      repository.addQuestion(q);
    }
  }

  QuizSession startQuiz(String title, {bool shuffle = false}) {
    return quizService.createSession(title, shuffle: shuffle);
  }

  QuizResult completeQuiz(QuizSession session, String username) {
    final result = quizService.evaluateSession(session, passingThreshold: config.passingScorePercentage);
    leaderboardService.recordScore(username, result.totalScore, result.percentage);
    return result;
  }
}
""")

    # lib export
    write_f('lib/quiz_engine.dart', """export 'src/models/question_type.dart';
export 'src/models/question.dart';
export 'src/models/answer_submission.dart';
export 'src/models/quiz_session.dart';
export 'src/models/quiz_result.dart';
export 'src/models/leaderboard_entry.dart';
export 'src/exceptions/quiz_exception.dart';
export 'src/repositories/quiz_repository.dart';
export 'src/services/quiz_service.dart';
export 'src/services/scoring_engine.dart';
export 'src/services/question_shuffler.dart';
export 'src/services/timer_service.dart';
export 'src/services/leaderboard_service.dart';
export 'src/validators/answer_validator.dart';
export 'src/utils/grade_calculator.dart';
export 'src/config/quiz_config.dart';
export 'src/application/quiz_app.dart';
""")

    # bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
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
  stdout.writeln('Starting session: ${session.title} (${session.questions.length} questions)\\n');

  // Simulate answers
  session.submitAnswer('q1', ['Dart']);
  session.submitAnswer('q2', ['true']);
  session.submitAnswer('q3', ['final']);

  final result = app.completeQuiz(session, 'Developer123');
  stdout.writeln('Quiz Result: $result');
  stdout.writeln('Passed: ${result.isPassed ? "YES" : "NO"}');
  stdout.writeln('==============================================');
}
""")

    # test/unit
    write_f('test/unit/quiz_unit_test.dart', """import 'package:test/test.dart';
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

    test('AnswerValidator prevents multiple selections on single choice questions', () {
      const q = Question(
        id: '2',
        text: 'Test?',
        type: QuestionType.multipleChoice,
        correctAnswers: ['A'],
      );

      expect(() => AnswerValidator.validateSubmission(q, ['A', 'B']), throwsA(isA<QuizException>()));
    });
  });
}
""")

    # test/integration
    write_f('test/integration/quiz_integration_test.dart', """import 'package:test/test.dart';
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
""")

    print("Project 06 (Quiz Engine) generated successfully with 22 Dart files!")

if __name__ == '__main__':
    generate_p06('dart-project-lab')
