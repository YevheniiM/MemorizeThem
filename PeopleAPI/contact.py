class Contact:
    def __init__(self):
        self.name = None
        self.ID = None
        self.email = None
        self.address = dict()
        self.biography = None
        self.birthday = dict()
        self.gender = None
        self.interests = None
        self.phone_number = dict()
        self.photos = None

    def add_information(self, info_dict):
        self.name = info_dict.get('name', None)
        self.ID = info_dict.get('ID', None)
        self.email = info_dict.get('email', None)
        self.address = info_dict.get('address', dict())
        self.biography = info_dict.get('biography', None)
        self.birthday = info_dict.get('birthday', dict())
        self.gender = info_dict.get('gender', None)
        self.interests = info_dict.get('interests', None)
        self.phone_number = info_dict.get('phone', dict())
        self.photos = info_dict.get('photo', None)

    def __str__(self):
        final_user_info = '---------------------------------------------\n'
        final_user_info += '{0}: {1} (id)\n'.format(self.name, self.ID)
        if self.email:
            final_user_info += 'Email: {0}\n'.format(self.email)
        if self.address:
            final_user_info += 'Address: {0}\n'.format(self.address)
        if self.biography:
            final_user_info += 'Biography: {0}\n'.format(self.biography)
        if self.birthday:
            final_user_info += 'Birthday: {0}\n'.format(self.birthday)
        if self.gender:
            final_user_info += 'Gender: {0}\n'.format(self.gender)
        if self.interests:
            final_user_info += 'Interests: {0}\n'.format(self.interests)
        if self.phone_number:
            final_user_info += 'Phone number: {0}\n'.format(self.phone_number)
        if self.photos:
            final_user_info += 'Photos: {0}\n'.format(self.photos)
        final_user_info += '---------------------------------------------\n'

        return final_user_info
