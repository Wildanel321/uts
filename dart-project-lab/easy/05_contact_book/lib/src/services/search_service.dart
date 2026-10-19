import '../models/contact.dart';
import '../models/search_filter.dart';
import '../repositories/contact_repository.dart';
import '../utils/string_similarity.dart';

class SearchService {
  final ContactRepository repository;

  SearchService(this.repository);

  List<Contact> search(SearchFilter filter) {
    var items = repository.getAll();

    if (filter.onlyFavorites) {
      items = items.where((c) => c.isFavorite).toList();
    }

    if (filter.group != null && filter.group!.isNotEmpty) {
      items = items
          .where((c) => c.group.toLowerCase() == filter.group!.toLowerCase())
          .toList();
    }

    if (filter.query != null && filter.query!.trim().isNotEmpty) {
      final q = filter.query!.trim();
      items = items.where((c) {
        final matchesName = StringSimilarity.isFuzzyMatch(c.name, q);
        final matchesPhone = c.phone.contains(q);
        final matchesEmail = c.email.toLowerCase().contains(q.toLowerCase());
        return matchesName || matchesPhone || matchesEmail;
      }).toList();
    }

    return items;
  }
}
