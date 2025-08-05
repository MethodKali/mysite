from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'status', 'created_on') #variavel de elementos que serão exibidos na pagina admin
    list_filter = ('status',) #Filtros que serão usados
    search_fields = ('title', 'content') #elementos para o mecanismo de busca
    prepopulated_fields = {'slug':('title',)} #Elementos autopreenchiveis com base no titulo do post

admin.site.register(Post, PostAdmin)