import 'dart:io';
import 'package:contact_book/contact_book.dart';

void main(List<String> args) {
  stdout.writeln('==============================================');
  stdout.writeln('          05. CONTACT BOOK CLI                ');
  stdout.writeln('==============================================');

  final app = ContactApp.create();

  app.addContact('Alice Wonderland', '081234567890', 'alice@wonderland.org',
      group: 'Friends');
  app.addContact('Bob Builder', '+628987654321', 'bob@builder.com',
      group: 'Work');
  app.addContact('Charlie Chaplin', '085512348888', 'charlie@comedy.com',
      group: 'Family');

  stdout.writeln('All Contacts in Book:');
  for (final c in app.contactService.listAll()) {
    stdout.writeln('  [${c.group}] ${c.name} - ${c.phone} (${c.email})');
  }

  stdout.writeln('\nFuzzy Search "Alce":');
  final results = app.find('Alce');
  for (final r in results) {
    stdout.writeln('  Match: ${r.name} (${r.phone})');
  }

  stdout.writeln('==============================================');
}
