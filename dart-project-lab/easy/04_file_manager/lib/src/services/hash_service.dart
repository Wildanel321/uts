import 'dart:io';
import 'package:crypto/crypto.dart';
import '../models/hash_result.dart';
import '../validators/path_validator.dart';

class HashService {
  static Future<HashResult> computeSha256(String filePath) async {
    PathValidator.validateFileExists(filePath);
    final file = File(filePath);
    final bytes = await file.readAsBytes();
    final digest = sha256.convert(bytes);

    return HashResult(
      filePath: filePath,
      algorithm: 'SHA-256',
      digestHex: digest.toString(),
      sizeBytes: bytes.length,
    );
  }

  static bool compareHashes(HashResult a, HashResult b) {
    return a.digestHex.toLowerCase() == b.digestHex.toLowerCase();
  }
}
