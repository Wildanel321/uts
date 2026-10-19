import 'package:test/test.dart';
import 'package:calculator_cli/calculator_cli.dart';

void main() {
  group('Calculator App End-to-End Integration Tests', () {
    late CalculatorApp app;

    setUp(() {
      app = CalculatorApp(
          config: const CalculatorConfig(angleMode: AngleMode.degree));
    });

    test('Calculates standard arithmetic precedence', () {
      expect(app.execute('2 + 3 * 4'), equals('14'));
      expect(app.execute('(2 + 3) * 4'), equals('20'));
      expect(app.execute('2 ^ 3 + 1'), equals('9'));
    });

    test('Evaluates scientific functions', () {
      expect(app.execute('sqrt(25) + 5'), equals('10'));
      expect(app.execute('sin(90) * 10'), equals('10'));
      expect(app.execute('fact(4)'), equals('24'));
    });

    test('Evaluates expressions with constants', () {
      final res = double.parse(app.execute('pi * 2'));
      expect(res, closeTo(6.2831853, 1e-4));
    });

    test('Handles history and undo functionality', () {
      app.execute('10 + 20');
      app.execute('50 - 5');
      expect(app.getHistory().length, equals(2));

      final histStr = app.execute('history');
      expect(histStr, contains('10 + 20 = 30'));
      expect(histStr, contains('50 - 5 = 45'));

      app.execute('undo');
      expect(app.getHistory().length, equals(1));

      app.execute('clear');
      expect(app.getHistory().length, equals(0));
    });
  });
}
