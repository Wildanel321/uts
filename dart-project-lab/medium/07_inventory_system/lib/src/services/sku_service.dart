import '../repositories/product_repository.dart';
import '../utils/sku_generator.dart';

class SkuService {
  final ProductRepository repository;

  SkuService(this.repository);

  String createSku(String category, String productName) {
    final count = repository.getAll().length + 1;
    return SkuGenerator.generate(category, productName, count);
  }

  bool isSkuUnique(String sku) => repository.findBySku(sku) == null;
}
