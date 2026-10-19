class ContactStats {
  final int totalContacts;
  final int favoriteCount;
  final Map<String, int> groupDistribution;

  const ContactStats({
    required this.totalContacts,
    required this.favoriteCount,
    required this.groupDistribution,
  });

  @override
  String toString() =>
      'Total: $totalContacts, Favorites: $favoriteCount, Groups: ${groupDistribution.length}';
}
