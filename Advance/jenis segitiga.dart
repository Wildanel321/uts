import 'dart:io';

void main() {
  print('==============================================');
  print('        PROGRAM KLASIFIKASI SEGITIGA          ');
  print('               (LEVEL: ADVANCE)               ');
  print('==============================================');

  stdout.write('Masukkan sisi a: ');
  double a = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan sisi b: ');
  double b = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan sisi c: ');
  double c = double.parse(stdin.readLineSync()!);

  print('----------------------------------------------');
  // Syarat segitiga: jumlah 2 sisi harus selalu lebih besar dari sisi lainnya
  if (a + b > c && a + c > b && b + c > a) {
    if (a == b && b == c) {
      print('Jenis Segitiga: Sama Sisi');
    } else if (a == b || a == c || b == c) {
      print('Jenis Segitiga: Sama Kaki');
    } else {
      print('Jenis Segitiga: Sembarang');
    }
  } else {
    print('Status: Bukan Segitiga');
  }
  print('==============================================');
}
