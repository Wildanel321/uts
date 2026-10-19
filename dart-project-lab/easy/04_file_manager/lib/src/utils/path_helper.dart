import 'package:path/path.dart' as p;

class PathHelper {
  static String normalize(String inputPath) => p.normalize(inputPath);
  static String getExtension(String filePath) =>
      p.extension(filePath).toLowerCase();
  static String getBasename(String filePath) => p.basename(filePath);
}
