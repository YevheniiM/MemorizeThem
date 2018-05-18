from .contact import Contact


class Contacts:
    contacts = list()

    def __init__(self, contacts_list):
        """

        :param models_test: list()

        """
        Contacts.contacts.clear()
        Contacts.set_contacts(contacts_list)

    @staticmethod
    def print_contacts():
        for contact in Contacts.contacts:
            print(contact)

    @staticmethod
    def set_contacts(contacts_list):
        for contact in contacts_list:
            c = Contact()
            c.add_information(contact)
            Contacts.contacts.append(c)
