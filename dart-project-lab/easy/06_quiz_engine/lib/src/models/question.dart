import 'question_type.dart';

class Question {
  final String id;
  final String text;
  final QuestionType type;
  final List<String> options;
  final List<String> correctAnswers;
  final int points;
  final String explanation;

  const Question({
    required this.id,
    required this.text,
    required this.type,
    this.options = const [],
    required this.correctAnswers,
    this.points = 10,
    this.explanation = '',
  });

  Map<String, dynamic> toJson() => {
        'id': id,
        'text': text,
        'type': type.name,
        'options': options,
        'correctAnswers': correctAnswers,
        'points': points,
        'explanation': explanation,
      };

  factory Question.fromJson(Map<String, dynamic> json) => Question(
        id: json['id'] as String,
        text: json['text'] as String,
        type: QuestionType.values.byName(json['type'] as String),
        options: List<String>.from(json['options'] as List? ?? []),
        correctAnswers:
            List<String>.from(json['correctAnswers'] as List? ?? []),
        points: json['points'] as int? ?? 10,
        explanation: json['explanation'] as String? ?? '',
      );
}
