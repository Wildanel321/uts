import 'dart:convert';
import '../models/transaction.dart';

class JsonParser {
  static String toJsonString(List<Transaction> txs) {
    final list = txs.map((t) => t.toJson()).toList();
    return const JsonEncoder.withIndent('  ').convert(list);
  }

  static List<Transaction> fromJsonString(String jsonStr) {
    final decoded = jsonDecode(jsonStr) as List<dynamic>;
    return decoded
        .map((item) => Transaction.fromJson(item as Map<String, dynamic>))
        .toList();
  }
}
