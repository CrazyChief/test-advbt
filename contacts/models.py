from django.db import models
from django.core.urlresolvers import reverse


class Location(models.Model):
    company_name = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=300, null=True)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.company_name + ' ' + self.location


class Phone(models.Model):
    country_prefix = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    def __str__(self):
        return self.country_prefix + ': ' + self.phone


class Email(models.Model):
    PUBLISHED = True
    DRAFT = False
    STATUSES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
    )
    email = models.EmailField(max_length=254)
    is_active = models.BooleanField(choices=STATUSES, default=DRAFT)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email

    def is_email_active(self):
        return self.is_active

    is_email_active.admin_order_field = 'is_active'
    is_email_active.boolean = True
    is_email_active.short_description = 'Is active?'


class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    review = models.TextField()
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ["-date_added"]

    def get_absolute_url(self):
        return reverse('contacts:index')

    def __str__(self):
        return self.name + ' ' + self.email + '(' + str(self.date_added) + ')'















