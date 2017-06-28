from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField("Tytuł", max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField("Wpis")
    pub_date = models.DateTimeField("Data publikacji", auto_now_add=True)
    last_modified = models.DateTimeField("Data aktualizacji", auto_now=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.slug:
                self.slug = slugify(unidecode(self.title))
            else:
                self.slug = slugify(unidecode(self.slug))

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Author(models.Model):
    pass


class Comment(MPTTModel):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', blank=True, null=True)
    author = models.CharField("Autor", max_length=255)
    text = models.TextField("Komentarz")
    pub_date = models.DateTimeField("Data publikacji", auto_now_add=True)

    def __str__(self):
        return "%s:  %s" % (self.author, self.text)


class Rating(models.Model):
    pass
