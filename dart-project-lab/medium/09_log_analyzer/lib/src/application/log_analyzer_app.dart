import '../config/analyzer_config.dart';
import '../models/analysis_report.dart';
import '../models/filter_criteria.dart';
import '../models/log_entry.dart';
import '../parsers/clf_log_parser.dart';
import '../parsers/log_parser.dart';
import '../parsers/standard_log_parser.dart';
import '../services/aggregation_service.dart';
import '../services/filter_service.dart';
import '../services/report_exporter.dart';

class LogAnalyzerApp {
  final AnalyzerConfig config;
  final LogParser standardParser;
  final LogParser clfParser;

  LogAnalyzerApp({AnalyzerConfig? config})
      : config = config ?? const AnalyzerConfig(),
        standardParser = StandardLogParser(),
        clfParser = ClfLogParser();

  List<LogEntry> parseLines(List<String> lines, {bool isClf = false}) {
    final parser = isClf ? clfParser : standardParser;
    final results = <LogEntry>[];
    for (final line in lines) {
      final entry = parser.parseLine(line);
      if (entry != null) {
        results.add(entry);
      }
    }
    return results;
  }

  List<LogEntry> filterEntries(
      List<LogEntry> entries, FilterCriteria criteria) {
    return entries.where((e) => FilterService.matches(e, criteria)).toList();
  }

  AnalysisReport analyze(List<LogEntry> entries) =>
      AggregationService.analyze(entries);
  String exportReportJson(AnalysisReport report) =>
      ReportExporter.toJson(report);
  String exportReportCsv(AnalysisReport report) => ReportExporter.toCsv(report);
}
