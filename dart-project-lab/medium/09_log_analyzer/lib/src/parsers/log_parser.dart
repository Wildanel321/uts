import '../models/log_entry.dart';

abstract class LogParser {
  LogEntry? parseLine(String line);
}
