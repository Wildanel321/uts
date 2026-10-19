import 'dart:math';
import '../models/question.dart';

class QuestionShuffler {
  final Random _rng;

  QuestionShuffler({Random? random}) : _rng = random ?? Random();

  List<Question> shuffleQuestions(List<Question> questions) {
    final copy = List<Question>.from(questions);
    for (int i = copy.length - 1; i > 0; i--) {
      final j = _rng.nextInt(i + 1);
      final temp = copy[i];
      copy[i] = copy[j];
      copy[j] = temp;
    }
    return copy;
  }

  List<String> shuffleOptions(List<String> options) {
    final copy = List<String>.from(options);
    copy.shuffle(_rng);
    return copy;
  }
}
