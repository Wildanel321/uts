class HashResult {
  final String filePath;
  final String algorithm;
  final String digestHex;
  final int sizeBytes;

  HashResult({
    required this.filePath,
    required this.algorithm,
    required this.digestHex,
    required this.sizeBytes,
  });

  @override
  String toString() => '[$algorithm] $digestHex ($sizeBytes bytes)';
}
