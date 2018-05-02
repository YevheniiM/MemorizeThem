import httplib2
from apiclient import discovery
from credentials import get_credentials


class Connections:
    def __init__(self):
        self.credentials = get_credentials()

    def get_connections(self, fields):
        http = self.credentials.authorize(httplib2.Http())
        print(type(http))
        service = discovery.build('people', 'v1', http=http,
                                  discoveryServiceUrl='https://people.googleapis.com/$discovery/rest')
        print(type(service))

        results = service.people().connections().list(
            resourceName='people/me',
            personFields=','.join(fields)
        ).execute()
        print(type(results))

        return results.get('connections', [])

    def get_all_data(self):
        users = list()

        connections = self.get_connections(
                [
                    'addresses', 'biographies', 'birthdays',
                    'emailAddresses', 'genders', 'interests',
                    'phoneNumbers', 'photos', 'names'
                ]
        )
        for person in connections:

            names = person.get('names', [])
            addresses = person.get('addresses', [])
            biographies = person.get('biographies', [])
            birthdays = person.get('birthdays', [])
            email = person.get('emailAddresses', [])
            genders = person.get('genders', [])
            interests = person.get('interests', [])
            phone = person.get('phoneNumbers', [])
            photos = person.get('photos', [])
            person_info = dict()

            if len(names) > 0:
                user_name = names[0].get('displayName')
                user_id = names[0].get('metadata', dict()).get('source', dict()).get('id', '')
                person_info['ID'] = user_id
                person_info['name'] = user_name

            if len(addresses) > 0:
                user_address = dict()
                user_address['country'] = addresses[0].get('country', '')
                user_address['postalCode'] = addresses[0].get('postalCode', '')
                user_address['city'] = addresses[0].get('city', '')
                user_address['streetAddress'] = addresses[0].get('streetAddress', '')
                person_info['address'] = user_address

            if len(biographies) > 0:
                user_biography = biographies[0].get('value', '')
                person_info['biography'] = user_biography

            if len(birthdays) > 0:
                user_birthday = dict()
                birthday = birthdays[0].get('date', {})
                user_birthday['day'] = birthday.get('day', '')
                user_birthday['month'] = birthday.get('month', '')
                user_birthday['year'] = birthday.get('year', '')
                person_info['birthday'] = user_birthday

            if len(email) > 0:
                user_email = email[0].get('value', '')
                person_info['email'] = user_email

            if len(genders) > 0:
                user_gender = genders[0].get('value', '')
                person_info['gender'] = user_gender

            if len(interests) > 0:
                user_interest = interests[0].get('value', '')
                person_info['interests'] = user_interest

            if len(phone) > 0:
                user_phone = dict()
                user_phone['formatted'] = phone[0].get('formattedType', '')
                user_phone['type'] = phone[0].get('type', '')
                user_phone['phone'] = phone[0].get('value', '')
                person_info['phone'] = user_phone

            if len(photos) > 0:
                photo = photos[0].get('url', '')
                person_info['photo'] = photo

            users.append(person_info)

        return users