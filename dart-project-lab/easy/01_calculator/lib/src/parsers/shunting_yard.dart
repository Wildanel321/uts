import '../models/token.dart';
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
        if (i + 1 < tokens.length &&
            tokens[i + 1].type == TokenType.leftParen) {
          operatorStack.add(token);
        } else {
          outputQueue.add(token);
        }
      } else if (_isOperator(token.type)) {
        // Handle unary minus: if at start or previous token is operator/leftParen
        if (token.type == TokenType.minus &&
            (prevToken == null ||
                _isOperator(prevToken.type) ||
                prevToken.type == TokenType.leftParen)) {
          // Represent unary minus as a multiply with -1 or special handling
          outputQueue.add(Token(
              type: TokenType.number,
              text: '0',
              numberValue: 0.0,
              position: token.position));
        }

        while (
            operatorStack.isNotEmpty && _isOperator(operatorStack.last.type)) {
          final top = operatorStack.last;
          final pCurrent = _precedence[token.type] ?? 0;
          final pTop = _precedence[top.type] ?? 0;

          // Power is right-associative
          final isRightAssoc = token.type == TokenType.power;
          if ((!isRightAssoc && pCurrent <= pTop) ||
              (isRightAssoc && pCurrent < pTop)) {
            outputQueue.add(operatorStack.removeLast());
          } else {
            break;
          }
        }
        operatorStack.add(token);
      } else if (token.type == TokenType.leftParen) {
        operatorStack.add(token);
      } else if (token.type == TokenType.rightParen) {
        while (operatorStack.isNotEmpty &&
            operatorStack.last.type != TokenType.leftParen) {
          outputQueue.add(operatorStack.removeLast());
        }
        if (operatorStack.isEmpty) {
          throw SyntaxException('Mismatched parentheses in expression',
              position: token.position);
        }
        operatorStack.removeLast(); // pop '('

        if (operatorStack.isNotEmpty &&
            operatorStack.last.type == TokenType.identifier) {
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
