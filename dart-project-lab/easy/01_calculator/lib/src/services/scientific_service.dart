import 'dart:math' as math;
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
      throw MathDomainException(
          'Square root of negative number is undefined in real numbers');
    }
    return math.sqrt(x);
  }

  double log10(double x) {
    if (x <= 0) {
      throw MathDomainException(
          'Logarithm base 10 argument must be strictly positive');
    }
    return math.log(x) / math.ln10;
  }

  double ln(double x) {
    if (x <= 0) {
      throw MathDomainException(
          'Natural logarithm argument must be strictly positive');
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
