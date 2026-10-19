enum LogLevel {
  debug,
  info,
  warn,
  error,
  fatal;

  static LogLevel fromString(String val) {
    switch (val.trim().toUpperCase()) {
      case 'DEBUG':
        return LogLevel.debug;
      case 'WARN':
      case 'WARNING':
        return LogLevel.warn;
      case 'ERROR':
        return LogLevel.error;
      case 'FATAL':
        return LogLevel.fatal;
      case 'INFO':
      default:
        return LogLevel.info;
    }
  }
}
