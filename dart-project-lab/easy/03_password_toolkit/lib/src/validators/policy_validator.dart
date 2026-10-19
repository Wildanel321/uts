import '../models/password_policy.dart';
import '../exceptions/toolkit_exception.dart';

class PolicyValidator {
  static void validate(PasswordPolicy policy) {
    if (policy.minLength < 4) {
      throw ToolkitException('Password minimum length must be at least 4.');
    }
    if (!policy.requireUppercase &&
        !policy.requireLowercase &&
        !policy.requireDigits &&
        !policy.requireSymbols) {
      throw ToolkitException(
          'At least one character set must be enabled in policy.');
    }
  }
}
