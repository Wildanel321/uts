import 'dart:io';

const List<String> projects = [
  'easy/01_calculator',
  'easy/02_expense_tracker',
  'easy/03_password_toolkit',
  'easy/04_file_manager',
  'easy/05_contact_book',
  'easy/06_quiz_engine',
  'medium/07_inventory_system',
  'medium/08_task_scheduler',
  'medium/09_log_analyzer',
  'medium/10_rest_api_client',
  'medium/11_chat_server',
  'medium/12_web_scraper',
  'advance/13_mini_database',
  'advance/14_http_framework',
  'advance/15_static_code_analyzer',
  'advance/16_job_queue_engine',
];

void main(List<String> args) async {
  stdout.writeln('=====================================================');
  stdout.writeln('   DART PROJECT LAB — COMPLETE AUTOMATED VERIFIER     ');
  stdout.writeln('=====================================================');

  final dartVersion = Platform.version;
  stdout.writeln('Dart SDK version: $dartVersion');
  stdout.writeln('Total Projects to verify: ${projects.length}\n');

  int totalFiles = 0;
  int passedProjects = 0;
  int failedProjects = 0;
  final failedList = <String>[];

  for (final projectRelPath in projects) {
    final projDir = Directory(projectRelPath);
    stdout.writeln('-----------------------------------------------------');
    stdout.writeln('Verifying: $projectRelPath');
    stdout.writeln('-----------------------------------------------------');

    if (!projDir.existsSync()) {
      stdout.writeln('[ERROR] Directory not found: $projectRelPath');
      failedProjects++;
      failedList.add(projectRelPath);
      continue;
    }

    // 1. Count Dart files
    final dartFiles = projDir
        .listSync(recursive: true)
        .whereType<File>()
        .where((f) => f.path.endsWith('.dart') && !f.path.contains('.dart_tool'))
        .toList();

    stdout.writeln('Found ${dartFiles.length} Dart files.');
    totalFiles += dartFiles.length;

    if (dartFiles.length < 20) {
      stdout.writeln('[FAILED] Project has fewer than 20 Dart files: ${dartFiles.length}');
      failedProjects++;
      failedList.add(projectRelPath);
      continue;
    }

    // 2. Run pub get
    stdout.write('Running "dart pub get"... ');
    final pubResult = await Process.run('dart', ['pub', 'get'], workingDirectory: projectRelPath);
    if (pubResult.exitCode != 0) {
      stdout.writeln('[FAILED]');
      stderr.writeln(pubResult.stderr);
      failedProjects++;
      failedList.add(projectRelPath);
      continue;
    }
    stdout.writeln('[OK]');

    // 3. Run dart format check
    stdout.write('Running "dart format --output=none --set-exit-if-changed ."... ');
    final formatResult = await Process.run(
      'dart',
      ['format', '--output=none', '--set-exit-if-changed', '.'],
      workingDirectory: projectRelPath,
    );
    if (formatResult.exitCode != 0) {
      stdout.writeln('[FAILED]');
      stdout.writeln(formatResult.stdout);
      stderr.writeln(formatResult.stderr);
      failedProjects++;
      failedList.add(projectRelPath);
      continue;
    }
    stdout.writeln('[OK]');

    // 4. Run dart analyze
    stdout.write('Running "dart analyze"... ');
    final analyzeResult = await Process.run('dart', ['analyze'], workingDirectory: projectRelPath);
    if (analyzeResult.exitCode != 0) {
      stdout.writeln('[FAILED]');
      stdout.writeln(analyzeResult.stdout);
      stderr.writeln(analyzeResult.stderr);
      failedProjects++;
      failedList.add(projectRelPath);
      continue;
    }
    stdout.writeln('[OK]');

    // 5. Run dart test
    stdout.write('Running "dart test"... ');
    final testResult = await Process.run('dart', ['test'], workingDirectory: projectRelPath);
    if (testResult.exitCode != 0) {
      stdout.writeln('[FAILED]');
      stdout.writeln(testResult.stdout);
      stderr.writeln(testResult.stderr);
      failedProjects++;
      failedList.add(projectRelPath);
      continue;
    }
    stdout.writeln('[OK]');

    passedProjects++;
  }

  stdout.writeln('=====================================================');
  stdout.writeln('                 VERIFICATION SUMMARY                ');
  stdout.writeln('=====================================================');
  stdout.writeln('Total Projects Tested : ${projects.length}');
  stdout.writeln('Passed Projects       : $passedProjects');
  stdout.writeln('Failed Projects       : $failedProjects');
  stdout.writeln('Total Pure Dart Files : $totalFiles (Required: >= 320)');

  if (failedProjects > 0) {
    stdout.writeln('\nFailed Projects list:');
    for (final p in failedList) {
      stdout.writeln(' - $p');
    }
    exit(1);
  } else {
    stdout.writeln('\nALL 16 PROJECTS PASSED ALL FORMAT, ANALYZE, AND TEST CHECKS!');
    exit(0);
  }
}
