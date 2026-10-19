import 'dart:math';
import '../models/passphrase_config.dart';
import '../utils/word_list.dart';

class PassphraseGenerator {
  final Random _rng;

  PassphraseGenerator({Random? random}) : _rng = random ?? Random.secure();

  String generate([PassphraseConfig config = const PassphraseConfig()]) {
    final selectedWords = <String>[];
    for (int i = 0; i < config.wordCount; i++) {
      String word = WordList.words[_rng.nextInt(WordList.words.length)];
      if (config.capitalize) {
        word = word[0].toUpperCase() + word.substring(1);
      }
      selectedWords.add(word);
    }

    String result = selectedWords.join(config.separator);
    if (config.includeNumber) {
      result += '${config.separator}${_rng.nextInt(900) + 100}';
    }
    return result;
  }
}
