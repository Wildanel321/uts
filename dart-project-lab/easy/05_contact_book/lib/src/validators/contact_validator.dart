import '../models/contact.dart';
import '../exceptions/validation_exception.dart';

class ContactValidator {
  static void validate(Contact contact) {
    if (contact.name.trim().isEmpty) {
      throw ValidationException('Contact name cannot be empty.');
    }

    if (contact.phone.trim().isEmpty) {
      throw ValidationException('Contact phone number cannot be empty.');
    }

    final emailRegex = RegExp(r'^[\w\.\-]+@[\w\.\-]+\.[a-zA-Z]{2,}$');
    if (contact.email.isNotEmpty && !emailRegex.hasMatch(contact.email)) {
      throw ValidationException(
          'Invalid email address format: ${contact.email}');
    }
  }
}
