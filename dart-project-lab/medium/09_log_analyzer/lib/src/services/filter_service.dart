import '../models/filter_criteria.dart';
import '../models/log_entry.dart';

class FilterService {
  static bool matches(LogEntry entry, FilterCriteria criteria) {
    if (criteria.minLevel != null &&
        entry.level.index < criteria.minLevel!.index) {
      return false;
    }
    if (criteria.ip != null && entry.ip != criteria.ip) {
      return false;
    }
    if (criteria.statusCode != null &&
        entry.statusCode != criteria.statusCode) {
      return false;
    }
    if (criteria.query != null &&
        !entry.message.toLowerCase().contains(criteria.query!.toLowerCase())) {
      return false;
    }
    return true;
  }
}
