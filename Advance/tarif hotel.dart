import 'dart:io';

void main() {
  print('==============================================');
  print('         PROGRAM TARIF RESERVASI HOTEL        ');
  print('               (LEVEL: ADVANCE)               ');
  print('==============================================');

  stdout.write('Masukkan harga kamar per malam (Rp): ');
  double hargaKamar = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan jumlah malam menginap: ');
  int malam = int.parse(stdin.readLineSync()!);

  stdout.write('Apakah member? (Y/N): ');
  String member = stdin.readLineSync()!.toUpperCase();

  double totalAwal = hargaKamar * malam;
  double diskonPersen = 0;

  if (member == 'Y') {
    if (malam <= 2) {
      diskonPersen = 0.10;
    } else if (malam <= 5) {
      diskonPersen = 0.15;
    } else {
      diskonPersen = 0.25;
    }
  } else {
    if (malam > 5) {
      diskonPersen = 0.10;
    }
  }

  double nominalDiskon = totalAwal * diskonPersen;
  double setelahDiskon = totalAwal - nominalDiskon;
  double potonganTambahan = 0;

  if (setelahDiskon > 3000000) {
    potonganTambahan = 200000;
  }

  double totalBayar = setelahDiskon - potonganTambahan;

  print('----------------------------------------------');
  print('Total Awal        : Rp $totalAwal');
  print('Diskon            : ${(diskonPersen * 100).toInt()}% (Rp $nominalDiskon)');
  print('Setelah Diskon    : Rp $setelahDiskon');
  print('Potongan Tambahan : Rp $potonganTambahan');
  print('Total Bayar       : Rp $totalBayar');
  print('==============================================');
}
