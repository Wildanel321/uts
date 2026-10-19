import '../models/transaction.dart';
import '../models/transaction_type.dart';

class CsvParser {
  static String toCsv(List<Transaction> transactions) {
    final buffer = StringBuffer('id,title,amount,type,categoryId,date,note\n');
    for (final t in transactions) {
      final safeTitle = t.title.replaceAll(',', ' ');
      final safeNote = t.note.replaceAll(',', ' ');
      buffer.writeln(
          '${t.id},$safeTitle,${t.amount},${t.type.name},${t.categoryId},${t.date.toIso8601String()},$safeNote');
    }
    return buffer.toString();
  }

  static List<Transaction> fromCsv(String csv) {
    final lines = csv
        .split('\n')
        .map((l) => l.trim())
        .where((l) => l.isNotEmpty)
        .toList();
    if (lines.isEmpty) return [];

    final list = <Transaction>[];
    for (int i = 1; i < lines.length; i++) {
      final cols = lines[i].split(',');
      if (cols.length >= 6) {
        list.add(Transaction(
          id: cols[0],
          title: cols[1],
          amount: double.tryParse(cols[2]) ?? 0.0,
          type: TransactionType.values.byName(cols[3]),
          categoryId: cols[4],
          date: DateTime.parse(cols[5]),
          note: cols.length > 6 ? cols[6] : '',
        ));
      }
    }
    return list;
  }
}
