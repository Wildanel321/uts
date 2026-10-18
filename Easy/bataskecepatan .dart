import 'dart:io';

void main() {
  print('==============================================');
  print('       PROGRAM BATAS KECEPATAN KENDARAAN      ');
  print('                (LEVEL: EASY)                 ');
  print('==============================================');

  stdout.write('Masukkan kecepatan kendaraan (km/jam): ');
  int kecepatan = int.parse(stdin.readLineSync()!);

  if (kecepatan > 80) {
    print('Status: Melebihi Batas Kecepatan');
  } else {
    print('Status: Kecepatan Aman');
  }
}
