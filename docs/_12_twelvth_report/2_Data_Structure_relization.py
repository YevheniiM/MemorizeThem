from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'patronymic', 'country', 'city', 'flat_number', 'house_number',
                  'email', 'mobile_phone', 'work_phone', 'home_phone', 'job',
                  'biography', 'interests', 'photo']