import 'dart:io';

void main() {
  print('Program Seleksi Beasiswa Poliwangi');

  stdout.write('Masukkan IPK mahasiswa: ');
  double ipk = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan penghasilan orang tua per bulan (Rp): ');
  double penghasilan = double.parse(stdin.readLineSync()!);

  if (ipk >= 3.50 && penghasilan <= 4000000) {
    print('Berhak Menerima Beasiswa');
  } else {
    print('Tidak Berhak');
  }
}
