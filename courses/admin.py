from django.contrib import admin

# tem que importar o model primeiro, e a classe
from .models import Course

# registra as opcoes do curso
class CourseAdmin(admin.ModelAdmin):

    # como vai ser exibido na pagina dele
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    # faz com que o campo slug seja preenchido automaticamente
    prepopulated_fields = {'slug': ('name',)}

# Mostra la no admin do proprio Django
admin.site.register(Course, CourseAdmin)
