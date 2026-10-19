import os

def generate_p01(base_dir):
    pdir = os.path.join(base_dir, 'easy', '01_calculator')
    os.makedirs(os.path.join(pdir, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'models'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'exceptions'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'parsers'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'services'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'validators'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'utils'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'config'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'lib', 'src', 'application'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'unit'), exist_ok=True)
    os.makedirs(os.path.join(pdir, 'test', 'integration'), exist_ok=True)

    def write_f(rel_path, content):
        target = os.path.join(pdir, rel_path)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

    # 1. pubspec.yaml
    write_f('pubspec.yaml', """name: calculator_cli
description: Modular pure Dart scientific calculator CLI and expression evaluator.
version: 1.0.0
environment:
  sdk: '>=3.0.0 <4.0.0'

dev_dependencies:
  test: ^1.25.0
""")

    # 2. README.md
    write_f('README.md', """# 01. Calculator CLI

Aplikasi kalkulator baris perintah (*CLI*) berbasis Dart murni yang dilengkapi mesin evaluasi ekspresi matematika Shunting-yard, perhitungan fungsi ilmiah, riwayat kalkulasi, dan penanganan kesalahan aritmetika yang tangguh.

## Fitur Utama
- **Operasi Aritmetika**: Penjumlahan (+), Pengurangan (-), Perkalian (*), Pembagian (/), Modulo (%), dan Pangkat (^).
- **Fungsi Ilmiah**: Sin, Cos, Tan, Log10, Ln, Sqrt, dan Faktorial (!).
- **Mode Sudut**: Derajat (*Degree*) dan Radian (*Radian*).
- **Evaluasi Ekspresi**: Tokenizer (Lexer) dan algoritma Shunting-yard untuk konversi Infix ke Postfix (RPN).
- **Riwayat Perhitungan**: Pencatatan log ekspresi dan hasil dengan fitur *Undo* dan *Clear*.
- **Validasi Input**: Pengecekan keseimbangan tanda kurung dan karakter ilegal.

## Struktur File (22 File Dart)
- `bin/main.dart`: Entry point aplikasi CLI.
- `lib/calculator_cli.dart`: Library export publik.
- `lib/src/models/`: Token, TokenType, AngleMode, CalculationHistory.
- `lib/src/exceptions/`: CalculatorException, SyntaxException, MathDomainException.
- `lib/src/parsers/`: Lexer, ShuntingYard, ExpressionParser.
- `lib/src/services/`: ArithmeticService, ScientificService, EvaluatorService, HistoryService.
- `lib/src/validators/`: InputValidator.
- `lib/src/utils/`: NumberFormatter.
- `lib/src/config/`: CalculatorConfig.
- `lib/src/application/`: CalculatorApp.
- `test/unit/`: Pengujian unit fungsi aritmetika dan parser.
- `test/integration/`: Pengujian alur kalkulasi end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
""")

    # 3. lib/src/models/token_type.dart
    write_f('lib/src/models/token_type.dart', """enum TokenType {
  number,
  plus,
  minus,
  multiply,
  divide,
  modulo,
  power,
  leftParen,
  rightParen,
  identifier,
  comma,
  eof,
}
""")

    # 4. lib/src/models/token.dart
    write_f('lib/src/models/token.dart', """import 'token_type.dart';

class Token {
  final TokenType type;
  final String text;
  final double? numberValue;
  final int position;

  Token({
    required this.type,
    required this.text,
    this.numberValue,
    required this.position,
  });

  @override
  String toString() => 'Token($type, "$text", pos: $position)';
}
""")

    # 5. lib/src/models/angle_mode.dart
    write_f('lib/src/models/angle_mode.dart', """enum AngleMode {
  degree,
  radian,
}
""")

    # 6. lib/src/models/calculation_history.dart
    write_f('lib/src/models/calculation_history.dart', """class HistoryEntry {
  final String expression;
  final double result;
  final DateTime timestamp;

  HistoryEntry({
    required this.expression,
    required this.result,
    DateTime? timestamp,
  }) : timestamp = timestamp ?? DateTime.now();

  @override
  String toString() => '[$timestamp] $expression = $result';
}
""")

    # 7. lib/src/exceptions/calculator_exception.dart
    write_f('lib/src/exceptions/calculator_exception.dart', """class CalculatorException implements Exception {
  final String message;
  CalculatorException(this.message);

  @override
  String toString() => 'CalculatorException: $message';
}
""")

    # 8. lib/src/exceptions/syntax_exception.dart
    write_f('lib/src/exceptions/syntax_exception.dart', """import 'calculator_exception.dart';

class SyntaxException extends CalculatorException {
  final int position;
  SyntaxException(super.message, {this.position = -1});

  @override
  String toString() => position >= 0
      ? 'SyntaxException at pos $position: $message'
      : 'SyntaxException: $message';
}
""")

    # 9. lib/src/exceptions/math_domain_exception.dart
    write_f('lib/src/exceptions/math_domain_exception.dart', """import 'calculator_exception.dart';

class MathDomainException extends CalculatorException {
  MathDomainException(super.message);

  @override
  String toString() => 'MathDomainException: $message';
}
""")

    # 10. lib/src/utils/number_formatter.dart
    write_f('lib/src/utils/number_formatter.dart', """class NumberFormatter {
  static String format(double value, {int precision = 8}) {
    if (value.isNaN) return 'NaN';
    if (value.isInfinite) return value.isNegative ? '-Infinity' : 'Infinity';
    
    // Check if whole integer
    if (value == value.roundToDouble() && value.abs() < 1e12) {
      return value.toInt().toString();
    }
    
    final str = value.toStringAsFixed(precision);
    // Trim trailing zeroes
    final trimmed = str.replaceAll(RegExp(r'0+$'), '').replaceAll(RegExp(r'\\.$'), '');
    return trimmed;
  }
}
""")

    # 11. lib/src/validators/input_validator.dart
    write_f('lib/src/validators/input_validator.dart', """import '../exceptions/syntax_exception.dart';

class InputValidator {
  static void validateParentheses(String expression) {
    int balance = 0;
    for (int i = 0; i < expression.length; i++) {
      final ch = expression[i];
      if (ch == '(') balance++;
      if (ch == ')') balance--;
      if (balance < 0) {
        throw SyntaxException('Unmatched closing parenthesis', position: i);
      }
    }
    if (balance > 0) {
      throw SyntaxException('Unmatched opening parenthesis at end of expression');
    }
  }

  static void validateNonEmpty(String expression) {
    if (expression.trim().isEmpty) {
      throw SyntaxException('Expression cannot be empty');
    }
  }
}
""")

    # 12. lib/src/parsers/lexer.dart
    write_f('lib/src/parsers/lexer.dart', """import '../models/token.dart';
import '../models/token_type.dart';
import '../exceptions/syntax_exception.dart';

class Lexer {
  final String source;
  int _position = 0;

  Lexer(this.source);

  List<Token> tokenize() {
    final tokens = <Token>[];
    while (_position < source.length) {
      final char = source[_position];

      if (_isWhitespace(char)) {
        _position++;
        continue;
      }

      if (_isDigit(char) || (char == '.' && _peekDigit())) {
        tokens.add(_readNumber());
        continue;
      }

      if (_isLetter(char)) {
        tokens.add(_readIdentifier());
        continue;
      }

      switch (char) {
        case '+':
          tokens.add(Token(type: TokenType.plus, text: '+', position: _position++));
          break;
        case '-':
          tokens.add(Token(type: TokenType.minus, text: '-', position: _position++));
          break;
        case '*':
          tokens.add(Token(type: TokenType.multiply, text: '*', position: _position++));
          break;
        case '/':
          tokens.add(Token(type: TokenType.divide, text: '/', position: _position++));
          break;
        case '%':
          tokens.add(Token(type: TokenType.modulo, text: '%', position: _position++));
          break;
        case '^':
          tokens.add(Token(type: TokenType.power, text: '^', position: _position++));
          break;
        case '(':
          tokens.add(Token(type: TokenType.leftParen, text: '(', position: _position++));
          break;
        case ')':
          tokens.add(Token(type: TokenType.rightParen, text: ')', position: _position++));
          break;
        case ',':
          tokens.add(Token(type: TokenType.comma, text: ',', position: _position++));
          break;
        default:
          throw SyntaxException('Unexpected character "$char"', position: _position);
      }
    }

    tokens.add(Token(type: TokenType.eof, text: '', position: _position));
    return tokens;
  }

  bool _isWhitespace(String c) => c == ' ' || c == '\\t' || c == '\\n' || c == '\\r';
  bool _isDigit(String c) => c.codeUnitAt(0) >= 48 && c.codeUnitAt(0) <= 57;
  bool _isLetter(String c) {
    final code = c.codeUnitAt(0);
    return (code >= 65 && code <= 90) || (code >= 97 && code <= 122) || c == '_';
  }

  bool _peekDigit() {
    if (_position + 1 >= source.length) return false;
    return _isDigit(source[_position + 1]);
  }

  Token _readNumber() {
    final start = _position;
    bool hasDot = false;

    while (_position < source.length) {
      final ch = source[_position];
      if (_isDigit(ch)) {
        _position++;
      } else if (ch == '.' && !hasDot) {
        hasDot = true;
        _position++;
      } else {
        break;
      }
    }

    final text = source.substring(start, _position);
    final value = double.tryParse(text);
    if (value == null) {
      throw SyntaxException('Invalid numeric literal "$text"', position: start);
    }
    return Token(type: TokenType.number, text: text, numberValue: value, position: start);
  }

  Token _readIdentifier() {
    final start = _position;
    while (_position < source.length && (_isLetter(source[_position]) || _isDigit(source[_position]))) {
      _position++;
    }
    final text = source.substring(start, _position);
    return Token(type: TokenType.identifier, text: text, position: start);
  }
}
""")

    # 13. lib/src/parsers/shunting_yard.dart
    write_f('lib/src/parsers/shunting_yard.dart', """import '../models/token.dart';
import '../models/token_type.dart';
import '../exceptions/syntax_exception.dart';

class ShuntingYard {
  static const Map<TokenType, int> _precedence = {
    TokenType.plus: 1,
    TokenType.minus: 1,
    TokenType.multiply: 2,
    TokenType.divide: 2,
    TokenType.modulo: 2,
    TokenType.power: 3,
  };

  static List<Token> convertToRpn(List<Token> tokens) {
    final outputQueue = <Token>[];
    final operatorStack = <Token>[];

    Token? prevToken;

    for (int i = 0; i < tokens.length; i++) {
      final token = tokens[i];

      if (token.type == TokenType.eof) break;

      if (token.type == TokenType.number) {
        outputQueue.add(token);
      } else if (token.type == TokenType.identifier) {
        if (i + 1 < tokens.length && tokens[i + 1].type == TokenType.leftParen) {
          operatorStack.add(token);
        } else {
          outputQueue.add(token);
        }
      } else if (_isOperator(token.type)) {
        // Handle unary minus: if at start or previous token is operator/leftParen
        if (token.type == TokenType.minus && (prevToken == null || _isOperator(prevToken.type) || prevToken.type == TokenType.leftParen)) {
          // Represent unary minus as a multiply with -1 or special handling
          outputQueue.add(Token(type: TokenType.number, text: '0', numberValue: 0.0, position: token.position));
        }

        while (operatorStack.isNotEmpty && _isOperator(operatorStack.last.type)) {
          final top = operatorStack.last;
          final pCurrent = _precedence[token.type] ?? 0;
          final pTop = _precedence[top.type] ?? 0;

          // Power is right-associative
          final isRightAssoc = token.type == TokenType.power;
          if ((!isRightAssoc && pCurrent <= pTop) || (isRightAssoc && pCurrent < pTop)) {
            outputQueue.add(operatorStack.removeLast());
          } else {
            break;
          }
        }
        operatorStack.add(token);
      } else if (token.type == TokenType.leftParen) {
        operatorStack.add(token);
      } else if (token.type == TokenType.rightParen) {
        while (operatorStack.isNotEmpty && operatorStack.last.type != TokenType.leftParen) {
          outputQueue.add(operatorStack.removeLast());
        }
        if (operatorStack.isEmpty) {
          throw SyntaxException('Mismatched parentheses in expression', position: token.position);
        }
        operatorStack.removeLast(); // pop '('

        if (operatorStack.isNotEmpty && operatorStack.last.type == TokenType.identifier) {
          outputQueue.add(operatorStack.removeLast()); // pop function call
        }
      }

      prevToken = token;
    }

    while (operatorStack.isNotEmpty) {
      final top = operatorStack.removeLast();
      if (top.type == TokenType.leftParen || top.type == TokenType.rightParen) {
        throw SyntaxException('Mismatched parentheses in expression');
      }
      outputQueue.add(top);
    }

    return outputQueue;
  }

  static bool _isOperator(TokenType type) {
    return type == TokenType.plus ||
        type == TokenType.minus ||
        type == TokenType.multiply ||
        type == TokenType.divide ||
        type == TokenType.modulo ||
        type == TokenType.power;
  }
}
""")

    # 14. lib/src/parsers/expression_parser.dart
    write_f('lib/src/parsers/expression_parser.dart', """import '../models/token.dart';
import '../validators/input_validator.dart';
import 'lexer.dart';
import 'shunting_yard.dart';

class ExpressionParser {
  List<Token> parse(String expression) {
    InputValidator.validateNonEmpty(expression);
    InputValidator.validateParentheses(expression);

    final lexer = Lexer(expression);
    final tokens = lexer.tokenize();
    return ShuntingYard.convertToRpn(tokens);
  }
}
""")

    # 15. lib/src/services/arithmetic_service.dart
    write_f('lib/src/services/arithmetic_service.dart', """import 'dart:math' as math;
import '../exceptions/math_domain_exception.dart';

class ArithmeticService {
  double add(double a, double b) => a + b;
  double subtract(double a, double b) => a - b;
  double multiply(double a, double b) => a * b;

  double divide(double a, double b) {
    if (b == 0.0) {
      throw MathDomainException('Division by zero is undefined');
    }
    return a / b;
  }

  double modulo(double a, double b) {
    if (b == 0.0) {
      throw MathDomainException('Modulo by zero is undefined');
    }
    return a % b;
  }

  double power(double base, double exp) {
    if (base < 0 && exp != exp.roundToDouble()) {
      throw MathDomainException('Negative base with fractional exponent is undefined in real numbers');
    }
    return math.pow(base, exp).toDouble();
  }
}
""")

    # 16. lib/src/services/scientific_service.dart
    write_f('lib/src/services/scientific_service.dart', """import 'dart:math' as math;
import '../models/angle_mode.dart';
import '../exceptions/math_domain_exception.dart';

class ScientificService {
  final AngleMode angleMode;

  ScientificService({this.angleMode = AngleMode.radian});

  double _toRadians(double angle) {
    return angleMode == AngleMode.degree ? angle * (math.pi / 180.0) : angle;
  }

  double sin(double x) => math.sin(_toRadians(x));
  double cos(double x) => math.cos(_toRadians(x));

  double tan(double x) {
    final rad = _toRadians(x);
    final cosVal = math.cos(rad);
    if (cosVal.abs() < 1e-15) {
      throw MathDomainException('Tangent is undefined for angle at asymptote');
    }
    return math.tan(rad);
  }

  double sqrt(double x) {
    if (x < 0) {
      throw MathDomainException('Square root of negative number is undefined in real numbers');
    }
    return math.sqrt(x);
  }

  double log10(double x) {
    if (x <= 0) {
      throw MathDomainException('Logarithm base 10 argument must be strictly positive');
    }
    return math.log(x) / math.ln10;
  }

  double ln(double x) {
    if (x <= 0) {
      throw MathDomainException('Natural logarithm argument must be strictly positive');
    }
    return math.log(x);
  }

  double factorial(double n) {
    if (n < 0 || n != n.roundToDouble()) {
      throw MathDomainException('Factorial requires non-negative integer');
    }
    final intN = n.toInt();
    if (intN > 170) {
      throw MathDomainException('Factorial overflow (maximum integer is 170)');
    }
    double res = 1.0;
    for (int i = 2; i <= intN; i++) {
      res *= i;
    }
    return res;
  }
}
""")

    # 17. lib/src/services/history_service.dart
    write_f('lib/src/services/history_service.dart', """import '../models/calculation_history.dart';

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
""")

    # 18. lib/src/services/evaluator_service.dart
    write_f('lib/src/services/evaluator_service.dart', """import '../models/token.dart';
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
          throw SyntaxException('Insufficient operands for operator "${token.text}"');
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
      throw SyntaxException('Invalid expression structure: excess operands remain');
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
""")

    # 19. lib/src/config/calculator_config.dart
    write_f('lib/src/config/calculator_config.dart', """import '../models/angle_mode.dart';

class CalculatorConfig {
  final AngleMode angleMode;
  final int precision;
  final bool storeHistory;

  const CalculatorConfig({
    this.angleMode = AngleMode.degree,
    this.precision = 8,
    this.storeHistory = true,
  });

  CalculatorConfig copyWith({
    AngleMode? angleMode,
    int? precision,
    bool? storeHistory,
  }) {
    return CalculatorConfig(
      angleMode: angleMode ?? this.angleMode,
      precision: precision ?? this.precision,
      storeHistory: storeHistory ?? this.storeHistory,
    );
  }
}
""")

    # 20. lib/src/application/calculator_app.dart
    write_f('lib/src/application/calculator_app.dart', """import '../config/calculator_config.dart';
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
        scientific = ScientificService(angleMode: (config ?? const CalculatorConfig()).angleMode),
        history = HistoryService(),
        evaluator = EvaluatorService(
          arithmetic: ArithmeticService(),
          scientific: ScientificService(angleMode: (config ?? const CalculatorConfig()).angleMode),
        );

  String execute(String input) {
    final trimmed = input.trim();
    if (trimmed.isEmpty) return '';

    if (trimmed == 'history') {
      final entries = history.getAll();
      if (entries.isEmpty) return 'No calculation history available.';
      final buffer = StringBuffer('Calculation History:\\n');
      for (int i = 0; i < entries.length; i++) {
        buffer.writeln('  [${i + 1}] ${entries[i].expression} = ${NumberFormatter.format(entries[i].result, precision: config.precision)}');
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
""")

    # 21. lib/calculator_cli.dart
    write_f('lib/calculator_cli.dart', """export 'src/models/token.dart';
export 'src/models/token_type.dart';
export 'src/models/angle_mode.dart';
export 'src/models/calculation_history.dart';
export 'src/exceptions/calculator_exception.dart';
export 'src/exceptions/syntax_exception.dart';
export 'src/exceptions/math_domain_exception.dart';
export 'src/parsers/lexer.dart';
export 'src/parsers/shunting_yard.dart';
export 'src/parsers/expression_parser.dart';
export 'src/services/arithmetic_service.dart';
export 'src/services/scientific_service.dart';
export 'src/services/evaluator_service.dart';
export 'src/services/history_service.dart';
export 'src/validators/input_validator.dart';
export 'src/utils/number_formatter.dart';
export 'src/config/calculator_config.dart';
export 'src/application/calculator_app.dart';
""")

    # 22. bin/main.dart
    write_f('bin/main.dart', """import 'dart:io';
import 'package:calculator_cli/calculator_cli.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('      01. CALCULATOR CLI & EVALUATOR          ');
  stdout.writeln('==============================================');
  stdout.writeln('Commands: "history", "undo", "clear", "exit"');
  stdout.writeln('Functions: sin, cos, tan, sqrt, log, ln, fact');
  stdout.writeln('Constants: pi, e');
  stdout.writeln('----------------------------------------------');

  final app = CalculatorApp(
    config: const CalculatorConfig(angleMode: AngleMode.degree),
  );

  if (args.isNotEmpty) {
    final expr = args.join(' ');
    try {
      final res = app.execute(expr);
      stdout.writeln('Result: $res');
    } catch (e) {
      stderr.writeln('Error: $e');
      exit(1);
    }
    return;
  }

  while (true) {
    stdout.write('calc> ');
    final line = stdin.readLineSync();
    if (line == null || line.trim().toLowerCase() == 'exit') {
      stdout.writeln('Goodbye!');
      break;
    }

    try {
      final res = app.execute(line);
      if (res.isNotEmpty) {
        stdout.writeln('=> $res');
      }
    } catch (e) {
      stderr.writeln('[Error] $e');
    }
  }
}
""")

    # 23. test/unit/calculator_unit_test.dart
    write_f('test/unit/calculator_unit_test.dart', """import 'package:test/test.dart';
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
      expect(() => sciDegree.factorial(-1), throwsA(isA<MathDomainException>()));
    });
  });

  group('Parser & Lexer Tests', () {
    test('Tokenizes complex expression', () {
      final lexer = Lexer('3 + 4 * 2 / ( 1 - 5 ) ^ 2');
      final tokens = lexer.tokenize();
      expect(tokens.map((t) => t.type), containsAllInOrder([
        TokenType.number,
        TokenType.plus,
        TokenType.number,
        TokenType.multiply,
        TokenType.number,
      ]));
    });

    test('Parenthesis validator detects mismatch', () {
      expect(() => InputValidator.validateParentheses('(3 + 4 * 2'), throwsA(isA<SyntaxException>()));
      expect(() => InputValidator.validateParentheses('3 + 4)'), throwsA(isA<SyntaxException>()));
    });
  });
}
""")

    # 24. test/integration/calculator_integration_test.dart
    write_f('test/integration/calculator_integration_test.dart', """import 'package:test/test.dart';
import 'package:calculator_cli/calculator_cli.dart';

void main() {
  group('Calculator App End-to-End Integration Tests', () {
    late CalculatorApp app;

    setUp(() {
      app = CalculatorApp(config: const CalculatorConfig(angleMode: AngleMode.degree));
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
""")

    print("Project 01 (Calculator CLI) generated successfully with 22 Dart files!")

if __name__ == '__main__':
    generate_p01('dart-project-lab')
