import 'log_level.dart';

class FilterCriteria {
  final LogLevel? minLevel;
  final String? query;
  final String? ip;
  final int? statusCode;

  const FilterCriteria({
    this.minLevel,
    this.query,
    this.ip,
    this.statusCode,
  });
}
