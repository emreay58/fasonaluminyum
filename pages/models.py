from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class ServicesModel(models.Model):
    image = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle')
    title = models.CharField(max_length=150, verbose_name='Hizmet Başlığı')
    description = models.TextField(verbose_name='Ön Açıklama')
    description1 = RichTextUploadingField(verbose_name='Ana Açıklama')
    image1 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    image2 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    image3 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    image4 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    image5 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    image6 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    image7 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    image8 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    image9 = models.ImageField(upload_to='hizmetler', verbose_name='Resim Ekle', default='static/img/default.png', blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class ProjectModel(models.Model):
    image = models.ImageField(upload_to='project', verbose_name='Resim Ekle')
    title = models.CharField(max_length=150, verbose_name='Hizmet Başlığı')
    description = models.TextField(verbose_name='Ön Açıklama')
    description1 = RichTextUploadingField(verbose_name='Ana Açıklama')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategori Seçin')
    tag = models.ManyToManyField(Tag, verbose_name='Etiket Seçin')
    image1 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    image2 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    image3 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    image4 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    image5 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    image6 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    image7 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    image8 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    image9 = models.ImageField(upload_to='project', verbose_name='Resim Ekle', )
    is_home = models.BooleanField(verbose_name='Ana Sayfada Gösterilsin Mi? (Sadece 4 Proje Gösterebilirsiniz)')
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title
    


class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ad Soyad')
    email = models.EmailField(verbose_name='E-mail')
    tel = models.IntegerField(verbose_name="Telefon")
    subject = models.CharField(max_length=50, verbose_name='Konu')
    mesaj = models.TextField()

    def __str__(self):
        return self.name
    
