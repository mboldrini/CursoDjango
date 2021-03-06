from django.db import models

# Create your models here.

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
           models.Q(name__icontains=query) | \
           models.Q(description__icontains=query)
        )



class Course(models.Model):

    name = models.CharField( 'Nome', max_length=150 )
    slug = models.SlugField( 'Atalho' )
    description = models.TextField( 'Descricao Simples', blank=True )
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField( 'Data de Inicio', null=True, blank=True )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        'Criado Em',
        auto_now_add=True
    )
    updated_at = models.DateTimeField( 'Atualizado em', auto_now=True )

    objects = CourseManager()

    # retorna o nome da Classe na pagina de admin
    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('courses:details', (), {'slug': self.slug} )

    # muda o nome la no botao de adicionar curso novo
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        #como vai ser organizado os cursos, por nome no caso
        ordering = ['name']