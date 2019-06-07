from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        db_table = 'categoria'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_cadastro = models.DateField(null=True)
    

    class Meta:
        db_table = 'produto'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
