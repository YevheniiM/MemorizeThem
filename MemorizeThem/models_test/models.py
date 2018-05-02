from django.db import models


class Address(models.Model):
    postal_code = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.CharField(max_length=16)
    flat_number = models.CharField(max_length=16)


class Contact(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=32)
    work_phone = models.CharField(max_length=32)
    home_phone = models.CharField(max_length=32)
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
    birthday = models.DateField()
    gender = models.CharField(max_length=16)
    biography = models.CharField(max_length=10000)
    interests = models.CharField(max_length=1000)
    photo = models.URLField()

    def __unicode__(self):
        return '{0} {1} {2}'.format(
            self.name, self.surname, self.patronymic
        )


