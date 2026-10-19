import '../models/leaderboard_entry.dart';
import '../repositories/quiz_repository.dart';

class LeaderboardService {
  final QuizRepository repository;

  LeaderboardService(this.repository);

  void recordScore(String username, int score, double percentage) {
    repository.addLeaderboardEntry(
      LeaderboardEntry(
          username: username, score: score, percentage: percentage),
    );
  }

  List<LeaderboardEntry> getTopScores([int limit = 10]) {
    return repository.getLeaderboard().take(limit).toList();
  }
}
