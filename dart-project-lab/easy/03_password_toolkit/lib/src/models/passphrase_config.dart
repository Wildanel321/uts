class PassphraseConfig {
  final int wordCount;
  final String separator;
  final bool capitalize;
  final bool includeNumber;

  const PassphraseConfig({
    this.wordCount = 4,
    this.separator = '-',
    this.capitalize = true,
    this.includeNumber = true,
  });
}
