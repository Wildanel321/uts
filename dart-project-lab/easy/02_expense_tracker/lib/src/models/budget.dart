class Budget {
  final int month;
  final int year;
  final double limitAmount;

  Budget({
    required this.month,
    required this.year,
    required this.limitAmount,
  });

  Map<String, dynamic> toJson() => {
        'month': month,
        'year': year,
        'limitAmount': limitAmount,
      };

  factory Budget.fromJson(Map<String, dynamic> json) => Budget(
        month: json['month'] as int,
        year: json['year'] as int,
        limitAmount: (json['limitAmount'] as num).toDouble(),
      );
}
