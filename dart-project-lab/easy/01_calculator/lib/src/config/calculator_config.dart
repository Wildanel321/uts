import '../models/angle_mode.dart';

class CalculatorConfig {
  final AngleMode angleMode;
  final int precision;
  final bool storeHistory;

  const CalculatorConfig({
    this.angleMode = AngleMode.degree,
    this.precision = 8,
    this.storeHistory = true,
  });

  CalculatorConfig copyWith({
    AngleMode? angleMode,
    int? precision,
    bool? storeHistory,
  }) {
    return CalculatorConfig(
      angleMode: angleMode ?? this.angleMode,
      precision: precision ?? this.precision,
      storeHistory: storeHistory ?? this.storeHistory,
    );
  }
}
