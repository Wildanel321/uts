import '../models/calculation_history.dart';

class HistoryService {
  final List<HistoryEntry> _entries = [];
  final int maxHistory;

  HistoryService({this.maxHistory = 50});

  void add(String expression, double result) {
    _entries.add(HistoryEntry(expression: expression, result: result));
    if (_entries.length > maxHistory) {
      _entries.removeAt(0);
    }
  }

  List<HistoryEntry> getAll() => List.unmodifiable(_entries);

  HistoryEntry? getLast() => _entries.isEmpty ? null : _entries.last;

  HistoryEntry? undo() {
    if (_entries.isNotEmpty) {
      return _entries.removeLast();
    }
    return null;
  }

  void clear() => _entries.clear();
}
