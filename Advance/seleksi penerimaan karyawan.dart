import 'dart:io';

void main() {
  print('==============================================');
  print('          SELEKSI PENERIMAAN KARYAWAN         ');
  print('               (LEVEL: ADVANCE)               ');
  print('==============================================');

  stdout.write('Masukkan Usia: ');
  int usia = int.parse(stdin.readLineSync()!);

  stdout.write('Masukkan Pendidikan (D3/S1): ');
  String pendidikan = stdin.readLineSync()!.toUpperCase();

  stdout.write('Masukkan Nilai Tes: ');
  double nilaiTes = double.parse(stdin.readLineSync()!);

  print('----------------------------------------------');
  if (usia >= 21 && usia <= 35 && pendidikan == 'S1' && nilaiTes >= 70) {
    print('Status: Lolos Seleksi');
  } else if (usia >= 21 && usia <= 35 && pendidikan == 'D3' && nilaiTes >= 85) {
    print('Status: Dipertimbangkan');
  } else {
    print('Status: Tidak Lolos');
  }
  print('==============================================');
}
