class PasswordPolicy {
  final int minLength;
  final bool requireUppercase;
  final bool requireLowercase;
  final bool requireDigits;
  final bool requireSymbols;
  final bool excludeAmbiguous;

  const PasswordPolicy({
    this.minLength = 12,
    this.requireUppercase = true,
    this.requireLowercase = true,
    this.requireDigits = true,
    this.requireSymbols = true,
    this.excludeAmbiguous = false,
  });
}
