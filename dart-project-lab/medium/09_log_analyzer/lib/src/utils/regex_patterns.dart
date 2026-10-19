class RegexPatterns {
  // [2026-01-01 12:00:00] [INFO] [AuthService] Message text here
  static final standardLog = RegExp(
    r'^\[(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2})\]\s*\[(\w+)\]\s*(?:\[([^\]]+)\])?\s*(.*)$',
  );

  // 192.168.1.1 - - [10/Oct/2026:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
  static final clfLog = RegExp(
    r'^(\S+)\s+\S+\s+\S+\s+\[([^\]]+)\]\s+"(\S+)\s+(\S+)\s+[^"]*"\s+(\d{3})\s+(\d+|-)',
  );
}
