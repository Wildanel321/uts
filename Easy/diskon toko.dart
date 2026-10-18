import 'dart:io';

void main() {
  print('==============================================');
  print('          PROGRAM DISKON TOKO                 ');
  print('             (LEVEL: EASY)                    ');
  print('==============================================');

  stdout.write('Masukkan total belanja (Rp): ');
  double totalBelanja = double.parse(stdin.readLineSync()!);

  double diskon = 0;
  if (totalBelanja >= 500000) {
    diskon = totalBelanja * 0.10;
  }

  double totalBayar = totalBelanja - diskon;

  print('----------------------------------------------');
  print('Total Belanja : Rp $totalBelanja');
  print('Diskon        : Rp $diskon');
  print('Total Bayar   : Rp $totalBayar');
  print('==============================================');
}
