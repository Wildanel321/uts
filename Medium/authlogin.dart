import 'dart:io';

void main() {
  print('==============================================');
  print('          PROGRAM AUTENTIKASI LOGIN           ');
  print('               (LEVEL: MEDIUM)                ');
  print('==============================================');

  stdout.write('Masukkan Username: ');
  String? username = stdin.readLineSync();

  stdout.write('Masukkan Password: ');
  String? password = stdin.readLineSync();

  print('----------------------------------------------');
  if (username == 'admin' && password == '12345') {
    print('Status: Login Berhasil');
  } else {
    print('Status: Login Gagal (Username atau password salah)');
  }
  print('==============================================');
}
