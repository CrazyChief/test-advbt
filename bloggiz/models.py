from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# class Category(models.Model):
#     PUBLISHED = True
#     DRAFT = False
#     CAT_CHOICES = (
#         (PUBLISHED, _('Published')),
#         (DRAFT, _('Draft')),
#     )
#     name = models.CharField(max_length=150, unique=True)
#     is_active = models.CharField(max_length=20, choices=CAT_CHOICES, default=DRAFT)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = _('Category')
#         verbose_name_plural = _('Categories')

    # def __str__(self):
    #     return self.name


# class Tag(models.Model):
#     title = models.CharField(max_length=30, unique=True, verbose_name=_('Title'))
#     description = models.CharField(max_length=1000, blank=True, verbose_name=_('Description'))
#     is_active = models.BooleanField(default=False, verbose_name=_('Is active'))
#     date_added = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of creation'))
#
#     class Meta:
#         ordering = ['title']
#         verbose_name = _('Tag')
#         verbose_name_plural = _('Tags')
#
#     def __str__(self):
#         return self.title


def upload_path(instance, filename):
    """
    Path to files
    :param instance:
    :param filename:
    :return:
    """
    return "blog/{0}".format(filename)


class Post(models.Model):
    PUBLISHED = True
    DRAFT = False
    POST_CHOICES = (
        (PUBLISHED, _('Published')),
        (DRAFT, _('Draft')),
    )
    title = models.CharField(max_length=500, unique=True, verbose_name=_('Title'))
    slug = models.SlugField(null=True)
    cover_picture = models.FileField(upload_to=upload_path, null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(choices=POST_CHOICES, default=DRAFT, verbose_name=_('Is published'))
    pretext = models.TextField(verbose_name=_('Short content'))
    content = models.TextField(verbose_name=_('Content'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, verbose_name=_('Author'))
    # tag = models.ManyToManyField(Tag, verbose_name=_('Tag'))
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of creation'))

    class Meta:
        ordering = ['-date_added']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    def is_post_published(self):
        return self.is_published

    is_post_published.admin_order_field = 'is_published'
    is_post_published.boolean = True
    is_post_published.short_description = _('Is published?')


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=_('Author'))
    email = models.EmailField(max_length=254)
    comment = models.TextField(verbose_name=_('Comment'))
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of creation'))

    class Meta:
        ordering = ['date_added']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.name

