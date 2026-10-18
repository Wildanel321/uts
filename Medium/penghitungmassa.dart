import 'dart:io';

void main() {
  print('==============================================');
  print('         PROGRAM PENGHITUNG BMI               ');
  print('            (LEVEL: MEDIUM)                   ');
  print('==============================================');

  stdout.write('Masukkan berat badan (kg): ');
  double berat = double.parse(stdin.readLineSync()!);

  stdout.write('Masukkan tinggi badan (meter): ');
  double tinggi = double.parse(stdin.readLineSync()!);

  double bmi = berat / (tinggi * tinggi);

  String kategori = '';
  if (bmi < 18.5) {
    kategori = 'Kurus';
  } else if (bmi <= 24.9) {
    kategori = 'Normal';
  } else if (bmi <= 29.9) {
    kategori = 'Kelebihan Berat Badan';
  } else {
    kategori = 'Obesitas';
  }

  print('----------------------------------------------');
  print('Nilai BMI : ${bmi.toStringAsFixed(1)}');
  print('Kategori  : $kategori');
  print('==============================================');
}
