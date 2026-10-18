import 'dart:io';

void main() {
  print('==============================================');
  print('        PROGRAM PENENTUAN KELULUSAN           ');
  print('               (LEVEL: ADVANCE)               ');
  print('==============================================');

  stdout.write('Masukkan Nilai Tugas: ');
  double tugas = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan Nilai UTS: ');
  double uts = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan Nilai UAS: ');
  double uas = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan Kehadiran (%): ');
  double kehadiran = double.parse(stdin.readLineSync()!);

  double nilaiAkhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas);

  print('----------------------------------------------');
  print('Nilai Akhir : ${nilaiAkhir.toStringAsFixed(2)}');
  print('Kehadiran   : $kehadiran%');

  if (uas < 40) {
    print('Status      : Tidak Lulus (UAS < 40)');
  } else if (nilaiAkhir >= 60 && kehadiran >= 75) {
    print('Status      : Lulus');
  } else {
    print('Status      : Tidak Lulus');
  }
  print('==============================================');
}
