class LeaderboardEntry {
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

  factory LeaderboardEntry.fromJson(Map<String, dynamic> json) =>
      LeaderboardEntry(
        username: json['username'] as String,
        score: json['score'] as int,
        percentage: (json['percentage'] as num).toDouble(),
        achievedAt: DateTime.parse(json['achievedAt'] as String),
      );
}
