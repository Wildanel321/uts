import 'package:test/test.dart';
import 'package:calculator_cli/calculator_cli.dart';

void main() {
  group('Arithmetic Service Tests', () {
    final arith = ArithmeticService();

    test('Basic addition and subtraction', () {
      expect(arith.add(10, 5), equals(15.0));
      expect(arith.subtract(10, 5), equals(5.0));
    });

    test('Multiplication and division', () {
      expect(arith.multiply(6, 7), equals(42.0));
      expect(arith.divide(100, 4), equals(25.0));
    });

    test('Division by zero throws MathDomainException', () {
      expect(() => arith.divide(10, 0), throwsA(isA<MathDomainException>()));
    });

    test('Power and modulo', () {
      expect(arith.power(2, 3), equals(8.0));
      expect(arith.modulo(10, 3), equals(1.0));
    });
  });

  group('Scientific Service Tests', () {
    final sciDegree = ScientificService(angleMode: AngleMode.degree);
    final sciRadian = ScientificService(angleMode: AngleMode.radian);

    test('Trigonometry in degrees', () {
      expect(sciDegree.sin(90), closeTo(1.0, 1e-9));
      expect(sciDegree.cos(0), closeTo(1.0, 1e-9));
      expect(sciDegree.tan(45), closeTo(1.0, 1e-9));
    });

    test('Trigonometry in radians', () {
      expect(sciRadian.sin(3.141592653589793 / 2), closeTo(1.0, 1e-9));
    });

    test('Square root and logs', () {
      expect(sciDegree.sqrt(16), equals(4.0));
      expect(() => sciDegree.sqrt(-4), throwsA(isA<MathDomainException>()));
      expect(sciDegree.log10(100), closeTo(2.0, 1e-9));
      expect(() => sciDegree.log10(0), throwsA(isA<MathDomainException>()));
    });

    test('Factorial', () {
      expect(sciDegree.factorial(5), equals(120.0));
      expect(sciDegree.factorial(0), equals(1.0));
      expect(
          () => sciDegree.factorial(-1), throwsA(isA<MathDomainException>()));
    });
  });

  group('Parser & Lexer Tests', () {
    test('Tokenizes complex expression', () {
      final lexer = Lexer('3 + 4 * 2 / ( 1 - 5 ) ^ 2');
      final tokens = lexer.tokenize();
      expect(
          tokens.map((t) => t.type),
          containsAllInOrder([
            TokenType.number,
            TokenType.plus,
            TokenType.number,
            TokenType.multiply,
            TokenType.number,
          ]));
    });

    test('Parenthesis validator detects mismatch', () {
      expect(() => InputValidator.validateParentheses('(3 + 4 * 2'),
          throwsA(isA<SyntaxException>()));
      expect(() => InputValidator.validateParentheses('3 + 4)'),
          throwsA(isA<SyntaxException>()));
    });
  });
}
