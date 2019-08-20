from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body1 = RichTextUploadingField(default='SOME STRING')
    body2 = RichTextUploadingField(default='SOME STRING')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

class Image(models.Model):
    pic = models.ImageField(upload_to='media/', blank=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def image_img(self):
        if self.pic:
            return u'' % self.pic.url
        else:
            return '(none)'

    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

class About(models.Model):
    title = models.CharField(max_length=150)
    body1 = RichTextUploadingField(default='SOME STRING')
    body2 = RichTextUploadingField(default='SOME STRING')
