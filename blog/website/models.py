from django.db import models

class Categories(models.TextChoices):
        TECH = 'TC', 'Tecnology'
        CR = 'CR', 'Curiosity'
        GR = 'GR', 'Geral'
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices= Categories.choices,
        default= Categories.GR
    )
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_category_label(self):
        return self.get_categories_display()

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

