import 'dart:io';

void main() {
  print('==============================================');
  print('          PROGRAM PENARIKAN SALDO             ');
  print('               (LEVEL: EASY)                  ');
  print('==============================================');

  stdout.write('Masukkan saldo rekening (Rp): ');
  double saldo = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan jumlah penarikan (Rp): ');
  double tarik = double.parse(stdin.readLineSync()!);

  print('----------------------------------------------');
  if (tarik <= saldo) {
    saldo -= tarik;
    print('Status: Transaksi Berhasil');
    print('Sisa Saldo: Rp $saldo');
  } else {
    print('Status: Saldo Tidak Cukup');
  }
  print('==============================================');
}
