import '../models/contact_group.dart';
import '../repositories/contact_repository.dart';

class GroupService {
  final ContactRepository repository;

  GroupService(this.repository);

  List<ContactGroup> getAvailableGroups() {
    final groupNames = repository.getAll().map((c) => c.group).toSet();
    groupNames.addAll(['General', 'Family', 'Work', 'Friends']);
    return groupNames.map((g) => ContactGroup(name: g)).toList();
  }

  int countByGroup(String groupName) {
    return repository
        .getAll()
        .where((c) => c.group.toLowerCase() == groupName.toLowerCase())
        .length;
  }
}
