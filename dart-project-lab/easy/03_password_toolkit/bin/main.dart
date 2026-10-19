import 'dart:io';
import 'package:password_toolkit/password_toolkit.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('          03. PASSWORD & VAULT TOOLKIT        ');
  stdout.writeln('==============================================');

  final app = ToolkitApp();

  final pwd = app.generatePassword(const PasswordPolicy(minLength: 16));
  stdout.writeln('Generated Password : $pwd');

  final strength = app.checkStrength(pwd);
  stdout.writeln('Strength Assessment: $strength');

  final phrase = app.generatePassphrase(const PassphraseConfig(wordCount: 4));
  stdout.writeln('Generated Passphrase: $phrase');
  stdout.writeln('Passphrase Strength : ${app.checkStrength(phrase)}');

  stdout.writeln('----------------------------------------------');
  stdout.writeln('Testing Encrypted Vault...');
  const masterKey = 'super_secret_master_key_2026';
  app.saveCredential(
    serviceName: 'GitHub',
    username: 'developer@example.com',
    password: pwd,
    masterKey: masterKey,
  );

  final recovered =
      app.retrievePassword(serviceName: 'GitHub', masterKey: masterKey);
  stdout.writeln('Recovered Secret   : $recovered');
  stdout.writeln(
      'Decryption Match   : ${recovered == pwd ? "SUCCESS" : "FAILED"}');
  stdout.writeln('==============================================');
}
