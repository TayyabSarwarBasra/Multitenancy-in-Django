from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    USERNAME_FIELD = 'email'
    email = models.EmailField('email address', unique=True, max_length=255)
    username = models.CharField('username', unique=True, max_length=50)
    first_name = models.CharField('first name', max_length=50)
    last_name = models.CharField('last name', max_length=50)
    mobile_number = models.CharField('mobile number', max_length=50)
    business_name = models.CharField('business name', max_length=50)
    password = models.CharField('password', max_length=50)
    address = models.CharField('address', max_length=50)
    auto_create_schema = True
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Domain(DomainMixin):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
