import 'package:test/test.dart';
import 'package:password_toolkit/password_toolkit.dart';

void main() {
  group('Encrypted Vault Flow Tests', () {
    late ToolkitApp app;
    const masterKey = 'master_pass_123';

    setUp(() {
      app = ToolkitApp();
    });

    test('Encrypts and decrypts credential roundtrip', () {
      const plainPassword = 'MySecretPassword!2026';
      app.saveCredential(
        serviceName: 'AWS',
        username: 'cloud_user',
        password: plainPassword,
        masterKey: masterKey,
      );

      final recovered =
          app.retrievePassword(serviceName: 'AWS', masterKey: masterKey);
      expect(recovered, equals(plainPassword));
    });

    test('Throws VaultException on duplicate service and username', () {
      app.saveCredential(
        serviceName: 'Gmail',
        username: 'user@gmail.com',
        password: 'Pass1',
        masterKey: masterKey,
      );

      expect(
        () => app.saveCredential(
          serviceName: 'Gmail',
          username: 'user@gmail.com',
          password: 'Pass2',
          masterKey: masterKey,
        ),
        throwsA(isA<VaultException>()),
      );
    });
  });
}
