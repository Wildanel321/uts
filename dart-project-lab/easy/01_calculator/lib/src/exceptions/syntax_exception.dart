import 'calculator_exception.dart';

class SyntaxException extends CalculatorException {
  final int position;
  SyntaxException(super.message, {this.position = -1});

  @override
  String toString() => position >= 0
      ? 'SyntaxException at pos $position: $message'
      : 'SyntaxException: $message';
}
