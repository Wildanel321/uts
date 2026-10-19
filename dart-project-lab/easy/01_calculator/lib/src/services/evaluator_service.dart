import '../models/token.dart';
import '../models/token_type.dart';
import '../exceptions/syntax_exception.dart';
import '../exceptions/calculator_exception.dart';
import 'arithmetic_service.dart';
import 'scientific_service.dart';

class EvaluatorService {
  final ArithmeticService arithmetic;
  final ScientificService scientific;

  EvaluatorService({
    required this.arithmetic,
    required this.scientific,
  });

  double evaluateRpn(List<Token> rpn) {
    if (rpn.isEmpty) {
      throw SyntaxException('No tokens to evaluate');
    }

    final stack = <double>[];

    for (final token in rpn) {
      if (token.type == TokenType.number) {
        stack.add(token.numberValue!);
      } else if (_isBinaryOp(token.type)) {
        if (stack.length < 2) {
          throw SyntaxException(
              'Insufficient operands for operator "${token.text}"');
        }
        final b = stack.removeLast();
        final a = stack.removeLast();
        stack.add(_applyBinaryOp(token.type, a, b));
      } else if (token.type == TokenType.identifier) {
        final func = token.text.toLowerCase();
        if (func == 'pi') {
          stack.add(3.141592653589793);
        } else if (func == 'e') {
          stack.add(2.718281828459045);
        } else {
          if (stack.isEmpty) {
            throw SyntaxException('Insufficient operands for function "$func"');
          }
          final arg = stack.removeLast();
          stack.add(_applyFunction(func, arg));
        }
      }
    }

    if (stack.length != 1) {
      throw SyntaxException(
          'Invalid expression structure: excess operands remain');
    }

    return stack.single;
  }

  bool _isBinaryOp(TokenType type) {
    return type == TokenType.plus ||
        type == TokenType.minus ||
        type == TokenType.multiply ||
        type == TokenType.divide ||
        type == TokenType.modulo ||
        type == TokenType.power;
  }

  double _applyBinaryOp(TokenType type, double a, double b) {
    switch (type) {
      case TokenType.plus:
        return arithmetic.add(a, b);
      case TokenType.minus:
        return arithmetic.subtract(a, b);
      case TokenType.multiply:
        return arithmetic.multiply(a, b);
      case TokenType.divide:
        return arithmetic.divide(a, b);
      case TokenType.modulo:
        return arithmetic.modulo(a, b);
      case TokenType.power:
        return arithmetic.power(a, b);
      default:
        throw CalculatorException('Unknown binary operator: $type');
    }
  }

  double _applyFunction(String func, double arg) {
    switch (func) {
      case 'sin':
        return scientific.sin(arg);
      case 'cos':
        return scientific.cos(arg);
      case 'tan':
        return scientific.tan(arg);
      case 'sqrt':
        return scientific.sqrt(arg);
      case 'log':
        return scientific.log10(arg);
      case 'ln':
        return scientific.ln(arg);
      case 'fact':
        return scientific.factorial(arg);
      default:
        throw SyntaxException('Unknown function identifier: "$func"');
    }
  }
}
