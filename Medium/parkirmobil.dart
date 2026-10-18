import 'dart:io';

void main() {
  print('==============================================');
  print('         PROGRAM TARIF PARKIR MOBIL           ');
  print('               (LEVEL: MEDIUM)                ');
  print('==============================================');

  stdout.write('Masukkan durasi parkir (jam): ');
  int jam = int.parse(stdin.readLineSync()!);

  int totalBiaya = 0;

  if (jam > 8) {
    totalBiaya = 20000;
  } else if (jam <= 2) {
    totalBiaya = 5000;
  } else {
    totalBiaya = 5000 + (jam - 2) * 2000;
  }

  print('----------------------------------------------');
  print('Durasi Parkir : $jam jam');
  print('Total Biaya   : Rp $totalBiaya');
  print('==============================================');
}
