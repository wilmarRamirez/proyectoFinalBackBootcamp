from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Create your models here.
class Exclusive(models.Model):
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    valor_anterior =models.CharField(max_length=100)
    valor_actualizado =models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="exclusive", null=True)
    #url_imagen = models.CharField(null=True)

class Best(models.Model):
    ciudad_pais = models.CharField(max_length=100)
    dia_prueba = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="best", null=True)
    #url_imagen = models.CharField(null=True)

class LatestBlog(models.Model):
    title = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="latestBlog", null=True)
    #url_imagen = models.CharField(null=True)


'''
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
class Post(TimeStampedModel, SoftDeletableModel):
	title = models.CharField(max_length=50, null=False, blank=True)
	body = models.TextField(max_length=5000, null=False, blank=True)
	date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
	slug = models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.title
'''