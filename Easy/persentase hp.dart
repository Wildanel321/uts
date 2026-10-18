import 'dart:io';

void main() {
  print('==============================================');
  print('        PROGRAM CEK BATERAI HP                ');
  print('             (LEVEL: EASY)                    ');
  print('==============================================');

  stdout.write('Masukkan persentase baterai: ');
  int baterai = int.parse(stdin.readLineSync()!);

  print('----------------------------------------------');
  if (baterai < 20) {
    print('Peringatan: Segera Isi Daya');
  } else {
    print('Status: Baterai Aman');
  }
  print('==============================================');
}
