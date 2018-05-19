from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Contact(models.Model):
    name = models.CharField(max_length=128, default="", null=True, blank=True)
    surname = models.CharField(max_length=128, default="", null=True, blank=True)
    patronymic = models.CharField(max_length=128, default="", null=True, blank=True)
    email = models.EmailField(default="", null=True, blank=True)
    mobile_phone = models.CharField(max_length=32, default="", null=True, blank=True)
    work_phone = models.CharField(max_length=32, default="", null=True, blank=True)
    home_phone = models.CharField(max_length=32, default="", null=True, blank=True)
    birthday = models.DateField(default=None, null=True, blank=True)
    gender = models.CharField(max_length=16, default="", null=True, blank=True)
    biography = models.CharField(max_length=10000, default="", null=True, blank=True)
    interests = models.CharField(max_length=1000, default="", null=True, blank=True)
    photo = models.URLField()
    job = models.CharField(max_length=250, default="", null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # needs to be unique
    postal_code = models.CharField(max_length=64, default="", null=True, blank=True)
    country = models.CharField(max_length=64, default="", null=True, blank=True)
    city = models.CharField(max_length=64, default="", null=True, blank=True)
    street = models.CharField(max_length=64, default="", null=True, blank=True)
    house_number = models.CharField(max_length=16, default="", null=True, blank=True)
    flat_number = models.CharField(max_length=16, default="", null=True, blank=True)

    def __unicode__(self):
        return '{0} {1} {2}'.format(
            self.name, self.surname, self.patronymic
        )


from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'patronymic', 'country', 'city', 'flat_number', 'house_number',
                  'email', 'mobile_phone', 'work_phone', 'home_phone', 'job',
                  'biography', 'interests', 'photo']
