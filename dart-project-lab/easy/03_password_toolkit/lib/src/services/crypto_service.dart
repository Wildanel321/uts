import 'dart:convert';
import 'package:crypto/crypto.dart';

class CryptoService {
  static String hashKey(String masterKey) {
    return sha256.convert(utf8.encode(masterKey)).toString();
  }

  static String encrypt(String plaintext, String masterKey) {
    final keyBytes = sha256.convert(utf8.encode(masterKey)).bytes;
    final textBytes = utf8.encode(plaintext);
    final cipherBytes = <int>[];

    for (int i = 0; i < textBytes.length; i++) {
      cipherBytes.add(textBytes[i] ^ keyBytes[i % keyBytes.length]);
    }

    return base64.encode(cipherBytes);
  }

  static String decrypt(String ciphertext, String masterKey) {
    final keyBytes = sha256.convert(utf8.encode(masterKey)).bytes;
    final cipherBytes = base64.decode(ciphertext);
    final textBytes = <int>[];

    for (int i = 0; i < cipherBytes.length; i++) {
      textBytes.add(cipherBytes[i] ^ keyBytes[i % keyBytes.length]);
    }

    return utf8.decode(textBytes);
  }
}
