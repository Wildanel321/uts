import '../exceptions/syntax_exception.dart';

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
      throw SyntaxException(
          'Unmatched opening parenthesis at end of expression');
    }
  }

  static void validateNonEmpty(String expression) {
    if (expression.trim().isEmpty) {
      throw SyntaxException('Expression cannot be empty');
    }
  }
}
