from django.db import models

class Book(models.Model):
    # = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    name = models.CharField('Name', max_length=120, unique=True)
    slug = models.SlugField('Slug', max_length=120, null=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2, default=0)
    desc = models.TextField('Description', blank=True)
    created_at = models.DateField('Created at', auto_now_add=True)
    updated_at = models.DateField('Updated at', auto_now=True)
    img = models.ImageField(upload_to="{% static 'book/images' %}", verbose_name='Book Image')
    author = models.CharField(max_length=120, null=True)

    class Meta:
        db_table = 'book'
        ordering = ('name',)

    def __str__(self):
        return self.name
