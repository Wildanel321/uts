import '../models/leaderboard_entry.dart';
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
