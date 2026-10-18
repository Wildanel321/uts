import 'dart:io';

void main() {
  print('==============================================');
  print('          PROGRAM SELEKSI BEASISWA            ');
  print('               (LEVEL: MEDIUM)                ');
  print('==============================================');

  stdout.write('Masukkan IPK mahasiswa: ');
  double ipk = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan penghasilan orang tua per bulan (Rp): ');
  double penghasilan = double.parse(stdin.readLineSync()!);

  print('----------------------------------------------');
  if (ipk >= 3.50 && penghasilan <= 4000000) {
    print('Status: Berhak Menerima Beasiswa');
  } else {
    print('Status: Tidak Berhak Menerima Beasiswa');
  }
  print('==============================================');
}
