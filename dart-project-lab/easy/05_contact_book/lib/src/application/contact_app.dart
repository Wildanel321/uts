import '../config/book_config.dart';
import '../models/contact.dart';
import '../models/search_filter.dart';
import '../repositories/contact_repository.dart';
import '../services/contact_service.dart';
import '../services/group_service.dart';
import '../services/search_service.dart';
import '../services/serialization_service.dart';

class ContactApp {
  final BookConfig config;
  final ContactRepository repository;
  final ContactService contactService;
  final SearchService searchService;
  final GroupService groupService;
  final SerializationService serializationService;

  ContactApp({BookConfig? config})
      : config = config ?? const BookConfig(),
        repository = ContactRepository(),
        contactService = ContactService(ContactRepository()),
        searchService = SearchService(ContactRepository()),
        groupService = GroupService(ContactRepository()),
        serializationService = SerializationService(ContactRepository());

  factory ContactApp.create({BookConfig? config}) {
    final repo = ContactRepository();
    return ContactApp._internal(
      config ?? const BookConfig(),
      repo,
      ContactService(repo),
      SearchService(repo),
      GroupService(repo),
      SerializationService(repo),
    );
  }

  ContactApp._internal(
    this.config,
    this.repository,
    this.contactService,
    this.searchService,
    this.groupService,
    this.serializationService,
  );

  Contact addContact(String name, String phone, String email,
      {String group = 'General'}) {
    return contactService.createContact(
        name: name, phone: phone, email: email, group: group);
  }

  List<Contact> find(String query) {
    return searchService.search(SearchFilter(query: query));
  }
}
