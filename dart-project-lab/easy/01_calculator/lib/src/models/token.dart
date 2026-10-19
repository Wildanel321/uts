import 'token_type.dart';

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
