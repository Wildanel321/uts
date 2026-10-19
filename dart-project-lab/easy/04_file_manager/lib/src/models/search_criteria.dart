class SearchCriteria {
  final String? nameQuery;
  final String? extension;
  final int? minSizeBytes;
  final int? maxSizeBytes;
  final bool recursive;

  const SearchCriteria({
    this.nameQuery,
    this.extension,
    this.minSizeBytes,
    this.maxSizeBytes,
    this.recursive = true,
  });
}
