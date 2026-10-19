import '../repositories/product_repository.dart';

class CsvService {
  final ProductRepository repository;

  CsvService(this.repository);

  String exportToCsv() {
    final buffer =
        StringBuffer('id,sku,name,category,unitPrice,quantity,minStock\n');
    for (final p in repository.getAll()) {
      buffer.writeln(
          '${p.id},${p.sku},${p.name},${p.category},${p.unitPrice},${p.quantity},${p.minStockThreshold}');
    }
    return buffer.toString();
  }
}
