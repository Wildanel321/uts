import '../config/quiz_config.dart';
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
    final result = quizService.evaluateSession(session,
        passingThreshold: config.passingScorePercentage);
    leaderboardService.recordScore(
        username, result.totalScore, result.percentage);
    return result;
  }
}
