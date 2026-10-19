class CronParser {
  // Simple cron parser: supports "@every Xs" or "@every Xm"
  static Duration? parseSimple(String cronExpr) {
    final trimmed = cronExpr.trim().toLowerCase();
    if (trimmed.startsWith('@every ')) {
      final spec = trimmed.substring(7).trim();
      if (spec.endsWith('s')) {
        final sec = int.tryParse(spec.replaceAll('s', ''));
        if (sec != null) return Duration(seconds: sec);
      } else if (spec.endsWith('m')) {
        final min = int.tryParse(spec.replaceAll('m', ''));
        if (min != null) return Duration(minutes: min);
      } else if (spec.endsWith('h')) {
        final hr = int.tryParse(spec.replaceAll('h', ''));
        if (hr != null) return Duration(hours: hr);
      }
    }
    return null;
  }
}
