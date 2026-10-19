import 'dart:io';
import 'package:calculator_cli/calculator_cli.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('      01. CALCULATOR CLI & EVALUATOR          ');
  stdout.writeln('==============================================');
  stdout.writeln('Commands: "history", "undo", "clear", "exit"');
  stdout.writeln('Functions: sin, cos, tan, sqrt, log, ln, fact');
  stdout.writeln('Constants: pi, e');
  stdout.writeln('----------------------------------------------');

  final app = CalculatorApp(
    config: const CalculatorConfig(angleMode: AngleMode.degree),
  );

  if (args.isNotEmpty) {
    final expr = args.join(' ');
    try {
      final res = app.execute(expr);
      stdout.writeln('Result: $res');
    } catch (e) {
      stderr.writeln('Error: $e');
      exit(1);
    }
    return;
  }

  while (true) {
    stdout.write('calc> ');
    final line = stdin.readLineSync();
    if (line == null || line.trim().toLowerCase() == 'exit') {
      stdout.writeln('Goodbye!');
      break;
    }

    try {
      final res = app.execute(line);
      if (res.isNotEmpty) {
        stdout.writeln('=> $res');
      }
    } catch (e) {
      stderr.writeln('[Error] $e');
    }
  }
}
