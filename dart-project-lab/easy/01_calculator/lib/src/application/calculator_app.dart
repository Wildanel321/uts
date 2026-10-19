import '../config/calculator_config.dart';
import '../models/calculation_history.dart';
import '../parsers/expression_parser.dart';
import '../services/arithmetic_service.dart';
import '../services/evaluator_service.dart';
import '../services/history_service.dart';
import '../services/scientific_service.dart';
import '../utils/number_formatter.dart';

class CalculatorApp {
  final CalculatorConfig config;
  final ExpressionParser parser;
  final ArithmeticService arithmetic;
  final ScientificService scientific;
  final EvaluatorService evaluator;
  final HistoryService history;

  CalculatorApp({CalculatorConfig? config})
      : config = config ?? const CalculatorConfig(),
        parser = ExpressionParser(),
        arithmetic = ArithmeticService(),
        scientific = ScientificService(
            angleMode: (config ?? const CalculatorConfig()).angleMode),
        history = HistoryService(),
        evaluator = EvaluatorService(
          arithmetic: ArithmeticService(),
          scientific: ScientificService(
              angleMode: (config ?? const CalculatorConfig()).angleMode),
        );

  String execute(String input) {
    final trimmed = input.trim();
    if (trimmed.isEmpty) return '';

    if (trimmed == 'history') {
      final entries = history.getAll();
      if (entries.isEmpty) return 'No calculation history available.';
      final buffer = StringBuffer('Calculation History:\n');
      for (int i = 0; i < entries.length; i++) {
        buffer.writeln(
            '  [${i + 1}] ${entries[i].expression} = ${NumberFormatter.format(entries[i].result, precision: config.precision)}');
      }
      return buffer.toString().trimRight();
    }

    if (trimmed == 'clear') {
      history.clear();
      return 'History cleared successfully.';
    }

    if (trimmed == 'undo') {
      final undone = history.undo();
      if (undone == null) return 'No history to undo.';
      return 'Undone last calculation: ${undone.expression} = ${undone.result}';
    }

    final rpn = parser.parse(trimmed);
    final result = evaluator.evaluateRpn(rpn);

    if (config.storeHistory) {
      history.add(trimmed, result);
    }

    return NumberFormatter.format(result, precision: config.precision);
  }

  List<HistoryEntry> getHistory() => history.getAll();
}
