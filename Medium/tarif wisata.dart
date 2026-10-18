import 'dart:io';

void main() {
  print('==============================================');
  print('        PROGRAM TARIF TEMPAT WISATA           ');
  print('               (LEVEL: MEDIUM)                ');
  print('==============================================');

  stdout.write('Masukkan usia pengunjung: ');
  int usia = int.parse(stdin.readLineSync()!);

  int tarif = 0;

  if (usia < 5) {
    tarif = 0;
  } else if (usia <= 12) {
    tarif = 15000;
  } else if (usia <= 59) {
    tarif = 30000;
  } else {
    tarif = 20000;
  }

  print('----------------------------------------------');
  print('Tarif Tiket: Rp $tarif');
  print('==============================================');
}
