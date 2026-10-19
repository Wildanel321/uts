import 'dart:math' as math;
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
      throw MathDomainException(
          'Negative base with fractional exponent is undefined in real numbers');
    }
    return math.pow(base, exp).toDouble();
  }
}
