import '../models/token.dart';
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
