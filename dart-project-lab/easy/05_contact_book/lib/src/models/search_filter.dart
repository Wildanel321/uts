class SearchFilter {
  final String? query;
  final String? group;
  final bool onlyFavorites;

  const SearchFilter({
    this.query,
    this.group,
    this.onlyFavorites = false,
  });
}
