class DateHelper {
  static String formatDate(DateTime dt) {
    final y = dt.year.toString().padLeft(4, '0');
    final m = dt.month.toString().padLeft(2, '0');
    final d = dt.day.toString().padLeft(2, '0');
    return '$y-$m-$d';
  }

  static bool isSameMonth(DateTime a, int year, int month) {
    return a.year == year && a.month == month;
  }
}
