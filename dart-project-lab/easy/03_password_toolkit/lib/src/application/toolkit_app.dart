import '../config/toolkit_config.dart';
import '../models/password_policy.dart';
import '../models/passphrase_config.dart';
import '../models/strength_result.dart';
import '../models/vault_entry.dart';
import '../repositories/vault_repository.dart';
import '../services/crypto_service.dart';
import '../services/passphrase_generator.dart';
import '../services/password_generator.dart';
import '../services/strength_checker.dart';

class ToolkitApp {
  final ToolkitConfig config;
  final PasswordGenerator passwordGenerator;
  final PassphraseGenerator passphraseGenerator;
  final VaultRepository vaultRepo;
  static int _idCounter = 0;

  ToolkitApp({ToolkitConfig? config})
      : config = config ?? const ToolkitConfig(),
        passwordGenerator = PasswordGenerator(),
        passphraseGenerator = PassphraseGenerator(),
        vaultRepo = VaultRepository();

  String generatePassword([PasswordPolicy? policy]) {
    return passwordGenerator.generate(policy ?? config.defaultPolicy);
  }

  String generatePassphrase(
      [PassphraseConfig config = const PassphraseConfig()]) {
    return passphraseGenerator.generate(config);
  }

  StrengthResult checkStrength(String password) {
    return StrengthChecker.check(password);
  }

  VaultEntry saveCredential({
    required String serviceName,
    required String username,
    required String password,
    required String masterKey,
  }) {
    final encrypted = CryptoService.encrypt(password, masterKey);
    final entry = VaultEntry(
      id: 'vlt_${DateTime.now().microsecondsSinceEpoch}_${++_idCounter}',
      serviceName: serviceName,
      username: username,
      encryptedCiphertext: encrypted,
    );
    vaultRepo.add(entry);
    return entry;
  }

  String retrievePassword({
    required String serviceName,
    required String masterKey,
  }) {
    final entry = vaultRepo.findByService(serviceName);
    if (entry == null) {
      throw Exception('Service not found in vault: $serviceName');
    }
    return CryptoService.decrypt(entry.encryptedCiphertext, masterKey);
  }
}
