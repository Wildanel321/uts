import '../models/password_policy.dart';

class ToolkitConfig {
  final PasswordPolicy defaultPolicy;
  final String vaultStoragePath;

  const ToolkitConfig({
    this.defaultPolicy = const PasswordPolicy(),
    this.vaultStoragePath = 'data/vault.enc',
  });
}
