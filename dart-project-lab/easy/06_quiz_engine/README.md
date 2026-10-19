# 06. Quiz Engine

Aplikasi mesin kuis interaktif (*Quiz Engine*) berbasis Dart murni. Menyediakan bank soal dengan aneka tipe pertanyaan (Pilihan Ganda, Benar/Salah, Isian Singkat, dan Multi-Jawaban), pengacakan pertanyaan berbasis algoritma *Fisher-Yates*, timer batas waktu pengerjaan, penilaian otomatis (*Scoring Engine*), konversi skor ke huruf mutu (A, B, C, D, F), dan papan peringkat (*Leaderboard*).

## Fitur Utama
- **Ragam Tipe Soal**: Multiple choice, True/False, Fill-in-the-blank, dan Multiple answer.
- **Pengacakan Fisher-Yates**: Mengacak urutan soal dan opsi jawaban secara adil.
- **Batas Waktu (Timer)**: Pelacakan durasi per sesi kuis.
- **Sistem Penilaian Otomatis**: Perhitungan poin akurat dengan pembobotan per soal.
- **Papan Skor & Riwayat**: Penyimpanan skor tertinggi pemain dan riwayat evaluasi.

## Struktur File (22 File Dart)
- `bin/main.dart`: CLI entry point interaktif.
- `lib/quiz_engine.dart`: Export publik modul.
- `lib/src/models/`: QuestionType, Question, QuizSession, QuizResult, LeaderboardEntry, AnswerSubmission.
- `lib/src/exceptions/`: QuizException.
- `lib/src/repositories/`: QuizRepository.
- `lib/src/services/`: QuizService, ScoringEngine, QuestionShuffler, TimerService, LeaderboardService.
- `lib/src/validators/`: AnswerValidator.
- `lib/src/utils/`: GradeCalculator.
- `lib/src/config/`: QuizConfig.
- `lib/src/application/`: QuizApp.
- `test/unit/`: Pengujian algoritma scoring, grade calculator, dan shuffler.
- `test/integration/`: Pengujian alur kuis lengkap dari mulai sesi hingga penerbitan hasil.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
