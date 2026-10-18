import 'dart:io';

void main() {
  print('==============================================');
  print('       PROGRAM HITUNG TARIF LISTRIK           ');
  print('               (LEVEL: ADVANCE)               ');
  print('==============================================');

  stdout.write('Masukkan pemakaian listrik (kWh): ');
  int pemakaian = int.parse(stdin.readLineSync()!);

  int tier1 = 0;
  int tier2 = 0;
  int tier3 = 0;

  if (pemakaian <= 100) {
    tier1 = pemakaian * 1500;
  } else if (pemakaian <= 300) {
    tier1 = 100 * 1500;
    tier2 = (pemakaian - 100) * 2000;
  } else {
    tier1 = 100 * 1500;
    tier2 = 200 * 2000;
    tier3 = (pemakaian - 300) * 2500;
  }

  int totalTagihan = tier1 + tier2 + tier3;

  print('----------------------------------------------');
  print('Total Pemakaian : $pemakaian kWh');
  print('Tier 1          : Rp $tier1');
  if (tier2 > 0) print('Tier 2          : Rp $tier2');
  if (tier3 > 0) print('Tier 3          : Rp $tier3');
  print('----------------------------------------------');
  print('Total Tagihan   : Rp $totalTagihan');
  print('==============================================');
}
