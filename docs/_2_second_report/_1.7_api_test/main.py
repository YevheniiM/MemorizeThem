from contacts import Contacts
from quickstart import Connections


def main():
    c = Connections()
    users = c.get_all_data()
    contacts = Contacts(users).contacts
    for contact in contacts:
        print(contact)


if __name__ == '__main__':
    main()