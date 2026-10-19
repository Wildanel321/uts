import '../models/token.dart';
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
          tokens.add(
              Token(type: TokenType.plus, text: '+', position: _position++));
          break;
        case '-':
          tokens.add(
              Token(type: TokenType.minus, text: '-', position: _position++));
          break;
        case '*':
          tokens.add(Token(
              type: TokenType.multiply, text: '*', position: _position++));
          break;
        case '/':
          tokens.add(
              Token(type: TokenType.divide, text: '/', position: _position++));
          break;
        case '%':
          tokens.add(
              Token(type: TokenType.modulo, text: '%', position: _position++));
          break;
        case '^':
          tokens.add(
              Token(type: TokenType.power, text: '^', position: _position++));
          break;
        case '(':
          tokens.add(Token(
              type: TokenType.leftParen, text: '(', position: _position++));
          break;
        case ')':
          tokens.add(Token(
              type: TokenType.rightParen, text: ')', position: _position++));
          break;
        case ',':
          tokens.add(
              Token(type: TokenType.comma, text: ',', position: _position++));
          break;
        default:
          throw SyntaxException('Unexpected character "$char"',
              position: _position);
      }
    }

    tokens.add(Token(type: TokenType.eof, text: '', position: _position));
    return tokens;
  }

  bool _isWhitespace(String c) =>
      c == ' ' || c == '\t' || c == '\n' || c == '\r';
  bool _isDigit(String c) => c.codeUnitAt(0) >= 48 && c.codeUnitAt(0) <= 57;
  bool _isLetter(String c) {
    final code = c.codeUnitAt(0);
    return (code >= 65 && code <= 90) ||
        (code >= 97 && code <= 122) ||
        c == '_';
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
    return Token(
        type: TokenType.number,
        text: text,
        numberValue: value,
        position: start);
  }

  Token _readIdentifier() {
    final start = _position;
    while (_position < source.length &&
        (_isLetter(source[_position]) || _isDigit(source[_position]))) {
      _position++;
    }
    final text = source.substring(start, _position);
    return Token(type: TokenType.identifier, text: text, position: start);
  }
}
