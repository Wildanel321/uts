# 08. Task Scheduler

Aplikasi penjadwal tugas (*Task Scheduler & Worker Pool*) tingkat menengah berbasis Dart murni. Menyediakan antrean tugas dengan berbagai tingkat prioritas (*Low, Medium, High, Urgent*), eksekusi satu kali (*one-off*) maupun berulang (*recurring intervals/cron-like*), manajemen konkurensi worker, serta mekanisme *retry* cerdas jika terjadi kegagalan.

## Fitur Utama
- **Manajemen Tugas Berprioritas**: 4 level prioritas untuk menentukan urutan eksekusi pekerjaan.
- **Tugas Berulang & Terjadwal**: Dukungan interval berulang (detik, menit, jam) dan penjadwalan masa depan.
- **Worker Pool Berbasis Dart**: Kolam worker dengan pembatasan konkurensi untuk mencegah *resource exhaustion*.
- **Penanganan Kegagalan (Retry Backoff)**: Percobaan ulang otomatis dengan batas maksimal dan pencatatan riwayat error.
- **Pelacakan Metrik & Audit**: Log riwayat eksekusi, durasi waktu komputasi, dan status tugas kekal.

## Struktur File (22 File Dart)
- `bin/main.dart`: Entry point CLI interaktif.
- `lib/task_scheduler.dart`: Export publik modul.
- `lib/src/models/`: ScheduledTask, TaskStatus, TaskPriority, ExecutionLog, SchedulerMetrics.
- `lib/src/exceptions/`: SchedulerException.
- `lib/src/repositories/`: TaskRepository.
- `lib/src/services/`: CronParser, RetryManager, TaskExecutor, WorkerPool, SchedulerService.
- `lib/src/validators/`: TaskValidator.
- `lib/src/utils/`: TimeUtils.
- `lib/src/config/`: SchedulerConfig.
- `lib/src/application/`: SchedulerApp.
- `test/unit/`: Pengujian prioritas tugas, retry backoff, dan parser ekspresi waktu.
- `test/integration/`: Pengujian alur eksekusi tugas dalam worker pool end-to-end.

## Cara Menjalankan
```bash
dart pub get
dart run bin/main.dart
```
