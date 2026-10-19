import 'calculator_exception.dart';

class MathDomainException extends CalculatorException {
  MathDomainException(super.message);

  @override
  String toString() => 'MathDomainException: $message';
}
