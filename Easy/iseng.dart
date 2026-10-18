import 'dart:io';

void main() {
  print('==============================================');
  print('       PROGRAM MENENTUKAN BILANGAN TERBESAR   ');
  print('                  (LEVEL: EASY)               ');
  print('==============================================');

  stdout.write('Masukkan bilangan pertama: ');
  int bil1 = int.parse(stdin.readLineSync()!);

  stdout.write('Masukkan bilangan kedua: ');
  int bil2 = int.parse(stdin.readLineSync()!);

  print('----------------------------------------------');
  if (bil1 > bil2) {
    print('Bilangan terbesar adalah $bil1');
  } else if (bil2 > bil1) {
    print('Bilangan terbesar adalah $bil2');
  } else {
    print('Kedua bilangan sama besar ($bil1)');
  }
  print('==============================================');
}
