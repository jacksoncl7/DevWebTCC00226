from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        db_table = 'category'
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField('Name', max_length=120, unique=True)
    slug = models.SlugField('Slug', max_length=120, null=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2, default=0)
    desc = models.TextField('Description', blank=True)
    author = models.CharField(max_length=120, null=True)
    img_path = models.CharField(max_length=120, null=True)
    #created_at = models.DateField('Created at', auto_now_add=True)
    #updated_at = models.DateField('Updated at', auto_now=True)
    #img = models.ImageField(upload_to="{% static 'book/images' %}", verbose_name='BookImage', null=True+)

    class Meta:
        db_table = 'book'
        ordering = ('name',)

    def __str__(self):
        return self.name
